import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
win_size = (800, 600)
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Pygame Window")

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 在窗口上绘制内容（此处为示例，可以根据需要进行修改）
    screen.fill((255, 255, 255))  # 白色背景
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)  # 红色圆形

    # 更新窗口
    pygame.display.update()

