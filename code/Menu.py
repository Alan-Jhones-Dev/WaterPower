import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COLOR_BLUE, COLOR_SEA_BLUE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('assets/menu/orig.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # pygame.mixer.music.load('assets/musicaMenu.wav')
        # pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Water', COLOR_BLUE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Power', COLOR_SEA_BLUE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 40 * i))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="African", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
