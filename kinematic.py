import pygame
from constants import *
from Arm import Arm

class Kinematic:
    def __init__(self, FK=None, IK=None):
        self.FK = FK
        self.IK = IK
        # 0 -> Inverse Kinematic , 1 -> Forward Kinematic
        self.SelectedMode = 0

    def AppendArm(self, length):
        self.FK.Append(length)
        self.IK.Append(length)


class ForwardKinematic:
    def __init__(self, position, arms=[], lastArm=None):
        self.position = position
        self.arms = arms
        self.lastArm = lastArm


    def Append(self, length):
        arm = Arm([0, 0], length, 0)
        arm.MODE = 1
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

    def Show(self, screen, ShowCircle):
        for i, arm in enumerate(self.arms):
            arm.Show(screen, ShowCircle)

class InverseKinematic:
    def __init__(self, position, arms=[], lastArm=None):
        self.position = position
        self.arms = arms
        self.lastArm = lastArm

    def Append(self, length):
        arm = Arm([0,0], length, 0)
        if self.lastArm != None:
            arm.position = self.lastArm.getPosition()
            arm.parent = self.lastArm
        else:
            arm.position = self.position
        self.arms.append(arm)
        self.lastArm = arm

    def Drag(self, target):
        self.lastArm.drag(target)

    def Show(self, screen, ShowCircle):
        for arm in self.arms:
            arm.Show(screen, ShowCircle)
