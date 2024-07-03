extends Node3D

var time = 0.0

"""
For Setting the custom Values the @export has to be set. 
"""
@export
var random_velocity:float

@export
var random_time:float

@export
var albedo_color:String

func _ready():
	# Get The Material
	var material = $cube2.get_surface_override_material(0)
	# Duplicate otherwise we can't change the Color  
	material = material.duplicate()
	# The Value gets from "0.12|0.34|0.56" to a Array: ["0.12","0.34","0.56"]
	var ac = albedo_color.split("|")
	# Set the new Color
	material.albedo_color = Color(float(ac[0]),float(ac[1]),float(ac[2]))
	# Override the Material
	$cube2.set_surface_override_material(0, material)

func _process(delta):
	position.y += (cos(time * random_time) * random_velocity) * delta # Sine movement
	time += delta
