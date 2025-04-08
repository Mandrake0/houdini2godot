import os
import godot
import houdini_godot_helper as hgh

#
# Create Asset GLTF  
#

def create_asset_GLTF(node, assetFolder, assetName, sopPath, flagType="Render", gltfFileType=".gltf"):
    try:
        # get child node with renderflag
        type = hou.nodeFlag.Render
        if (flagType != "Render"):
            type = hou.nodeFlag.Display
            
        child = hou.node(sopPath).children()
        for n in child:
            path = sopPath + "/" + str(n)
            if(hou.node(path).isGenericFlagSet(type)):
                # Create Path of not exist
                gltf_folder = assetFolder + assetName
                if not os.path.exists(gltf_folder):
                    os.makedirs(gltf_folder)
                
                gltf_file = gltf_folder + "/" + assetName + gltfFileType
                
                # Set Parameters
                node.parm('file').set(gltf_file)
                node.parm('soppath').set(path)
    
                # execute 
                node.parm("execute").pressButton()
                
                # clean up
                node.parm('file').set('')
                node.parm('soppath').set('')
                return
    except hou.OperationFailed:
        print("Cannot Execute Exporter")
                    
#
# Create Asset Scene     
#                
def create_asset_scene(projectFolder, assetFolder, assetName, gltf_filetype, godotFileType=".tscn"):
    
    gs = godot.Scene()
    gn = godot.Node(node_name=assetName)
    gn.add_external_ressource(assetFolder + "/" + assetName + "/" + assetName + gltf_filetype, id=1)
    gs.add_node(gn)

    gs.create_scene_file(folder=projectFolder + assetFolder, filename=assetName + godotFileType)

#
# Create Light Scene     
#    
def create_light_scene(projectFolder, assetFolder, asset, assetName, godotFileType=".tscn"):
    
    # Get some Parms Values
    node = hou.node(asset)
    light_type = node.parm("godot_light_type").eval()


    # Reading all Parameters from the Godot Light HDA
    parm_list = [
        ["light_color", "color"],
        ["light_energy", "float"],
        ["light_indirect_energy", "float"],
        ["light_negative", "bool"],
        ["light_specular", "float"],
        ["light_bake_mode", "int"]
    ]
    
    if(node.parm("shadow_enabled").evalAsInt()):
        list = [
            ["shadow_enabled", "int"],
            ["shadow_color", "color"],
            ["shadow_bias", "float"],
            ["shadow_reverse_cull_face", "bool"]
        ]
        
        parm_list.extend(list)
    
    if(light_type == "DirectionalLight"):
        list = [
            ["directional_shadow_mode", "int"],
            ["directional_shadow_split_1", "float"],
            ["directional_shadow_split_2", "float"],
            ["directional_shadow_split_3", "float"],
            ["directional_shadow_blend_splits", "bool"],
            ["directional_shadow_normal_bias", "float"],
            ["directional_shadow_bias_split_scale", "float"],
            ["directional_shadow_depth_range", "int"],
            ["directional_shadow_max_distance", "float"],
            ["shadow_enabled", "bool"]
        ]
        parm_list.extend(list)

    if(light_type == "OmniLight"):
        list = [
            ["omni_range", "float"],
            ["omni_attenuation", "float"],
            ["omni_shadow_mode", "int"],
            ["omni_shadow_detail", "int"]
        ]
        parm_list.extend(list)
        
    if(light_type == "SpotLight"):
        list = [
            ["spot_range", "float"],
            ["spot_attenuation", "float"],
            ["spot_angle", "float"],
            ["spot_angle_attenuation", "float"]
        ]
        parm_list.extend(list)     
        
    # Create Light Scene File    
    gs = godot.Scene()
    gn = godot.Node(node_name=assetName, node_type=light_type)
    gn.add_parameter_list(parameter_list=hgh.houdini_parameter_to_list(node, parm_list))
    gs.add_node(gn)
    
    folder = projectFolder + assetFolder
    filename = assetName + godotFileType
    gs.create_scene_file(folder, filename)

    
#
# Create Asset
#    
def createAsset():
    # Execute
    node = hou.pwd()
    projectFolder   = node.parm('project_folder').evalAsString()
    assetFolder     = node.parm("asset_folder").evalAsString()
    exportfolder    = projectFolder + assetFolder
    assetList       = node.parm("asset_list")
    godotFileType   = node.parm("godot_filetype").evalAsString()
    gltfFileType    = node.parm("gltf_filetype").evalAsString()
    flagType        = node.parm("asset_flag_type").evalAsString()
    
    
    for asset in assetList.evalAsNodes():
        # get Asset Name
        assetName = asset.name()
        
        
        # Export Godot Lights (no other ligts get Exported
        if(asset.type().name() == "godot_light"):
            create_light_scene(projectFolder, assetFolder, asset, assetName, godotFileType)
        
        # Export Geometry    
        elif(asset.type().name() == "geo"):
            if(node.parm('gltf_export').evalAsInt()):
                create_asset_GLTF(node, exportfolder, assetName, asset.path(), gltfFileType, flagType)
            
            if(node.parm('scene_file_export').evalAsInt()):
                create_asset_scene(projectFolder, assetFolder, assetName, godotFileType, gltfFileType)
        else:
            # Error Message if the Asset is not a valid Object
            print("The Asset: " + assetName + " doesn't get Exported there is no Export Function for it")


# Callback Function for add "/" 
def folderCallback(kwargs, name):
    v = kwargs["parm"].eval()
    if(v[-1:] != "/"):
        kwargs["parm"].set(v + "/")

