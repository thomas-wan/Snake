import pygame as pg
from Snake import Snake
from GameParameters import CELL_SIZE

class SnakeRenderer:
    def __init__(self) -> None:
        pass


    @staticmethod
    def render(screen: pg.Surface, snake: Snake) -> None:
        for block in snake.body:
            x, y = block * CELL_SIZE
            snake_rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(screen, pg.Color("green"), snake_rect)
