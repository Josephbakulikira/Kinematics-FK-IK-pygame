import pygame
from constants import *
from Arm import Arm

class ForwardKinematic:
    def __init__(self, position, arms=[], lastArm=None):
        self.position = position
        self.arms = arms
        self.lastArm = lastArm

    def Append(self, length):
        arm = Arm([0, 0], length, 0)
        self.arms.append(arm)

        arm.parent = self.lastArm
        self.lastArm = arm

        self.update()

    def update(self):
        for _arm in self.arms:
            if _arm.parent != None:
                _arm.position = _arm.parent.getPosition()
            else:
                _arm.position = self.position

    def RotateArm(self, index, angle):
        self.arms[index].angle = angle

    def Show(self, screen):
        for i, arm in enumerate(self.arms):
            arm.Show(screen)
