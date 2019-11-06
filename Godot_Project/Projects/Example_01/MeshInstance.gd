extends "res://Scripts/MeshInstance.gd"

var delimeter = ","
var csv_file = "test.csv"

var obj_box = preload("res://Mesh/box_object1.obj")


func _ready():
    var file = File.new()
    file.open("res://test.csv", file.READ)
	file.seek(0)
	print file.get_csv_line( delimeter)

    file.close()
    pass