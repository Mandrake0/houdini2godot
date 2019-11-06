# Houdini2Godot

Proof of concept 

*NOTE: There are some bad Bugs* 

## Installation

For adding the Files it requires to modify the houdini.env:

```Bash

####################
# houdini.env
####################
# example Windows
####################

#
# GODOT_LIB : Set the Path to the Houdini2Godot Installation Path 
# 

GODOT_LIB="C:\Development\houdini2godot"
GODOT_HDA=$GODOT_LIB/hda

# Add the Paths to the Houdini Variables

HOUDINI_OTLSCAN_PATH = $GODOT_HDA;@/otls
HOUDINI_PATH = $GODOT_LIB;&

```

There is also the Possability for using a XML File.


## Videos

[Example Instancing](https://vimeo.com/279678590)

## Ressources

The Full File Descripton doesn't exist but there is the Blender Exporter that could be used as Reference.

[Godot Doc TSCN](https://docs.godotengine.org/en/3.1/development/file_formats/tscn.html)

[Blender Exporter Example Files](https://github.com/godotengine/godot-blender-exporter/tree/master/tests)

