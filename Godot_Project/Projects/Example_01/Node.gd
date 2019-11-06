extends Node

var cvs_filename = "res://inst_points.csv"
var preload_filename = "res://inst_obj.csv"

func load_file(filename):
	var result = {}
	var f = File.new()
	f.open(filename, f.READ)
	var index = 1
	while not f.eof_reached():
    	var line = f.get_line()
    	result[str(index)] = line
    	index += 1
	f.close()
	return result

# var instance_object = preload("res://Scenes/box_object1.tscn")

func _ready():
	
	# Preload all Objects onces in a Array
	var pf = load_file(preload_filename)
	var pf_objects = {}
	var pf_index = 0
	
	for i in range(1, pf.size()):
		pf_objects[str(pf_index)] = load(pf[str(i)])
		pf_index += 1
	
	
	
	###########################################
	var r = load_file(cvs_filename)
	
	# Splitting the CSV File
	for i in range(1, r.size()):
		var line = r[str(i)]
		line = line.split(",")

		# Getting the Data and set it in order 
		var instance = str(line[0])
		var orient = Vector3(line[1], line[2], line[3])
		var position = Vector3(line[4], line[5], line[6])
		var scale = Vector3(line[7], line[8], line[9])

		# Instancing
		# Instancing with load is Slow how can that be optimized?
		var instance_object = pf_objects[instance] 
		# var instance_object = load(instance) 
		var o = instance_object.instance()
		o.set_translation(position)
		o.set_rotation_degrees(orient)
		o.set_scale(scale)
		add_child(o)
	
	