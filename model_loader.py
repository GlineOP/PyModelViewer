#hello!
def load_model(file_path):
    vertices = []
    faces = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split()
                if parts[0] == 'v':
                    if len(parts) >= 4:
                        x = float(parts[1])
                        y = float(parts[2])
                        z = float(parts[3])
                        vertices.append((x, y, z))
                
                elif parts[0] == 'f':
                    face = []
                    for part in parts[1:]:
                        vertex_index = int(part.split('/')[0]) - 1
                        if vertex_index < len(vertices):
                            face.append(vertex_index)
                    if len(face) >= 3:
                        faces.append(face)
        
        print(f"Loaded model: {len(vertices)} vertices, {len(faces)} faces")
        return {"vertices": vertices, "faces": faces}
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None