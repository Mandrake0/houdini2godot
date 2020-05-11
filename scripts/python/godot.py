import os


class Scene():
    
    def __init__(self,scene_load_steps=2, scene_format=2):
        self.load_steps = scene_load_steps
        self.format = scene_format
        self.node = []

    
    def add_node(self, godotNode):
        self.node.append(godotNode)

    def create_scene(self):
        header = "[gd_scene load_steps={} format={}]\n\n"
        out = header.format(str(self.load_steps), str(self.format))

        for n in self.node:
            out += str(n)

        return out

    def create_scene_file(self, folder, filename):
        # Create Folder if not Exist
        if not os.path.exists(folder):
            os.makedirs(folder)
        # Create full filepath
        full_filename = folder        
        if (folder[-1:] != "/"):
            full_filename += "/"
        full_filename += filename

        f = open(full_filename, "w")
        f.write(self.create_scene())
        f.close()

    
# Create a Node
class Node(object):
    
    def __init__(self, node_name, node_type="Node", parent=""):
        self.name = node_name
        self.type = node_type
        self.parent = parent
        self.parm = []
        self.ext = ""
        self.id = 0
 
    def add_parameter(self, parm_name, parm_value):
        parm_obj = {
            "name": parm_name,
            "value": parm_value
        }
        self.parm.append(parm_obj)

    def add_parameter_list(self, parameter_list):
        """
        Example Parameter List: [["Parm_01", "Hello"], ["Parm_02", "World"]]
        """
        for parm in parameter_list:
            self.add_parameter(parm[0], parm[1])
    
    def add_external_ressource(self, ext_path, id, exp_type="PackedScene"):
        header = "[ext_resource path=\"res://{}\" type=\"{}\" id={}]\n"
        self.ext = header.format(ext_path,exp_type,str(id))
        self.id = id

    def __str__(self):
        out = ""
        if self.ext != "":
            out += self.ext
            header = "[node name=\"{}\" instance=ExtResource( {} )]\n"
            out += header.format(self.name, str(self.id))
        else:
            out += self.ext
            header = "[node name=\"{}\" type=\"{}\"]\n"
            out += header.format(self.name, self.type)

        if self.parm.__len__() > 0:
            for p in self.parm:
                out += p["name"] + " = " + str(p["value"]) + "\n"
        
        return out + "\n"


if __name__ == "__main__":
    print("Example Setup with External Ressource:\n")
    gs = Scene()

    gn0 = Node("blabla name", "Sprite")
    gs.add_node(gn0)

    gn1 = Node("bla", "Sprite")
    gn1.add_external_ressource("path/to/ressource",1)
    gn1.add_parameter("Example_parm", "123")
    gs.add_node(gn1)

    print(gs.create_scene())
    gs.create_scene_file("test", "file.tscn")
