import pygame, sys
# 引入pygame常量
from pygame.locals import *

white = 255, 255, 255
blue = 0, 0, 200

# 初始化pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((600, 500))

# 要绘制文本，要先创建字体对象， 通过pygame.font将文本输出到图形窗口
myfont = pygame.font.Font(None, 60)

# 绘制平面
textImage = myfont.render("Hello Pygame", True, white)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    # 清除屏幕， 进行绘制， 然后刷新显示
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()
