import pygame

pygame.init()

ancho = 800
alto = 600
pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Juego")

encendido = True

while encendido:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            encendido = False

    pantalla.fill((0,0,0))

    pygame.display.flip()

pygame.quit()