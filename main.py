import json
import pygame
from board_tile import Tile
from dice import Die


class Main(object):
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1500, 1000))
        with open('board_tiles.json', encoding='utf-8') as file:
            self.board_tile_info = json.loads(file.read())
        self.tiles = self.mk_board_tiles()
        self.clock = pygame.time.Clock()

    def mk_board_tiles(self) -> list[Tile]:
        return [
            Tile(
                (10 + x * 110, 10 + y * 210),
                self.display,
                pygame.image.load(self.board_tile_info[y][x]["image"]),
                self.board_tile_info[y][x]["top colour"],
                self.board_tile_info[y][x]["price"]
                # x is the number of tiles in a row
                # y is the number of rows
            ) for x in range(10) for y in range(1)
        ]

    def draw_board_tiles(self) -> None:
        [i.draw_board_tile() for i in self.tiles]

    def main(self):
        die = Die((1200, 500), self.display)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    die.roll_die()

            self.display.fill((230, 230, 230))
            self.draw_board_tiles()
            die.draw_die()
            pygame.display.flip()

            # IDK how to get the actual FPS/refresh rate on a monitor, so I use the FPS/refresh rate of my primary
            # monitor for the FPS of the game. You can change the FPS by lowering or increasing the number
            # (decreasing the FPS to 60 or even 30 FPS could make the game smoother on lower end hardware)
            self.clock.tick(144)


if __name__ == "__main__":
    main = Main()
    main.main()
