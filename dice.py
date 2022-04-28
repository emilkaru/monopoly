import pygame
from typing import Union
import random


class Die(object):
    def __init__(self, pos: tuple[int, int], display: Union[pygame.Surface, pygame.SurfaceType]) -> None:
        """
        :param pos: the position of the die (from the top, left corner)
        :param display: the Surface to draw the die on
        """
        self.display = display  # the surface to draw the die on
        x, y = pos
        self.position = (x - 3, y - 3)
        self._mk_die(random.randint(1, 6))

    def draw_die(self) -> None:
        self.display.blit(self.surface, self.position)

    def roll_die(self) -> None:
        self._mk_die(random.randint(1, 6))

    def _mk_die(self, number):
        # the number surface
        font = pygame.font.SysFont('Consolas', 45)
        rendered_txt = font.render(str(number), True, (0, 0, 0))

        # make the surface
        self.surface = pygame.surface.Surface((60, 60), flags=pygame.SRCALPHA)  # the surface for the die
        self.surface.fill((0, 0, 0, 0))  # makes the surface transparent

        # make stuff appear on the surface
        # TODO: make 6 pictures for the numbers on the dice
        pygame.draw.lines(self.surface, (0, 0, 0), True, [(3, 3), (53, 3), (53, 53), (3, 53)], 5)  # die outline
        self.surface.blit(rendered_txt, (30 - rendered_txt.get_width() / 2, 30 - rendered_txt.get_height() / 2))

