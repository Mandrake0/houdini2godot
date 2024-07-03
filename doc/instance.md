# Instance

There is currently no Binary Fileformat but there are some Options in the Godot Scene Exporter.

Exported Attributes: instance, orient, P, scale

Godot Scene Exporter does converte N to orient automaticly but it could have small mismatch.

## Custom Attributes

It is Possible to Export Custom Attributes to Godot

Please see in the Example Project: Starter-Kit-3D-Platformer-Houdini-Example

### Godot
There is the Scene File cloud_houdini.tscn with the cloud_houdini.gd

### Houdini
File: Level-Generator.hiplc
In the Instance Node there is a special Setup how to Export Custom Parameters for Godot

The Godot Exporter detects the Parameters (godot_parm_* and godot_parms) and Export it.
