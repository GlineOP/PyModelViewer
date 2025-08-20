# Main file for 3D model viewer
import pygame
import sys
from model_loader import load_model
from renderer import render_model
from camera import Camera

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("3D Model Viewer")
    clock = pygame.time.Clock()
    
    # Load model
    model_data = load_model("models/cube.obj")
    if not model_data:
        print("No model loaded")
        return
    
    camera = Camera()
    color_mode = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    color_mode = not color_mode
                    if color_mode:
                        print("Switched to wireframe mode")
                    else:
                        print("Switched to blue mode")
            
            camera.handle_event(event)
        
        screen.fill((0, 0, 0))
        camera.update()
        render_model(screen, model_data, camera, color_mode)
        font = pygame.font.SysFont(None, 24)
        mode_text = "Mode: BLUE (SPACE to change)" if not color_mode else "Mode: WIREFRAME (SPACE to change)"
        text_surface = font.render(mode_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()