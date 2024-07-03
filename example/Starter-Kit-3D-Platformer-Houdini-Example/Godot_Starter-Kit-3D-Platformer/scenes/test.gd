extends Node3D

var obj = load("res://objects/cloud_houdini.tscn")

# Called when the node enters the scene tree for the first time.
func _ready():
	
	obj.set("random_time", 2.4)

	print(obj.get("position"))
#	print(obj.get_method_list())
	print(obj.get("random_time"))
#	print(obj.get("random_velocity"))

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
