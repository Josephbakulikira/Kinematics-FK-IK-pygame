import math
import pygame
from constants import Black

class Arm(object):
    def __init__(self, position, length, angle):
        self.position = position
        self.length = length
        self.angle = angle
        self.color = Black
        self.ArmStroke = 7
        self.parent = None
        self.child = None
        # 0 -> Inverse Kinematic , 1 -> ForwardKinematic
        self.MODE = 0
    def getPosition(self):
        angle = self.angle
        if self.MODE == 1:
            parent = self.parent

            while parent != None:
                angle += parent.angle
                parent = parent.parent

        return [self.position[0] + math.cos(angle) * self.length,
                self.position[1] + math.sin(angle) * self.length]

    def pointAt(self, target):
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]
        self.angle = math.atan2(dy, dx)

    def drag(self, target):
        self.pointAt(target)
        self.position[0] = target[0] - math.cos(self.angle) * self.length
        self.position[1] = target[1] - math.sin(self.angle) * self.length
        if self.parent != None:
            self.parent.drag(self.position)

    def Show(self, screen, ShowCircle):
        pygame.draw.line(screen, self.color, self.position, self.getPosition(), self.ArmStroke)
        if ShowCircle:
            pygame.draw.circle(screen, (255, 205, 25), self.position, 10)
