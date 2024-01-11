extends Node

@export_file("Instance File")
var instance_filename 	= "res://houdini_export/instance.csv"
@export_file("Assets File")
var assets_filename 	= "res://houdini_export/assets.csv"
@export
var delimeter 			= ","

func _ready():
	"""
	Preload all Assets onces in a Array
	"""
	var f = FileAccess.open(assets_filename, FileAccess.READ)
	var pf_objects = []
	while not f.eof_reached():
		pf_objects.append(load(f.get_line()))
	f.close()

	"""
	Load Instance Data and create Instances
	""" 
	f = FileAccess.open(instance_filename, FileAccess.READ)
	# Splitting the CSV File
	while not f.eof_reached():
		var line = f.get_csv_line(delimeter)
		# Instancing
		var o = pf_objects[int(line[0])].instantiate()
		o.position 	= Vector3(float(line[5]), float(line[6]), float(line[7]))
		o.basis 	= Basis(Quaternion(float(line[1]), float(line[2]), float(line[3]), float(line[4])))
		o.scale		= Vector3(float(line[8]), float(line[9]), float(line[10]))
		add_child(o)
	f.close()
	
	var node = self.get_node(".")
	node.owner = get_tree().edited_scene_root
