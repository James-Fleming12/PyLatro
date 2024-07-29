import pygame
from gameElements import Joker, TarotCard

class Button:
    def __init__(self, name: str, 
                 x: float, 
                 y: float, 
                 height: float, 
                 width: float, 
                 color: pygame.Color, 
                 command: str):
        self.name = name
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.c = color
        self.pressed = False
        self.command = command

    def __str__(self) -> str:
        return f"{self.name} ({self.x}, {self.y})"

    def getRender(self) -> pygame.Rect:
        if self.pressed:
            return pygame.Rect(self.x, self.y + (self.h / 5) - 5, self.w, self.h)
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    def getShadow(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y + self.h, self.w, self.h / 5)
    
    def getColor(self) -> pygame.Color:
        if self.pressed:
            temp = self.c
            return (0, 0, 0) # how darken the color????
        return self.c
    
    def press(self) -> None:
        self.pressed = True
    def unpress(self) -> None:
        self.pressed = False

    def isHovered(self, pos: tuple[int, int]) -> bool:
        return pos[0] > self.x and pos[1] > self.y and pos[0] < self.x+self.w and pos[1] < self.y+self.h

class Container: # for jokers or tarot cards
    
    def __init__(self, x: float, y: float, w: float, h: float, type: str, amount: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = type
        self.amount = amount
        self.items = []
    
    def add() -> None:
        pass

    def sell() -> None:
        pass

class InfoBox: # hands, money, discards, ante, rount

    def __init__(self, x: float, y: float, w: float, h: float, message: str = ""):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.message = message

    def getInner(self) -> pygame.Rect:
        if len(self.message) == 0:
            return pygame.Rect(self.x+10, self.y+10, self.w-20, self.h-20)
        return pygame.Rect(self.x+40, self.y+10, self.w-20, self.h-20)

    def getOutline(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.w, self.h)