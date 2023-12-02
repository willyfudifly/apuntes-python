import pygame
import random
import os.path
import playsound

#¡¡¡IMPORTANTE!!!
#¡¡¡NECESARIO INSTALAR PIP INSTALL PLAYSOUND PARA QUE TODO FUNCIONE!!!

#configuracion de pantalla
ventana_hori = 800
ventana_vert = 600
FPS = 90
color = (255, 255, 255)
color_puntuacion = (255, 233, 133)
fondo = pygame.image.load("fondo.png")

carpeta_juego = os.path.dirname(__file__)

def musicaGeneral():
    #pone musica para que el juego no este en silencio absoluto
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('musica.mp3'))
    pygame.mixer.Channel(0).set_volume(0.3)
    #pygame.mixer.music.play()

def sonidoRebote():
    #da feedback para dar sentimiento a la funcion Raquetazo
    pygame.mixer.music.load('rebote.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()   

def sonidoCentrar():
    #da feedback para dar sentimiento a la funcion Centrar
    pygame.mixer.music.load('error.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()

class PelotaPong:
  def __init__(self, fichero_imagen):
    #atributos de clase
    
    #pelotafoto
    self.imagen = pygame.image.load(os.path.join(carpeta_juego, "bola.png")).convert_alpha()

    #dimensiones PelotaPong
    self.ancho, self.alto = self.imagen.get_size()

    #posicion incial pelota

    self.x = ventana_hori / 2 - self.ancho / 2 
    self.y = ventana_vert / 2 - self.alto / 2

    #direccion movemint
    self.dir_x = random.choice ([-5, 5])
    self.dir_y = random.choice ([-5, 5])

    #puntuacion
    self.puntuacion = 0
    self.puntuacion_ai = 0


  #centrar bola para sistema de puntos
  def centrar(self):

      self.x = ventana_hori / 2 - self.ancho / 2 
      self.y = ventana_vert / 2 - self.alto / 2

      self.dir_x = -self.dir_x
      self.dir_y = random.choice ([-5, 5])


  #mover la pelota sumamos direccion a posicion
  def mover(self): 
    self.x += self.dir_x
    self.y += self.dir_y

  #funcion para rebotar y respawnear

  def rebotar (self):
    #recentrar la pelota si se "sale" del campo

    if self.x < 29:
      self.puntuacion_ai += 1
      self.centrar()
      sonidoCentrar()  
    if self.x > ventana_hori - 30 - self.alto:
      self.centrar()
      self.puntuacion += 1
      sonidoCentrar()
    #rebotar techo y suelo

    if self.y < 27:
      self.dir_y = -self.dir_y
      sonidoRebote()
    if self.y > ( ventana_vert - 30) - self.ancho:
      self.dir_y = -self.dir_y
      sonidoRebote()
        
class RaquetaPong:
  def __init__(self):

    self.imagen = pygame.image.load(os.path.join(carpeta_juego, "raqueta.png")).convert_alpha()

    #dimensiones raqueta
    self.ancho, self.alto = self.imagen.get_size()

    #posicion raqueta
    self.x = 0 
    self.y = ventana_vert / 2 - self.alto / 2

    #direccion raqueta
    self.dir_y = 0

  #funcion de movimiento de raqueta
  def mover (self):
    self.y += self.dir_y
    if self.y <= 29:
      self.dir_y = 0
    if self.y + self.alto >= ventana_vert - 30:
      self.dir_y = 0

  #ia oponente  
  def mover_ai (self, pelota):
    if self.y > pelota.y:
      self.dir_y = -3
    elif self.y < pelota.y:
      self.dir_y = 3
    else:
      self.dir_y = 0
    
    self.y += self.dir_y

  #introduce rebote en la raqueta
  def raquetazo(self, pelota):
    if (
      pelota.x < self.x + self.ancho
      and pelota.x > self.x
      and pelota.alto + pelota.y > self.y
      and pelota.y < self.y + self.alto 
    ):
      pelota.dir_x = -pelota.dir_x
      pelota.x = self.x + self.ancho
      sonidoRebote()

  #introduce rebote en la raqueta que no controlamos
  def raquetazo_ai(self, pelota):
      if (
        pelota.x + pelota.ancho > self.x
        and pelota.x < self.x + self.ancho
        and pelota.y + pelota.alto > self.y
        and pelota.y < self.y + self.alto 
      ):
        pelota.dir_x = -pelota.dir_x
        pelota.x = self.x - pelota.ancho
        sonidoRebote()
        

#funcino principañl
def main (): 
  musicaGeneral()
  #inicia juego
  pygame.init()

  #da tamaño de ventana
  ventana = pygame.display.set_mode((ventana_hori, ventana_vert))

  #título de ventana
  pygame.display.set_caption("PONG v1.0")

  #fuente letra
  fuente = pygame.font.Font(None,60)

  #pelota variable, es una format
  pelota = PelotaPong ("bola.png")

  #raqueta izq
  raqueta_1 = RaquetaPong()
  raqueta_1.x = 60

  raqueta_2 = RaquetaPong()
  raqueta_2.x = ventana_hori - 60 - raqueta_2.ancho

  #para hacer el while eterno hasta q perdamos
  jugando = True

  while jugando: 
    

    #calcular donde pelota esta
    pelota.mover()
    pelota.rebotar()
    raqueta_1.mover()
    raqueta_2.mover_ai(pelota)
    raqueta_1.raquetazo(pelota)
    raqueta_2.raquetazo_ai(pelota)

    #pintar ventana de color
    ventana.blit (fondo, [0, 0])
    #renderizar pelota y raqueta
    ventana.blit(pelota.imagen, ( pelota.x, pelota.y))

    ventana.blit(raqueta_1.imagen, ( raqueta_1.x, raqueta_1.y))
    ventana.blit(raqueta_2.imagen, ( raqueta_2.x, raqueta_2.y))

    #puntuacion izq
    texto = f"{pelota.puntuacion}"
    letrero = fuente.render(texto, False, color_puntuacion)
    ventana.blit(letrero, ((ventana_hori / 2) / 2 - fuente.size(texto)[0] / 2 , ventana_vert / 9))
    
    #puntuacion der
    texto = f"{pelota.puntuacion_ai}"
    letrero = fuente.render(texto, False, color_puntuacion)
    ventana.blit(letrero, ((ventana_hori / 2) * 1.5 - fuente.size(texto)[0] / 2 , ventana_vert / 9))

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
        jugando = False

      #movimiento de raqueta, mira si hay una tecla pulsada
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          raqueta_1.dir_y = -5
        if event.key == pygame.K_s:
          raqueta_1.dir_y = 5

      #movimiento raqueta comprueba si hay tecla soltaa  
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