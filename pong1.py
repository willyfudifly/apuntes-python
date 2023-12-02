# Pong_1.py: Ventana del juego

import pygame
from pygame.locals import *

# Constantes para la inicialización de la superfície de dibujo
VENTANA_HORI = 800 # Ancho de la ventana
VENTANA_VERT = 600 # Alto de la ventana
FPS = 60 # Fotograma por segundo
BLANCO = (255, 255, 255) # Color del fondo de la ventana (RGB)

def main():
    # Inicialización de Pygame
    pygame.init()

    # Incialización de la superfície de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 1")

    # Bucle principal
    jugando = True
    while jugando:
        ventana.fill(BLANCO)

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False
        
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()