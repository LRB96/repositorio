# 1 Modulos pygame, sys, random (no tener un archivo llamado random, porque sino no funciona)

#Establecer constantes para los enemigos y el jugador (ANCHO, ALTO, color_rojo, color_negro. color_azul, jugador_size,enemigo_size, jugador_pos, enemigo_pos)

#Crear ventana

#Variable game_over y reloj para los frames

#Funcion para detectar colisisones con parametros y condiciones que verifiquen primero en eje X, luego en eje Y, y retornen True

#Ciclo while sobre el cual corre el juego

#Dentro del ciclo while primero un ciclo for para que la ventana no se cierre, y se detecten los movimientos del jugador

#A la altura del for el resto asfdbasdfidsfhg 



#Agregar un diccionario para maneajr facilmente los enemigos.

#Modulos
import pygame
import sys 
import random


# Constantes
ANCHO= 800
ALTO= 600
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)


#Jugador
jugador_size = [50,50]
jugador_pos = [ANCHO / 2, ALTO - jugador_size[0] * 2]


#enemigo(s)
enemigo_size = [50,50]
enemigo_pos = [random.randint(0, ANCHO - enemigo_size[0]), 0]

enemigo_size2 = [50,50]
enemigo_pos2 = [random.randint(0, ANCHO - enemigo_size[0]), 0]

enemigo_size3 = [50,50]
enemigo_pos3 = [random.randint(0, ANCHO - enemigo_size[0]), 0]

enemigo_size4 = [50,50]
enemigo_pos4 = [random.randint(0, ANCHO - enemigo_size[0]), 0]

#Crear ventana
ventana = pygame.display.set_mode((ANCHO,ALTO))

#Bucle para el juego no se cierre automáticamente
#Dentro del bucle:
# Primero: 
game_over = False
clock = pygame.time.Clock()
# score = 0


# def draw_text(surface, text, size, x, y):
#     font = pygame.font.SysFont("serif", size)
#     text_surface = font.render(text, True, color_rojo)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x, y)
#     surface.blit(text_surface, text_rect)


def detectar_colisiones(jugador_pos, enemigo_pos, enemigo_pos2, enemigo_pos3, enemigo_pos4):
    jx = jugador_pos[0] 
    jy = jugador_pos[1] 

    ex = enemigo_pos[0] 
    ey = enemigo_pos[1] 

    ex2 = enemigo_pos2[0]   
    ey2 = enemigo_pos2[1]   

    ex3 = enemigo_pos3[0]
    ey3 = enemigo_pos3[1]

    ex4 = enemigo_pos4[0]
    ey4 = enemigo_pos4[1]


    if (ex >= jx and ex <(jx+ jugador_size[0])) or (jx >= ex and jx < (ex + enemigo_size[0])):
           if (ey >= jy and ey <(jy+ jugador_size[1])) or (jy >= ex and jy < (ey + enemigo_size[1])):
                return True 

    if (ex2 >= jx and ex2 <(jx+ jugador_size[0])) or (jx >= ex2 and jx < (ex2 + enemigo_size2[0])):
        if (ey2 >= jy and ey2 <(jy+ jugador_size[1])) or (jy >= ex2 and jy < (ey2 + enemigo_size2[1])):
            return True 

    if (ex3 >= jx and ex3 <(jx+ jugador_size[0])) or (jx >= ex3 and jx < (ex3 + enemigo_size3[0])):
        if (ey3 >= jy and ey3 <(jy+ jugador_size[1])) or (jy >= ex3 and jy < (ey3 + enemigo_size3[1])):
            return True 

    if (ex4 >= jx and ex4 <(jx+ jugador_size[0])) or (jx >= ex4 and jx < (ex4 + enemigo_size4[0])):
        if (ey4 >= jy and ey4 <(jy+ jugador_size[1])) or (jy >= ex4 and jy < (ey4 + enemigo_size4[1])):
            return True 


while not game_over:
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            sys.exit()
        
        # Detectar movimiento del jugador
       
        if event.type == pygame.KEYDOWN:
            x = jugador_pos[0]
            y = jugador_pos[1]
            if event.key == pygame.K_LEFT:
                x -= jugador_size[0]
            if event.key == pygame.K_RIGHT:
                x += jugador_size[0]
            if event.key == pygame.K_UP:
                y -= jugador_size[0]
            if event.key == pygame.K_DOWN:
                y += jugador_size[0]

            jugador_pos[0] = x
            jugador_pos[1] = y
            # score += 10

    ventana.fill(color_negro)

    if enemigo_pos[1] >= 0 and enemigo_pos[1] < ALTO:
        enemigo_pos[1] += 20
        enemigo_pos2[1] += 20
        enemigo_pos3[1] += 20
        enemigo_pos4[1] += 20
    else:
        #Eje X
        enemigo_pos[0] =random.randint(0, ANCHO - enemigo_size[0])
        enemigo_pos2[0] =random.randint(0, ANCHO - enemigo_size2[0])
        enemigo_pos3[0] =random.randint(0, ANCHO - enemigo_size3[0])
        enemigo_pos4[0] =random.randint(0, ANCHO - enemigo_size4[0])
        #Eje Y
        enemigo_pos[1] = 0
        enemigo_pos2[1] = 0
        enemigo_pos3[1] = 0
        enemigo_pos4[1] = 0

    if  detectar_colisiones(jugador_pos, enemigo_pos, enemigo_pos2, enemigo_pos3, enemigo_pos4):
        game_over = True

    
    #Dibujar enemigo
    pygame.draw.rect(ventana, color_azul, (enemigo_pos[0], enemigo_pos[1], enemigo_size[0], enemigo_size[1]))
    pygame.draw.rect(ventana, color_azul, (enemigo_pos2[0], enemigo_pos2[1], enemigo_size2[0], enemigo_size2[1]))
    pygame.draw.rect(ventana, color_azul, (enemigo_pos3[0], enemigo_pos3[1], enemigo_size3[0], enemigo_size3[1]))
    pygame.draw.rect(ventana, color_azul, (enemigo_pos4[0], enemigo_pos4[1], enemigo_size4[0], enemigo_size4[1]))
    #Dibujar jugador
    # Primero donde se pone la figura
    #Segundo el color
    #Tercero Posición en pantalla y el tamaño
    #La posición en panatalla y el tamaño van siemmpre entre parentesis
    pygame.draw.rect(ventana, color_rojo, (jugador_pos[0], jugador_pos[1], jugador_size[0], jugador_size[1]))
    clock.tick(30)

    # draw_text(ventana, str(score), 25, ANCHO // 2, 10)
    pygame.display.update()
