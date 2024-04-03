import pygame as pg
from pygame.math import Vector2
from GameParameters import CELL_SIZE

class FruitRenderer:
    def __init__(self) -> None:
        pass

    @staticmethod
    def render(screen: pg.Surface, fruits: list[Vector2]) -> None:
        for fruit in fruits:
            x, y = fruit.position * CELL_SIZE
            fruit_rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(screen, pg.Color("red"), fruit_rect)
