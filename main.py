import pygame


WIDTH = 1300
HEIGHT = 700
SIZE = (WIDTH,HEIGHT)
FPS = 60
class ball(pygame.sprite.Sprite):
    def __init__(self,filename,coords,size):
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        self.rect = self.image.get_rect()
        self.rect.center = coords
    def reset(self):
        w.blit(self.image,(self.rect.x,self.rect.y))
class Racet(pygame.sprite.Sprite):
    def __init__(self,filename,coords,size,speed):
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.speed = speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < HEIGHT-100:
            self.rect.y += self.speed
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]and self.rect.y < HEIGHT-100:
            self.rect.y += self.speed
    def reset(self):
        w.blit(self.image,(self.rect.x,self.rect.y))

racet_l = Racet("racket.png",(50,HEIGHT/2),(50,100),10)
racet_r = Racet("racket.png",(WIDTH-50,HEIGHT/2),(50,100),10)
bal = ball("ball.png",(WIDTH/2,HEIGHT/2),(50,50))

speed_x, speed_y = 5,5



w = pygame.display.set_mode(SIZE)
backgraund = pygame.transform.scale(pygame.image.load("skyline.jpg"),SIZE)

clock = pygame.time.Clock()
pygame.font.init()
font1 = pygame.font.Font(None,60)
font2 = pygame.font.Font(None,45)

score_l = 0
score_r = 0

run = True
fin = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not fin:
        w.blit(backgraund,(0,0))
        racet_l.reset()
        racet_r.reset()
        racet_l.update_l()
        racet_r.update_r()
        
        bal.rect.x += speed_x
        bal.rect.y += speed_y
        bal.reset()
        if bal.rect.y <= 0 or bal.rect.y >= HEIGHT-50:
            speed_y = -speed_y
        if pygame.sprite.collide_rect(bal,racet_l)\
            or pygame.sprite.collide_rect(bal,racet_r):
            speed_x = -speed_x
        if bal.rect.x <= -50:
            score_r+= 1
            bal.rect.center = WIDTH/2,HEIGHT/2

        if score_r >= 5:
            fin = True
            text = font1.render("Лол",True,(255,0,0))
            w.blit(text,(WIDTH/2,HEIGHT/2))
        if bal.rect.x >= WIDTH+50:
            score_l+= 1
            bal.rect.center = WIDTH/2,HEIGHT/2
        if score_l >= 5:
            fin = True
            text = font1.render("Лол",True,(255,0,0))
            w.blit(text,(WIDTH/2,HEIGHT/2))
        score_r_t = font2.render(str(score_r),True,(255,0,0))
        score_l_t = font2.render(str(score_l),True,(255,0,0))
        w.blit(score_l_t,(WIDTH/4,50))
        w.blit(score_r_t,(WIDTH*3/4,50))
    pygame.display.update()
    clock.tick(FPS)

