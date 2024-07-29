import pygame

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

    def getRender(self) -> pygame.Rect:
        if self.pressed:
            return pygame.Rect(self.x, self.y + (self.h / 5) - 5, self.w, self.h)
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    def getShadow(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y + self.h, self.w, self.h / 5)
    
    def getColor(self) -> pygame.Color:
        if self.pressed:
            temp = self.c
            return (0, 0, 0)
        return self.c
    
    def press(self) -> None:
        self.pressed = True
    def unpress(self) -> None:
        self.pressed = False

    def isHovered(self, pos: tuple[int, int]) -> bool:
        return pos[0] > self.x and pos[1] > self.y and pos[0] < self.x+self.w and pos[1] < self.y+self.h