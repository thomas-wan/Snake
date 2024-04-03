from __future__ import annotations
from pygame.math import Vector2
from random import randint

class Fruit:
    def __init__(self, x: int, y: int) -> None:
        self.position = Vector2(x, y)


    @staticmethod
    def random(boundX, boundY) -> Fruit:
        return Fruit(randint(0, boundX), randint(0, boundY))
