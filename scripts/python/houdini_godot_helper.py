"""
Helper Functions for the Houdini Godot Exporter

"""

import hou

def houdini_parameter_to_list(node, list):
    data = []
    for item in list:
        name = item[0]
        type = item[1]

        p = node.parm(name)
        res = ""
        if(type == "int"):
            res = str(p.evalAsInt())
        if(type == "float"):
            res =  str(p.evalAsFloat())
        if(type == "color"):
            r = str(node.parm(name + "r").eval())
            g = str(node.parm(name + "g").eval())
            b = str(node.parm(name + "b").eval())
            res = "Color( " +r+ ", " +g+ ", " +b+ ", 1 )" 
        if(type == "bool"):
            res = str(bool(p.evalAsInt())).lower()   
            
        data.append([name, res])
    return data