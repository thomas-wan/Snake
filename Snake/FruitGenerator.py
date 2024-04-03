from Snake import Snake
from Fruit import Fruit
from Board import Board

class FruitGenerator:
    def generateFruit(board: Board, snake: Snake) -> None:
        while not board.fruits:  # one fruit in the board (for now)
            fruit = Fruit.random(board.width-1, board.length-1)
            if fruit not in snake.body:
                board.fruits.append(fruit)
            else:
                continue

