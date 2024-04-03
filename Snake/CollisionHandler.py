from Snake import Snake
from Board import Board

class CollisionHandler:
    def __init__(self) -> None:
        pass


    def __inBounds(board: Board, snake: Snake) -> bool:
        return 0 <= snake.head().x < board.width and 0 <= snake.head().y < board.length


    def __eatsTail(snake: Snake) -> bool:
        return snake.nextMove() in snake.body


    @staticmethod
    def isDead(board: Board, snake: Snake) -> bool:
        return not CollisionHandler.__inBounds(board, snake) or CollisionHandler.__eatsTail(snake)
