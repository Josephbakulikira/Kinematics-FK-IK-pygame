import math
import pygame
from constants import Black

class Arm:
    def __init__(self, position, length, angle):
        self.position = position
        self.length = length
        self.angle = angle
        self.color = Black
        self.ArmStroke = 7
        self.parent = None
        self.child = None

    def getPosition(self):
        angle = self.angle
        parent = self.parent

        while parent != None:
            angle += parent.angle
            parent = parent.parent

        return [self.position[0] + math.cos(angle) * self.length,
                self.position[1] + math.sin(angle) * self.length]

    def Show(self, screen):
        pygame.draw.line(screen, self.color, self.position, self.getPosition(), self.ArmStroke)
        pygame.draw.circle(screen, (255, 205, 25), self.position, 10)
