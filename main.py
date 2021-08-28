import pygame
import math
from constants import *
from kinematic import ForwardKinematic, InverseKinematic, Kinematic
from Arm import Arm

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
fps = 60

angle = 0

K = Kinematic(ForwardKinematic([Width//2, Height//2]), InverseKinematic([Width//2, Height//2]))
K.AppendArm(100)
K.AppendArm(100)
K.AppendArm(100)


K.FK.RotateArm(0, 1.3)
K.FK.RotateArm(1, -1.5)
K.FK.RotateArm(2, 0.98)


toggleMode = 0

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

        if event.type == pygame.MOUSEMOTION:
            if moveMouse == True:
                mousePosition = pygame.mouse.get_pos()
                if toggleMode == 0:
                    K.IK.Drag(mousePosition)

    if toggleMode == 1:
        K.FK.RotateArm(0, math.sin(angle) * 1.3)
        K.FK.RotateArm(1, math.sin(angle * 1.2) * -0.9)
        K.FK.RotateArm(2, math.sin(angle * 0.73) * 1.12)

        angle += 0.05

        K.FK.update()
        K.FK.Show(screen)
    else:
        K.IK.Show(screen)
    pygame.display.flip()


pygame.quit()
