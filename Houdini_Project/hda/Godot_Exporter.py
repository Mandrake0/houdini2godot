import hou
import houdini2godot


def console_message(node):
    print "\nRunning Exporter\n"
    print "=======================\n"
    list = ["selectedObjects","projectFolder"]
    for l in list:
        value = node.parm(l).eval()
        print l + ": " + value + "\n"
        if value == "":
            hou.ui.displayMessage("There is no Value in " + l, severity=hou.severityType.Error)
            return
    print "======================="

def create_mesh(node_current, node_export_path):
       
    # Export File
    export_node = hou.node("./ropnet/export")
    export_node.parm("soppath").set(node_current.path())
    export_node.parm("sopoutput").set(node_export_path)
    export_node.render()
    
    # Cleanup
    export_node.parm("soppath").set("")
    export_node.parm("sopoutput").set("")

def create_geo_meshinstance(houdini2godot, node, project_folder=""):

    # Create File pathname
    node_name = node.name()
    node_asset_folder = node.parm("assetFolder").eval()
    node_asset_name = node.parm("assetName").eval()

    # Setup for Mesh File Export
    if node_asset_name != "":
        node_name = node_asset_name

    if node_asset_folder != "":
            project_folder += node_asset_folder

    node_export_path = project_folder + node_name + ".obj"
    create_mesh(node, node_export_path)

    id_ext = houdini2godot.add_ext_ressource(node_asset_folder, node_name + ".tscn", nodetype="ArrayMesh" )

    node_get_values = ""
    node_parms = {"mesh" : "ExtResource( " + id_ext + " )"}

    # Return for usage directly hg.add_node_value()
    return node_name, "MeshInstance", "", node_parms


def run_export():

    # Godot Node
    node_exp = hou.pwd()

    # Console Message some Information
    console_message(node_exp)
    
    # Get Global Parameters
    exp_data_so = node_exp.parm("selectedObjects").eval()
    exp_data_pf = node_exp.parm("projectFolder").eval()

    # Safety Message
    if exp_data_pf == "":
        hou.Mhou.ui.displayMessage("Add Project Folder Path", severity=hou.severityType.ImportantMessage)
        return

    # Get Nodes by Pattern
    nodes_list = hou.node("/").glob(exp_data_so)
    # print nodes_list

    if node_exp.parm("singleScene").eval() == 1:
        hg = houdini2godot.GodotNodes()
        hg.scene_cleanup()
    
    for node in nodes_list:
        node_type = node.type().name()

        if node_exp.parm("singleScene").eval() == 0:
            hg = houdini2godot.GodotNodes()
            hg.scene_cleanup()

        # Selects only Nodes with Geo Attribute          
        if node_type == "geo":
            hg.add_node_value(create_geo_meshinstance(hg, node, exp_data_pf))







