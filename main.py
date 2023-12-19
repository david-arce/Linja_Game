import pygame
import sys

WIDTH = 700
HEIGHT = 480

BLACK = (0, 0, 0)
RED = (255, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("EL JUEGO DE LINJA")

    black_circle_positions = []
    red_circle_positions = []
    coordinates = [[155, 100], [225, 100], [295, 100], [365, 100], [435, 100], [505, 100], [575, 100], [575, 145], [575, 190], [575, 235], [575, 280], [575, 325], [85, 325], [155, 325], [225, 325], [295, 325], [365, 325], [435, 325], [505, 325], [85, 100], [85, 145], [85, 190], [85, 235], [85, 280], [155, 145], [155, 190], [155, 235], [155, 280], [225, 145], [225, 190], [225, 235], [225, 280], [295, 145], [295, 190], [295, 235], [295, 280], [365, 145], [365, 190], [365, 235], [365, 280], [435, 145], [435, 190], [435, 235], [435, 280], [505, 145], [505, 190], [505, 235], [505, 280]]
    
    # Agregar las posiciones de los círculos negros horizontalmente
    for x in range(155, 575 + 1, 70):
        black_circle_positions.append([x, 100])

    # Agregar las posiciones de los círculos negros verticalmente
    for y in range(145, 325 + 1, 45):
        black_circle_positions.append([575, y])

    # Agregar las posiciones de los círculos rojos horizontalmente
    for x in range(85, 505 + 1, 70):
        red_circle_positions.append([x, 325])

    # Agregar las posiciones de los círculos rojos verticalmente
    for y in range(100, 280 + 1, 45):
        red_circle_positions.append([85, y])

    print("positions black: ", black_circle_positions)
    print("positions red: ", red_circle_positions)
    selected_circle = None
    
    while True:
        fondo = pygame.image.load("tablero.png").convert()
        screen.blit(fondo, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("CLIC")
                mouse_pos = pygame.mouse.get_pos()
                if selected_circle is None:
                    for pos in black_circle_positions + red_circle_positions:
                        if pos[0] - 15 < mouse_pos[0] < pos[0] + 15 and pos[1] - 15 < mouse_pos[1] < pos[1] + 15:
                            selected_circle = pos
                            
                      
                else:
                    # Verifica si la nueva posición está ocupada
                    collision = False
                    for item in black_circle_positions + red_circle_positions:
                        if item[0] - 15 < mouse_pos[0] < item[0] + 15 and item[1] - 15 < mouse_pos[1] < item[1] + 15:
                            collision = True
                            break
                    
                    # Si no hay colisión, mueve el círculo
                    if not collision:                    
                        for item in coordinates:
                            if item[0] - 15 < mouse_pos[0] < item[0] + 15 and item[1] - 15 < mouse_pos[1] < item[1] + 15:
                                selected_circle[0], selected_circle[1] = item
                        # selected_circle[0], selected_circle[1] = mouse_pos
                        selected_circle = None
                    
        
        for pos in black_circle_positions:
            pygame.draw.circle(screen, BLACK, pos, 15)
        for pos in red_circle_positions:
            pygame.draw.circle(screen, RED, pos, 15)

        # Controlar la velocidad de actualización
        pygame.time.Clock().tick(60)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
