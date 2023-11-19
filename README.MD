# Houdini2Godot

**Made for Godot 4.x**

**Houdini Project Files are made with H20**

Exports TSCN and ESCN Files with gltf as ressources.
Scense can be Exported with customized Godot Instancer. 

## Development

**Please give some Feedback what type of Features are needed.** 

Currently there are no plans to create a custom exporter for Animations, Bones because GLTF should solve this requirement.

I am not a Godot Game Developer the question is how the Tools can be used Productive for a Artist! Feedback are Welcome

## Installation

1. Download Current Repository
2. Extract to preferd Directory
3. Move houdini2godot.json to the Houdini User Package Folder | **Note: There is Windows SETUP Script**
4. Edit houdini2godot.json and set the Path
5. Start Houdini and check if the Godot Assets are loaded Networkview:(Tab -> Godot)
    There is also Godot Shelf but currently not required

### Package

Use the Package JSON file for Houdini. 
You need to set the path Manualy in the file.

[SideFx Doc](https://www.sidefx.com/docs/houdini/ref/plugins.html)

#### Windows
Run *windows_setup.ps1* in Powershell to Setup Godot2Houdini with the correct Path's

## Example Starter-Kit-3D-Platformer-Houdini-Example

**Ideal for Starters**

Project is Setuped with Relative Paths, should work out the box. (Tested on Windows 10)

![Houdini](/help/images/Houdini_StarterKit3DPlatformer.PNG)

Houdini Scene Setup

![Houdini](/help/images/Godot_StarterKit3DPlatformer.PNG)

Godot Project

**Note: The Scene gets only loaded at Runtime of the Game. In the Editor the Scene can't be seen!!!**

## Example 

There are Project Files for Godot Engine and a hip File for Houdini
The Godot Project requires the data from houdini to work.

To Export corrctly in Houdini it requires to change the Godot Project Folder in the Node's: 
* godot_asset_export
* godot_scene_export

## Videos

Old Video of the Proof of Concept:
[Example Instancing](https://vimeo.com/279678590)

## Ressources

The Full File Descripton doesn't exist but there is the Blender Exporter that could be used as Reference.

[Godot Doc TSCN](https://docs.godotengine.org/en/3.1/development/file_formats/tscn.html)

[Blender Exporter Example Files](https://github.com/godotengine/godot-blender-exporter/tree/master/tests)

# Credit

**Big Credit to Kenney for the Godot Example Scene THANK YOU.**

**https://www.kenny.nl**