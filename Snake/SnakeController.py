import pygame as pg
from pygame.math import Vector2
from time import sleep
from Snake import Snake


class SnakeController:
    def __init__(self) -> None:
        pass


    def updateDirection(snake: Snake, event: pg.USEREVENT) -> None:
        if event.key == pg.K_UP and snake.direction.y != 1:
            snake.direction = Vector2(0, -1)
        if event.key == pg.K_DOWN and snake.direction.y != -1:
            snake.direction = Vector2(0, 1)
        if event.key == pg.K_RIGHT and snake.direction.x != -1:
            snake.direction = Vector2(1, 0)
        if event.key == pg.K_LEFT and snake.direction.x != 1:
            snake.direction = Vector2(-1, 0)
