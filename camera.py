import pygame
class Camera:
    def __init__(self):
        self.rotation_x = 0
        self.rotation_y = 0
        self.distance = 5.0
        self.dragging = False
        self.last_mouse_pos = (0, 0)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse
                self.dragging = True
                self.last_mouse_pos = event.pos
            elif event.button == 4:  # Wheel up
                self.distance = max(2.0, self.distance - 0.5)
            elif event.button == 5:  # Wheel down
                self.distance = min(20.0, self.distance + 0.5)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
        
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            dx = event.pos[0] - self.last_mouse_pos[0]
            dy = event.pos[1] - self.last_mouse_pos[1]
            
            self.rotation_y += dx * 0.5
            self.rotation_x += dy * 0.5
            self.rotation_x = max(-90, min(90, self.rotation_x))
            self.last_mouse_pos = event.pos
    
    def update(self):
        pass