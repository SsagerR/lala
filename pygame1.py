#pygame.init()
#pygame.quit()
import pygame
import sys 
pygame.init()
# hero_rect = pygame.Rect(100, 100, 100, 100)
# print("the origin of the hero: %d %d" % (hero_rect.x, hero_rect.y))
# print("the size of the hero: %d %d" % (hero_rect.width, hero_rect.height))
# print("the size of the herp: %d" % (hero_rect.size[0] * hero_rect.size[1]))
#size returns a tuple (width, height)
#pygame.display.set_mode()初始化游戏显示窗口
#pygame.display.update()刷新屏幕内容显示
#set_mode(resolution = (0, 0), flags = 0, depth = 0)
#resolution指定屏幕的宽和高，默认创建的窗口大小和屏幕大小一致
#flags窗口指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
#depth参数表示颜色的位数，默认自动匹配
pygame.display.set_mode((600, 700))
while True:
    pass
pygame.quit()#卸载游戏内存