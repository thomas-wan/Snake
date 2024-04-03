import pygame as pg
from sys import exit

from Board import Board
from Snake import Snake
from BoardRenderer import BoardRenderer
from SnakeRenderer import SnakeRenderer
from FruitRenderer import FruitRenderer
from CollisionHandler import CollisionHandler
from GameParameters import *
from SnakeController import SnakeController
from FruitGenerator import FruitGenerator
from SnakeBoardInteraction import SnakeBoardInteraction

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("Snake")
    clock = pg.time.Clock()
    SCREEN_UPDATE = pg.USEREVENT
    pg.time.set_timer(SCREEN_UPDATE, 125)

    board = Board()
    snake = Snake()
    screen = pg.display.set_mode((board.width * CELL_SIZE, board.length * CELL_SIZE))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == SCREEN_UPDATE:
                if CollisionHandler.isDead(board, snake):
                    pg.quit()
                    exit()
                SnakeBoardInteraction.moveSnake(board, snake)
                FruitGenerator.generateFruit(board, snake)
            if event.type == pg.KEYDOWN:
                SnakeController.updateDirection(snake, event)


        BoardRenderer.render(screen)
        SnakeRenderer.render(screen, snake)
        FruitRenderer.render(screen, board.fruits)
        pg.display.update()
        clock.tick(FPS)