# Simple 3D model renderer using pygame
import pygame
import math

def project_point(point, camera):
    # Simple 3D to 2D projection
    x, y, z = point
    
    # Apply camera rotation
    angle_x = math.radians(camera.rotation_x)
    angle_y = math.radians(camera.rotation_y)
    
    # Rotate around Y axis
    x1 = x * math.cos(angle_y) - z * math.sin(angle_y)
    z1 = x * math.sin(angle_y) + z * math.cos(angle_y)
    
    # Rotate around X axis
    y1 = y * math.cos(angle_x) - z1 * math.sin(angle_x)
    z2 = y * math.sin(angle_x) + z1 * math.cos(angle_x)
    
    # Apply camera distance
    z2 += camera.distance
    
    # Perspective projection
    if z2 > 0:
        scale = 200 / z2
        screen_x = 400 + x1 * scale
        screen_y = 300 - y1 * scale
        return (screen_x, screen_y)
    return None

def render_model(screen, model_data, camera, color_mode):
    vertices = model_data["vertices"]
    faces = model_data["faces"]
    
    for face in faces:
        points = []
        for vertex_index in face:
            if vertex_index < len(vertices):
                point_3d = vertices[vertex_index]
                point_2d = project_point(point_3d, camera)
                if point_2d:
                    points.append(point_2d)
        
        if len(points) >= 3:
            if color_mode:
                pygame.draw.polygon(screen, (100, 100, 200), points, 1)
            else:
                # Solid blue mode
                pygame.draw.polygon(screen, (0, 100, 255), points, 0)
                pygame.draw.polygon(screen, (0, 50, 150), points, 1)
    
    if color_mode:
        for vertex in vertices:
            point_2d = project_point(vertex, camera)
            if point_2d:
                pygame.draw.circle(screen, (255, 255, 255), (int(point_2d[0]), int(point_2d[1])), 2)