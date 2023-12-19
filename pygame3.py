import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1024, 1024))
bg = pygame.image.load("/Users/zhongzhichen/Desktop/pygame/1.jpg")
screen.blit(bg, (0, 0))#background
mc = pygame.image.load("/Users/zhongzhichen/Desktop/pygame/R-C.png")
screen.blit(mc, (-100, -100))#main character
pygame.display.update()

clock = pygame.time.Clock()
#frame 60
#每隔1/60s移动一次所有图像的位置

hero_rect = pygame.Rect(-100, -100, 782, 1000)

while True:#game started

    clock.tick(60)#指定循环体内部代码执行频率
    hero_rect.x += 1
    hero_rect.y += 1
    screen.blit(bg, (0, 0))
    screen.blit(mc, hero_rect)
    pygame.display.update()
    if hero_rect.x >= 1024 or hero_rect.y >= 1024:
        hero_rect.x = -1000
        hero_rect.y = -1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
