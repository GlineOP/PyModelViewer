Run the program:
python main.py(needed for use: python, pygame)

Controls:
LMB + mouse movement - camera rotation
Mouse wheel - zoom in/out
Space - switch display modes
ESC - exit the program

Display modes:
Blue mode (default) - the model is filled with blue
Wire mode - the models wireframe with points is displayed

Supported formats:
Only OBJ files with triangular polygons
Vertices (v) and faces (f) are supported
Textures and normals are ignored

How to add your model:
Put the OBJ file in the models/ folder
Change the path in main.py to your model:
model_data = load_model("models/your_model.obj")

Limitations:
Only simple OBJ files
No support for materials and textures
Basic 3D projection without lighting
Only triangular polygons

License:
MIT
