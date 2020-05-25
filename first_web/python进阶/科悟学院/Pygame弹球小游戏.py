import pygame
import random
pygame.init()  # 初始化

screen = pygame.display.set_mode((800,600))  # 创建窗口并设置大小

pygame.display.set_caption('一个弹球小游戏') # 设置标题

# 游戏的本质 死循环

ball_y = 100
ball_x = 400
clock = pygame.time.Clock()
FPS = 60 # 每秒显示图像帧数

ban = pygame.Rect(0,0,100,20) # 矩形

ban.centerx = 400
ban.centery = 400

v0 =0
v1 =0
G = 9.8 * 100  # 自己调整  加速度
t = 1/ FPS # 时间t

# 准备两个变量判断左右是否被按下
left = False
right = False

while 1:
    # 清空屏幕
    screen.fill((0,0,0))
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:   # 如果点击x号，退出。
            print("游戏正常退出")
            exit(0)
        if e.type ==pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left == True
            if e.key == pygame.K_RIGHT:
                right ==True
        if e.type ==  pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left == False
            if e.key == pygame.K_RIGHT:
                right == False



    if left:
        ban.centerx -= 20
    if right:
        ban.centerx += 20



    pygame.draw.rect(screen,(190,120,47),ban)

    # 计算位移距离
    s = v0 * t + (G *(t**2))/2

    v0 = v0 +G * t
    ball_y += s  # 加上次距离

    ball = pygame.draw.circle(screen,(187,14,128),(int(ball_x),int(ball_y)),10)  #屏幕，颜色，位置，半径

    if ban.colliderect(ball):
        v0 = -v0
        v1 = random.randint(-5,5)
    ball_x += v1
    if ball_x < 0 or ball_x >800:
        v1 = -v1

    if ball_y > 450:
        print('游戏结束')
        exit()
    # 匀加速直线运动 - 自由落体


    clock.tick(FPS)     # 设置时钟

    pygame.display.update() # 更新界面


