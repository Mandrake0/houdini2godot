extends MeshInstance

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pass

func _process(delta):
	# Called every frame. Delta is time since last frame.
	# Update game logic here.
	
	if Input.is_action_pressed("ui_left"):
		translate(Vector3(-0.1, 0, 0))
	
	if Input.is_action_pressed("ui_right"):
		translate(Vector3(0.1, 0, 0))
		
	if Input.is_action_pressed("ui_up"):
		translate(Vector3(0, 0 , -0.1))
	
	if Input.is_action_pressed("ui_down"):
		translate(Vector3(0, 0, 0.1))
	
	if Input.is_action_pressed("ui_cancel"):
		get_tree().quit()
	
	
	pass
