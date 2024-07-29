from components.uiElements import Button
import pygame

def getContainers() -> None:
    pass

def getGameButtons() -> list[Button]:
    return [
        Button("Test", 10, 10, 50, 80, pygame.Color(255, 0, 0), 
               "print('Test Pressed')"),
        Button("Other", 10, 100, 50, 80, pygame.Color(255, 0, 0), 
               "print('Other Pressed')"),
    ]