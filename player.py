import random
from typing import Union
import dice
import pygame


class Player(object):
    def __init__(self,
                 display: Union[pygame.Surface, pygame.SurfaceType],
                 image: pygame.Surface,
                 die: dice.Die
                 ) -> None:
        """
        :param display: the Surface to draw the player on
        :param image: the surface with the player "skin"
        """
        self.display = display
        self.image = image
        self.tile_x = 0
        self.tile_y = 0
        self.pos = (
                13 + self.tile_x * 110 + random.randint(0, 70),
                13 + self.tile_y * 210 + random.randint(0, 170)
        )

    def draw(self):
        self.display.blit(self.image, self.pos)

    def move(self, moved_tile: int) -> None:
        tiles_moved = moved_tile + self.tile_x + self.tile_y * 10
        self.tile_x = tiles_moved % 10
        self.tile_y = tiles_moved % 39 // 10
        self.pos = (
            13 + self.tile_x * 110 + random.randint(0, 70),
            13 + self.tile_y * 210 + random.randint(0, 170)
        )
