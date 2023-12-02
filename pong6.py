# Pong6.py: Controlar raqueta

import pygame
from pygame.locals import *
import random
import os.path

# Constantes para la inicialización de la superfície de dibujo
VENTANA_HORI = 800 # Ancho de la ventana
VENTANA_VERT = 600 # Alto de la ventana
FPS = 60 # Fotograma por segundo
BLANCO = (255, 255, 255) # Color del fondo de la ventana (RGB)

carpeta_juego = os.path.dirname(__file__)

class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la clase ---

        # Imagen de la pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de movimiento de la pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= 0:
            self.reiniciar()
        if self.x + self.ancho >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])

class RaquetaPong:
    def __init__(self):

        self.imagen = pygame.image.load(os.path.join("/Users/Willy/apuntes-python/PONG", "raqueta.png")).convert_alpha()

        # --- Atributos de la clase ---

        # Dimensiones de la raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la raqueta
        self.dir_y = 0

    def mover(self):
            self.y += self.dir_y
            if self.y <= 0:
                self.y = 0
            if self.y + self.alto >= VENTANA_VERT:
                self.y = VENTANA_VERT - self.alto


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superfície de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 6")

    pelota = PelotaPong(os.path.join("/Users/Willy/apuntes-python/PONG", "BOLA.png"))

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False
            
            # Detecta que se ha pulsado una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5
            
            # Detecta que se ha soltado una tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
