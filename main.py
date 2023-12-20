import random
import pygame
import sys

WIDTH = 700
HEIGHT = 480

BLACK = (0, 0, 0)
RED = (255, 0, 0)

def mostrar_mensaje(screen, mensaje, posicion):
    color = (255, 255, 255)  # Color blanco
    font = pygame.font.Font(None, 28)
    text = font.render(mensaje, True, color)
    screen.blit(text, posicion)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("EL JUEGO DE LINJA")

    black_circle_positions = []
    red_circle_positions = []
    # black_circle_positions = [[155, 100], [225, 100], [295, 100], [295, 190], [295, 145], [155, 145], [155, 190], [155, 235], [155, 280], [155, 325], [225, 145], [225, 190]]
    # red_circle_positions = [[365, 235], [365, 190], [365, 145], [505, 280], [365, 325], [435, 325], [505, 325], [435, 145], [435, 190], [435, 235], [435, 280], [365, 280]]
    
    coordinates = [[85, 100], [85, 145], [85, 190], [85, 235], [85, 280], [85, 325], [155, 100], [155, 145], [155, 190], [155, 235], [155, 280], [155, 325], [225, 100], [225, 145], [225, 190], [225, 235], [225, 280], [225, 325], [295, 100], [295, 145], [295, 190], [295, 235], [295, 280], [295, 325], [365, 100], [365, 145], [365, 190], [365, 235], [365, 280], [365, 325], [435, 100], [435, 145], [435, 190], [435, 235], [435, 280], [435, 325], [505, 100], [505, 145], [505, 190], [505, 235], [505, 280], [505, 325], [575, 100], [575, 145], [575, 190], [575, 235], [575, 280], [575, 325]]
    
    posicion_utilidad = [[85, 370], [155, 370], [225, 370], [295, 370], [365, 370], [435, 370], [505, 370], [575, 370]]
   
    
    # Convertir a matriz de 8x6
    matrix = [coordinates[i:i + 8] for i in range(0, len(coordinates), 8)]
    
    selected_circle = None
    arr_cant_fichas = [0] * 8 #lista que almacena la cantidad de fichas en cada columna
    # for fila in matrix:
    #     for coordenada in fila:
    #         print(coordenada)
        
    #Agregar las posiciones de los círculos negros horizontalmente
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

    
    def board(black_circle_positions, red_circle_positions, arr_cant_fichas):
        fondo = pygame.image.load("tablero.png").convert()
        screen.blit(fondo, (0, 0))
        
        color_ficha = ""
        
        #pinta los circulos
        for pos in black_circle_positions:
            pygame.draw.circle(screen, BLACK, pos, 15)
        for pos in red_circle_positions:
            pygame.draw.circle(screen, RED, pos, 15)
            
        if selected_circle in black_circle_positions:
            color_ficha = "Negra"
        elif selected_circle in red_circle_positions:
            color_ficha = "Roja"
        else:
            color_ficha = "/"
        # Mensaje ficha seleccionada
        mensaje = "Ficha "+color_ficha+" seleccionada"
        posicion_mensaje = (10, 10)  
        mostrar_mensaje(screen, mensaje, posicion_mensaje)
        
        #mensaje cantidad de fichas en cada columna
        for item in range(8): 
            mensaje = str(arr_cant_fichas[item])
            posicion_mensaje = posicion_utilidad[item]  
            mostrar_mensaje(screen, mensaje, posicion_mensaje)
    
    #verifica si el juego termina
    def termina(black_circle_positions, red_circle_positions, coordinates):
        cant_fichas_negras = 0
        #comprobar si termina el juego
        for i in range(8):
            for item in coordinates[i * 6: (i + 1) * 6]:
                if item in black_circle_positions:
                    cant_fichas_negras += 1
                elif item in red_circle_positions:
                    cant_fichas_negras = 0
            if cant_fichas_negras == 12:
                return True
            else:
                return False
        
    def suma_columna(black_circle_positions, red_circle_positions, arr_cant_fichas):
        #contar y sumar la cantidad de fichas en cada columna
        for i in range(8):
            cant_fichas = 0
            # print(f"columna{i + 1}")
            for item in coordinates[i * 6: (i + 1) * 6]:
                if item in black_circle_positions:
                    cant_fichas += 1
                elif item in red_circle_positions:
                    cant_fichas += 1
                
            arr_cant_fichas[i] = cant_fichas
        return arr_cant_fichas    
    
    turno_maquina = False
    while True:
        print("turno humano")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                print("CLIC")
                mouse_pos = pygame.mouse.get_pos()
                if selected_circle is None:
                    for pos in red_circle_positions:
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
                                turno_maquina = True
                        # selected_circle[0], selected_circle[1] = mouse_pos
                        selected_circle = None
    
        if turno_maquina:
            print("turno maquina")
            
            ficha_negra_aleatoria = random.choice(black_circle_positions)
            coordenada_aleatoria = random.choice(coordinates)
            if coordenada_aleatoria not in black_circle_positions + red_circle_positions:
                ficha_negra_aleatoria[0], ficha_negra_aleatoria[1] = coordenada_aleatoria
                turno_maquina = False
                
            
        cant_fichas = suma_columna(black_circle_positions, red_circle_positions, arr_cant_fichas)
        
        termina(black_circle_positions, red_circle_positions, coordinates)
        
        board(black_circle_positions, red_circle_positions, cant_fichas)

        # Controlar la velocidad de actualización
        pygame.time.Clock().tick(20)
        
        #actualiza
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()
