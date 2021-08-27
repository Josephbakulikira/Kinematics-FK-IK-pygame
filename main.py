import pygame
import math
from constants import *
from kinematic import ForwardKinematic, InverseKinematic
from Arm import Arm

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
fps = 60

angle = 0

FK = ForwardKinematic([Width//2, Height//2])
FK.Append(100)
FK.Append(100)
FK.Append(100)
FK.RotateArm(0, 1.3)
FK.RotateArm(1, -1.5)
FK.RotateArm(2, 0.98)

IK = InverseKinematic([Width//2, Height//2])
IK.Append(100)
IK.Append(100)
IK.Append(100)

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
        if event.type == pygame.MOUSEMOTION:
            if moveMouse == True:
                mousePosition = pygame.mouse.get_pos()
                IK.Drag(mousePosition)

    FK.RotateArm(0, math.sin(angle) * 1.3)
    FK.RotateArm(1, math.sin(angle * 1.2) * -0.9)
    FK.RotateArm(2, math.sin(angle * 0.73) * 1.12)

    angle += 0.05

    FK.update()
    FK.Show(screen)
    IK.Show(screen)
    pygame.display.flip()


pygame.quit()
