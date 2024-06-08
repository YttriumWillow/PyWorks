import pygame
from pygame.locals import *
import os
import random

print(" " * 20 + "START")
print("-" * 45)
t = os.getcwd()
print("Running Location:", t)
score = 0

class Plane(pygame.sprite.Sprite):
    # 主战飞机初始化
    def __init__(self): # 调用object的init()方法
        super().__init__()
        self.image = pygame.image.load(".\\source\\img\\img_plane.png")   # 创建Surface对象，长宽200, 100(115, 60)
        # self.plane_image = pygame.image.load(".\\source\\img\\img_plane.png")
        # self.image.blit(self.plane_image, (0, 0))    # 图片填充
        # self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()   # 得到对象的矩形（飞行）
        self.rect.x = 100    # x坐标为100
        self.rect.y = 500    # y坐标为0
        self.speed = 5   # 速度为5
        self.lives = 10   # 生命为5
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullet_sprites.add(bullet)
        shoot_sound.play()

    def update(self):
        # self.rect.y += self.speed
        keys = pygame.key.get_pressed()

        # wasd和←↓↑→
        if keys[K_a] or keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_d] or keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_w] or keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_s] or keys[K_DOWN]:
            self.rect.y += self.speed

        # 防止出屏
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 480:
            self.rect.right = 480
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

class Bullet(pygame.sprite.Sprite):
    # 子弹初始化
    def __init__(self, x, y):
        super().__init__()
        # self.image = pygame.Surface((10, 20))
        self.image = pygame.image.load(".\\source\\img\\img_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 8
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -10:
            self.kill()

class Meteorite(pygame.sprite.Sprite):
    # 陨石初始化
    def __init__(self):
        super().__init__()
        self.image = random.choice(meteo_images)
        # self.image.fill((255, 0, 0))
        # self.met_image = random.choice(meteo_images)
        # self.image.blit(self.met_image, (0, 0))    # 图片填充
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 480)
        self.rect.y = random.randint(-30, -5)
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(2, 7)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        cond1 = self.rect.x < -40
        cond2 = self.rect.x > 520
        cond3 = self.rect.y > 640
        if cond1 or cond2 or cond3:
            self.rect.x = random.randint(0, 520)
            self.rect.y = random.randint(-30, -5)
            self.speedx = random.randint(-5, 5)
            self.speedy = random.randint(2, 7)


def draw_text(surf, text, size, x, y):
    font = pygame.font.SysFont("Consolas", size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

pygame.init()
pygame.mixer.init()


bg_y = 0
bg1 = pygame.image.load(".\\source\\img\\img_bg.jpg")
bg2 = pygame.image.load(".\\source\\img\\img_bg.jpg")
screen = pygame.display.set_mode((480, 600)) # 创建400 * 600游戏窗口(1200, 675)
# screen.blit(bg, (0, 0))  # 设置背景白色

FPS = 60
clock = pygame.time.Clock()

plane = Plane()
all_sprites = pygame.sprite.Group()
meteo_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()

all_sprites.add(plane)

meteo_list = [".\\source\\img\\img_meteorite_0{0}.png".format(i) for i in range(9)]
meteo_images = []
for i in meteo_list:
    meteo_images.append(pygame.image.load(i))

for i in range(8):
    met = Meteorite()
    all_sprites.add(met)
    meteo_sprites.add(met)

hit_sound = pygame.mixer.Sound(".\\source\\mic\\hit.wav")
shoot_sound = pygame.mixer.Sound(".\\source\\mic\\shoot.ogg")
pygame.mixer.music.load(".\\source\\mic\\BGmusic.mp3")
pygame.mixer.music.play(loops = -1)
running = True  # 设置运行标志

while running:
    if plane.lives <= 0:
        running = False
    for event in pygame.event.get():    # 获取事件
        if event.type == pygame.QUIT:   # 鼠标点击关闭，设置运行标志为False
            running = False
        if event.type == pygame.KEYDOWN:    # 检测键盘是否按下
            if event.key == pygame.K_ESCAPE:    # 按下Esc，设置运行标志为False
                running = False
            if event.key == pygame.K_SPACE:
                plane.shoot()
                
    
    clock.tick(FPS)

    bg_y += 3
    if bg_y == 1200:
        bg_y = 0
    screen.blit(bg1, (0, bg_y))
    screen.blit(bg2, (0, bg_y - 1200))

    hits = pygame.sprite.groupcollide(meteo_sprites, bullet_sprites, True, False)
    for hit in hits:
        met = Meteorite()
        all_sprites.add(met)
        meteo_sprites.add(met)
        hit_sound.play()
        score += 1
    hit = pygame.sprite.spritecollide(plane, meteo_sprites, True)
    if hit:
        plane.lives -= 1
    
    draw_text(screen, "score " + str(score), 20, 50, 15)
    draw_text(screen, "life " + str(plane.lives), 20, 150, 15)
    # 在 screen 100, 100处建立飞机对象
    #screen.blit(plane.image, plane.rect)
    all_sprites.update()
    all_sprites.draw(screen)
    # bullet.update()
    
    pygame.display.update()
    
pygame.quit()

print("\nGame over!\nscore: " + str(score) + "\n")

