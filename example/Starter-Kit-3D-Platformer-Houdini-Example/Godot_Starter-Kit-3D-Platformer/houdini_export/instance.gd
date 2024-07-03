extends Node

"""
Note:
.csv suffix are producing Errors in Godot Engine use .txt

"""
@export_file("Instance File")
var instance_filename 	= "res://houdini_export/instance.txt"
@export_file("Assets File")
var assets_filename 	= "res://houdini_export/assets.txt"
@export
var delimeter 			= ","

func _ready():
	"""
	Preload all Assets onces in a Array
	
	Data: Type,AssetsName,CustomValue...
		Type: 	0 => Default Object
				1 => Has Custom Value
	"""
	var f = FileAccess.open(assets_filename, FileAccess.READ)
	var preLoad_Assets = []			# Array of Loaded Assets
	var preLoad_Assets_list= []		# Array of all Asset and Custom Attribute 
	while not f.eof_reached():
		var line = f.get_csv_line(delimeter)
		if line.size() < 2:
			continue
		preLoad_Assets.append(load(str(line[1])))
		preLoad_Assets_list.append(line)
	f.close()
	
	"""
	Load Instance Data and create Instances
	""" 
	f = FileAccess.open(instance_filename, FileAccess.READ)
	# Splitting the CSV File
	while not f.eof_reached():
		var line = f.get_csv_line(delimeter)
		
		# Instancing 
		var o = preLoad_Assets[int(line[0])].instantiate()

		# Set Default Values | Note: Basis is Orientation of the Object
		o.basis 	= Basis(Quaternion(float(line[1]), float(line[2]), float(line[3]), float(line[4])))
		o.position 	= Vector3(float(line[5]), float(line[6]), float(line[7]))
		o.scale		= Vector3(float(line[8]), float(line[9]), float(line[10]))
		
		# Custom Attributes
		if preLoad_Assets_list[int(line[0])][0]:
			for i in range(2,len(preLoad_Assets_list[int(line[0])])):
				o[preLoad_Assets_list[int(line[0])][i]] = line[9 + i]
				# For Testing
				# print(preLoad_Assets_list[int(line[0])][i] + " | ", o[preLoad_Assets_list[int(line[0])][i]])

		add_child(o)
	f.close()
