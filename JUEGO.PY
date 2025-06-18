import pygame
import pygame.mixer as mixer 

pygame.init()
mixer.init()
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

imagen_rectangulo = pygame.surface.Surface((100,100))
imagen_rectangulo.fill((128,128,0))
rectangulo = imagen_rectangulo.get_rect()

mixer.music.load("musica.wav")
mixer.music.set_volume(0)
esta_reproduciendo = False
clock = pygame.time.Clock()


logo_pygame = pygame.image.load("01.png")

color_circulo = (255,0,0)
coordenadas_centro = (200,150)
radio = 50

color_rectangulo = (0,128,0)
coordenadas_x = 500
coordenadas_y = 300
ancho = 175
alto = 200

pygame.display.set_caption("Este es mi juego")
flag_correr = True
while flag_correr:
    clock.tick(60)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    pantalla.fill((0,0,128))
    
    pygame.draw.circle(pantalla,color_circulo,coordenadas_centro,radio)
    pygame.draw.rect(pantalla, color_rectangulo, (coordenadas_x,coordenadas_y,ancho, alto), width=15, border_radius=50, )
    
    pantalla.blit(logo_pygame, (275, 290))
    rectangulo.y += 10
    if rectangulo.top > ALTO_VENTANA:
        rectangulo.bottom = 0
    
    if not esta_reproduciendo:
        mixer.music.play()
        esta_reproduciendo = True
    pantalla.blit(imagen_rectangulo, rectangulo)
    pygame.display.flip()
