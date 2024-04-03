from pygame.math import Vector2
from collections import deque

class Snake:
    def __init__(self) -> None:
        self.body = deque([Vector2(i, 10) for i in range(5, 9)])
        self.direction = Vector2(1, 0)


    def head(self) -> Vector2:
        return self.body[-1]


    def nextMove(self) -> Vector2:
        """
        returns the cell he is heading depending on the direction
        """
        return self.head() + self.direction
