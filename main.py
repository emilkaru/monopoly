import json
import random

import pygame
from typing import List
from board_tile import Tile
from dice import Die
from player import Player


class Main(object):
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1400, 800))

        with open('board_tiles.json', encoding='utf-8') as file:
            self.board_tile_info = json.loads(file.read())

        self.tiles = self.mk_board_tiles()
        self.die = Die((1200, 500), self.display)
        self.players = self.mk_players(10)

        self.player_number = 0
        self.player_numbers = [
            pygame.font.SysFont(
                'Consolas', 24, True
            ).render(
                f'player {i}', True, (0, 0, 0)
            ) for i in range(len(self.players))
        ]

        self.clock = pygame.time.Clock()

    def mk_board_tiles(self) -> List[Tile]:
        return [
            Tile(
                (10 + x * 110, 10 + y * 210),
                self.display,
                pygame.image.load(self.board_tile_info[y][x]["image"]),
                self.board_tile_info[y][x]["top colour"],
                self.board_tile_info[y][x]["price"]
                # x is the number of tiles in a row
                # y is the number of rows
            ) for x in range(10) for y in range(3)
        ]

    def mk_players(self, player_amount: int) -> List[Player]:
        return [
            Player(
                self.display,
                self.mk_player_image(f'P{i}'),
                self.die
            ) for i in range(player_amount)
        ]

    @staticmethod
    def mk_player_image(player_name: str) -> pygame.Surface:
        surface = pygame.surface.Surface((30, 30))
        surface.set_alpha(200)
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        surface.fill((r, g, b))

        pygame.draw.lines(surface, (0, 0, 0), True, ((0, 0), (28, 0), (28, 28), (0, 28)), 2)

        font = pygame.font.SysFont('Consolas', 24, True)
        surface.blit(font.render(player_name, True, (225, 225, 225) if r + g + b < 300 else (0, 0, 0)), (2, 0))
        return surface

    def main(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.players[self.player_number].move(self.die.roll_die())
                    self.player_number = (self.player_number + 1) % 9

            self.display.fill((230, 230, 230))

            [i.draw() for i in self.tiles]  # draw board tiles
            [i.draw() for i in self.players]  # draw players
            self.die.draw_die()
            self.display.blit(self.player_numbers[self.player_number], (1250, 10))

            pygame.display.flip()

            # IDK how to get the actual FPS/refresh rate on a monitor, so I use the FPS/refresh rate of my primary
            # monitor for the FPS of the game. You can change the FPS by lowering or increasing the number
            # (decreasing the FPS to 60 or even 30 FPS could make the game smoother on lower end hardware)
            self.clock.tick(10)


if __name__ == "__main__":
    main = Main()
    main.main()
