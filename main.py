import pygame
import math
from constants import *
from kinematic import ForwardKinematic

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
fps = 60

angle = 0

FK = ForwardKinematic([Width//2, Height//2])

FK.Append(200)
FK.Append(150)
FK.Append(100)

# FK.RotateArm(0, 1.3)
# FK.RotateArm(1, -1.5)
# FK.RotateArm(2, 0.98)

run = True
while run:
    clock.tick(fps)
    screen.fill(White)
    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False

    FK.RotateArm(0, math.sin(angle) * 1.3)
    FK.RotateArm(1, math.sin(angle * 1.2) * -0.9)
    FK.RotateArm(2, math.sin(angle * 0.73) * 1.12)

    angle += 0.05

    FK.update()
    FK.Show(screen)

    pygame.display.flip()


pygame.quit()
