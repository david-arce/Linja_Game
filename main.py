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
    
    coordinates = [[85, 100], [155, 100], [225, 100], [295, 100], [365, 100], [435, 100], [505, 100], [575,100], [85, 145], [155, 145], [225, 145], [295, 145], [365, 145], [435, 145], [505, 145], [575, 145], [85, 190], [155, 190], [225, 190], [295, 190], [365, 190], [435, 190], [505, 190], [575, 190], [85, 235], [155, 235], [225, 235], [295, 235], [365, 235], [435, 235], [505, 235], [575, 235], [85, 280], [155, 280], [225, 280], [295, 280], [365, 280], [435, 280], [505, 280], [575, 280],[85, 325], [155, 325], [225, 325], [295, 325], [365, 325], [435, 325], [505, 325], [575, 325]]
    
    posicion_utilidad = [[85, 370], [155, 370], [225, 370], [295, 370], [365, 370], [435, 370], [505, 370], [575, 370]]
   
    
    # Convertir a matriz de 8x6 las coordenadas permitidas
    matrix = [coordinates[i:i + 8] for i in range(0, len(coordinates), 8)]
    selected_circle = None
    # num_filas = len(matrix)
    # num_columnas = len(matrix[0]) if num_filas > 0 else 0
    # for col_index in range(num_columnas):
    #     for fila_index in range(num_filas):
    #         item = matrix[fila_index][col_index]
    #         print(item)
    
    # print(matrix)
    
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
    def termina(black_circle_positions, red_circle_positions):
        cant_fichas_negras = 0
        #comprobar si termina el juego
        num_filas = len(matrix)
        num_columnas = len(matrix[0]) if num_filas > 0 else 0
        
        for col_index in range(num_columnas):
            for fila_index in range(num_filas):
                item = matrix[fila_index][col_index]
                if item in black_circle_positions:
                    cant_fichas_negras += 1
                elif item in red_circle_positions:
                    cant_fichas_negras = 0
            if cant_fichas_negras == 12:
                return True
        if cant_fichas_negras != 12:
            return False
        
    def suma_columna(black_circle_positions, red_circle_positions):
        arr_cant_fichas = [0] * 8 #lista que almacena la cantidad de fichas en cada columna
        #contar y sumar la cantidad de fichas en cada columna
        num_filas = len(matrix)
        num_columnas = len(matrix[0]) if num_filas > 0 else 0
        
        # Recorrer la matriz por columnas
        for col_index in range(num_columnas):
            cant_fichas = 0
            for fila_index in range(num_filas):
                item = matrix[fila_index][col_index]
                if item in black_circle_positions:
                    cant_fichas += 1
                elif item in red_circle_positions:
                    cant_fichas += 1
                
            arr_cant_fichas[col_index] = cant_fichas
        return arr_cant_fichas    
    
    turno_maquina = False
    while True:
        
        # print("turno humano")
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
                        # index = 0                    
                        for fila in matrix:
                            index = 0
                            for item in fila:
                                if item[0] - 15 < mouse_pos[0] < item[0] + 15 and item[1] - 15 < mouse_pos[1] < item[1] + 15:
                                    selected_circle[0], selected_circle[1] = item
                                    cant_movimientos = suma_columna(black_circle_positions, red_circle_positions)
                                    turno = cant_movimientos[index] - 1
                                    
                                    turno_maquina = True
                                 
                                index += 1
                            # selected_circle[0], selected_circle[1] = mouse_pos
                        selected_circle = None

                    # print(turno)
            
    
        if turno_maquina:
            # print("turno maquina")
            ficha_negra_aleatoria = random.choice(black_circle_positions)
            coordenada_aleatoria = random.choice(coordinates)
            if coordenada_aleatoria not in black_circle_positions + red_circle_positions:
                ficha_negra_aleatoria[0], ficha_negra_aleatoria[1] = coordenada_aleatoria
                turno_maquina = False
                
            
        cant_fichas = suma_columna(black_circle_positions, red_circle_positions)
        
        termina(black_circle_positions, red_circle_positions)
        
        board(black_circle_positions, red_circle_positions, cant_fichas)

        # Controlar la velocidad de actualización
        pygame.time.Clock().tick(20)
        
        #actualiza
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()
