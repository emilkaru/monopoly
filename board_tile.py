import pygame
from typing import Union, Tuple


class Tile(object):
    def __init__(self,
                 pos: Tuple[int, int],
                 display: Union[pygame.Surface, pygame.SurfaceType],
                 image: pygame.Surface,
                 top_box_colour: Tuple[int, int, int] = None,
                 price: int = None,
                 line_colour: Tuple[int, int, int] = (150, 150, 150),
                 ) -> None:
        """
        :param pos: the position of the tile (from the top, left corner)
        :param display: the Surface to draw the tile on
        :param image: the surface with things on it
        :param top_box_colour: the colour of the top box (None by default, because you might have tiles without the top
        box)
        :param price: the price of the property
        :param line_colour: the colour of the lines surrounding the box
        """
        self.display = display  # the surface to draw the tile on
        x, y = pos
        self.position = (x - 3, y - 3)

        self.surface = pygame.surface.Surface((110, 210), flags=pygame.SRCALPHA)  # the surface for the tile
        self.surface.fill((0, 0, 0, 0))  # makes the surface transparent

        # draws the tile on the surface
        if top_box_colour is not None:
            pygame.draw.lines(self.surface, line_colour, True, [(3, 3), (103, 3), (103, 203), (3, 203)], 5)
            pygame.draw.line(self.surface, line_colour, (3, 33), (103, 33), 5)
            self.surface.fill(top_box_colour, ((6, 6), (95, 25)))
            self.surface.blit(image, (5, 5))
        else:
            pygame.draw.lines(self.surface, line_colour, True, [(3, 3), (103, 3), (103, 203), (3, 203)], 5)
            self.surface.blit(image, (5, 5))

        # draws the price of the property
        if price is not None:
            font = pygame.font.SysFont('Arial', 20)
            if str(round(price / 1_000_000, 1))[0] == "0":
                price_number = round(price / 1_000)
            elif str(round(price / 1_000_000, 1))[-1] != "0":
                price_number = float(round(price / 1_000_000, 1))
            else:
                price_number = round(price / 1_000_000)

            price_letter = "M" if price > 999_999 else "k"
            rendered_txt = font.render(f'{price_number}{price_letter}€', True, (0, 0, 0))
            self.surface.blit(rendered_txt, (round(53 - rendered_txt.get_width() / 2), 170))

    def draw(self) -> None:
        # called every frame to draw the surface made in __init__() on the screen
        self.display.blit(self.surface, self.position)

    def get_position_on_board(self) -> Tuple[int, int]:
        return self.position
