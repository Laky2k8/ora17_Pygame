import pygame
import math
import operator

import sys
import random

pygame.init()

player = pygame.image.load("player.png")

bg = pygame.image.load("bg.png")
arm = pygame.image.load("arm.png")
arm2 = pygame.image.load("arm.png")


x = 450
y = 200

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

#player = pygame.transform.scale(player, (200,200))

screen = pygame.display.set_mode([1000,500])
pygame.display.set_caption("PyGame 17. Class")

movingUp = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill('white')
        screen.blit(bg, (0, 0))

        pRect = player.get_rect()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= 10
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= 10
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 10
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 10

        correction_angle = 110

        arm1_pRect = player.get_rect(topleft=(x + 120, y + 70))
        arm2_pRect = player.get_rect(topleft=(x + 20, y + 70))

        arm1Pos = arm1_pRect.topleft
        arm2Pos = arm2_pRect.topleft

        arm1Rect = arm.get_rect(center= arm1Pos)
        arm2Rect = arm.get_rect(center=arm2Pos)

        mx, my = pygame.mouse.get_pos()
        dx1, dy1 = mx - arm1Rect.centerx, my - arm1Rect.centery
        dx2, dy2 = mx - arm2Rect.centerx, my - arm2Rect.centery
        angle1 = math.degrees(math.atan2(-dy1, dx1)) - correction_angle
        angle2 = math.degrees(math.atan2(-dy2, dx2)) - correction_angle

        newAngle = clamp(angle1, 0, 360) / 2
        newAngle2 = clamp(angle2, 0, 360) / 2
        armRot1 = pygame.transform.rotate(arm, angle1)
        armRot2 = pygame.transform.rotate(arm2, angle2)
        armRotRect1 = armRot1.get_rect(center=arm1Rect.topleft)
        armRotRect2 = armRot2.get_rect(center=arm2Rect.topleft)

        screen.blit(player, (x, y))
        screen.blit(armRot1,  armRotRect1.topleft)
        screen.blit(armRot2, armRotRect2.topleft)


        pygame.display.flip()

pygame.quit()