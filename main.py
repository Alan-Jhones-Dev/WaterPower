import pygame

pygame.init()

pygame.display.set_mode(size=(600, 500))

while True:
    pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Window
            quit()
