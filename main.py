import pygame
import math
from constants import *
from kinematic import ForwardKinematic, InverseKinematic, Kinematic
from Arm import Arm
import random

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
fps = 60

angle = 0

K = Kinematic(ForwardKinematic([Width//2, Height//2]), InverseKinematic([Width//2, Height//2]))
n = 15
for i in range(n):
    K.IK.Append(20)
for i in range(4):
    K.FK.Append(80)

for i in range(4):
    K.FK.RotateArm(i, random.uniform(-2, 2))


toggleMode = 0
ShowCircle = False
moveMouse = True
run = True
while run:
    clock.tick(fps)
    screen.fill(White)
    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                moveMouse = not moveMouse
            if event.key == pygame.K_e:
                toggleMode = (toggleMode + 1) % 2
            if event.key == pygame.K_q:
                ShowCircle = not ShowCircle
        if event.type == pygame.MOUSEMOTION:
            if moveMouse == True:
                mousePosition = pygame.mouse.get_pos()
                if toggleMode == 0:
                    K.IK.Drag(mousePosition)

    if toggleMode == 1:
        K.FK.RotateArm(0, math.sin(angle ) * 1.3  )
        K.FK.RotateArm(1, math.sin(angle * 1.2) * -0.9)
        K.FK.RotateArm(2, math.sin(angle * 0.73) * 1.12)
        K.FK.RotateArm(3, math.sin(angle * 0.23) * -8.12)

        angle += 0.05

        K.FK.update()
        K.FK.Show(screen, ShowCircle)
    else:
        K.IK.Show(screen, ShowCircle)
    pygame.display.flip()


pygame.quit()
