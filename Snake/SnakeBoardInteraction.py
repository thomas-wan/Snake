from Snake import Snake
from Board import Board

class SnakeBoardInteraction:
    @staticmethod
    def __eatsFruit(board: Board, snake: Snake) -> bool:
        for i, fruit in enumerate(board.fruits):
            if fruit.position == snake.head():
                board.fruits.pop(i)
                return True
        return False


    def moveSnake(board: Board, snake: Snake) -> None:
        new_head = snake.body[-1] + snake.direction
        snake.body.append(new_head)
        if not SnakeBoardInteraction.__eatsFruit(board, snake):
            snake.body.popleft()
