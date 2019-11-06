from string import Template


# import hou


class GodotNodes():
    class _scenetree():
        header = "[gd_scene load_steps=3 format=2]\n\n"     # cheap but it works
        ext_resource = {}
        sub_resource = {}
        node = {}

    def __init__(self):
        # this is empty
        print "init"

    def scene_cleanup(self):
        self._scenetree.ext_resource.clear()
        self._scenetree.sub_resource.clear()
        self._scenetree.node.clear()

    def debug_scenetree(self):
        return self._scenetree.node

    def add_node_value(self, name, nodetype="", parent="", node={}):
        """
        Creates a Dict with node values
        :param name: Node Name
        :param nodetype: Node Type
        :param parent: Position of Node
        :param node: Node Parameters as a Dict
        :return: None
        """

        node_count = self._scenetree.node.__len__()
        if parent == "":
            node = {node_count: {"name": name, "type": nodetype, "index": node_count, "node": node}}
        else:
            node = {node_count: {"name": name, "type": nodetype, "parent": parent, "index": node_count, "node": node}}
        self._scenetree.node.update(node)

    def add_ext_ressource(self, asset_path, asset_name, nodetype="ArrayMesh" ):

        node_count = self._scenetree.ext_resource.__len__()
        node = {node_count: {"type": nodetype, "id": node_count + 1, "path": "res://{}{}".format(asset_path, asset_name)}}
        self._scenetree.ext_resource.update(node)
        return node_count + 1

    def _add_sub_resource_value(self, name, nodetype="", node={}):
        """
        Adds Sub Resource
        :param name: 
        :param nodetype: 
        :param node: 
        :return: sub resource id
        """

        node_count = self._scenetree.sub_resource.__len__()
        node = {node_count: {"name": name, "type": nodetype, "index": node_count + 1, "node": node}}
        self._scenetree.sub_resource.update(node)
        return node_count + 1

    def Node(self, name, parent=""):
        self.add_node_value(name=name, nodetype="Node", parent=parent)

    def Spatial(self, name, parent=""):
        self.add_node_value(name=name, nodetype="Spatial", parent=parent)

    def create_scene(self, filename):
        # Create a File in Write mode
        f = open(filename, "w")

        # Add Default Header
        f.writelines(self._scenetree.header)

        def i_head(nodes, attribute_list=[], start_header=""):
            header = ""
            for i in range(0, len(nodes)):
                header += start_header
                for attr in attribute_list:
                    value = nodes[i].get(attr, "___NONE___")
                    if value != "___NONE___":
                        header += "{}=\"{}\" ".format(str(attr),str(value))
                header += "]\n\n"

                ##############
                # ATTRIBUTES #
                ##############

                # Add Attributes
                if nodes[i].get("node") != None:
                    for attr in nodes[i]["node"]:
                        header += "{} = {}\n".format(str(attr), str(nodes[i]["node"][attr]))

            return header

        print self._scenetree.node

        #################
        # EXT Ressource #
        #################

        nodes = self._scenetree.ext_resource
        print nodes
        header = i_head(nodes,["path", "type", "id"], "\n[ext_resource ")
        f.writelines(header)

        ##########
        # HEADER #
        ##########

        # Add Node Header and Attributes
        nodes = self._scenetree.node
        header = i_head(nodes, ["name", "type", "parent", "index"], "\n[node ")

        # Write to File
        f.writelines(header)


        # Save File and Close
        f.close()



def test_Node():
    n = GodotNodes()
    n.Node("abc")
    n.Spatial("Spatial", parent=".")
    n.create_scene("test")


if __name__ == "__main__":
    test_Node()
