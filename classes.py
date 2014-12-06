import pygame, math, myMath, random
white = (255,255,255)
black = (0,0,0)
KEYCOLOR = (255,0,200)
#EXPLOSION CLASS EXPLOSION CLASS EXPLOSION CLASS EXPLOSION CLASS EXPLOSION CLASS 
class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        #self.parent = parent
        self.posx = int(pos[0])
        self.posy = int(pos[1])
        self.x = self.posx
        self.y = self.posy
        self.size = 0
        self.max_size = 20
        self.dying = False
        self.dead = False
        self.alive = True
        #explosionsnd.play()
        
    def step(self):
        if self.dying == False and self.dead == False:
            self.size+=1.5
        if self.size>self.max_size:
            self.dying = True
            
    def draw(self,screen):
        screen = screen
        if self.dying:
            self.dead = True
            self.alive = False
            return pygame.draw.circle(screen, black, (self.posx, self.posy), int(self.size+1))
        if self.dead == False and self.dying == False:
            return pygame.draw.circle(screen, white, (self.posx, self.posy), int(self.size))
        
    def dead(self):
        return self.dead
# BULLET CLASS BULLET CLASS BULLET CLASS BULLET CLASS BULLET CLASS BULLET CLASS
class bullet():
    def create (self, color, pos, x):
        self.alive = True
        self.shot = True
        self.color = color
        self.speed = 20
        self.pos = pos   
        self.nextx = 0
        self.sourcey = 760
        self.sourcex = x
        self.nexty = self.sourcey
        self.destx = pos[0]
        self.desty = pos[1]
        self.x = self.sourcex + 2
        self.y = self.sourcey + 2
        self.angle = myMath.angle_to(self.destx, self.desty, self.x, self.y)
        #shoots.play()
        
    def step(self):
        if self.shot == True:
            if self.alive == True:
                self.x -= math.cos(self.angle)*self.speed
                self.y -= math.sin(self.angle)*self.speed
                self.sourcex -= math.cos(self.angle)*self.speed
                self.sourcey -= math.sin(self.angle)*self.speed
    def draw(self, screen):
        if self.alive == True:
            pygame.draw.line(screen, self.color, (self.sourcex, self.sourcey), (self.x, self.y))
# MISSILE CLASS MISSILE CLASS MISSILE CLASS MISSILE CLASS MISSILE CLASS
class missile:
    def create(self, color, speed):
        self.alive = True
        self.color = color
        self.speed = speed
        self.sourcex = random.randint(0,1024)
        self.nextx = 0
        self.sourcey = 25
        self.nexty = self.sourcey
        self.target = random.randint(0, 12)
        self.destx = 20 + self.target*80
        self.desty = 732
        self.x = self.sourcex
        self.y = self.sourcey
        self.angle = myMath.angle_to(self.x, self.y, self.destx, self.desty)
    def step(self):
        if self.alive == True:
            self.x += math.cos(self.angle)*self.speed
            self.y += math.sin(self.angle)*self.speed
    def draw(self, screen):
        screen = screen
        if self.alive == True:
            if self.x < 1022 and self.y < 740:
                    pygame.draw.line(screen, self.color, (self.sourcex, self.sourcey), (self.x, self.y))
            else:
                self.alive = False
            if self.x > 1022:
                self.alive = False
            if self.x < 0:
                self.alive = False
                
# BUILDING CLASS BUILDING CLASS BUILDING CLASS BUILDING CLASS BUILDING CLASS

class building:
    def __init__(self):
        #explosions, bullets, buildings, and missiles

        #pygame.init()
        #pygame.mixer.init()
        self.building1s = pygame.image.load("files/building-1.bmp").convert()
        self.building2s = pygame.image.load("files/building-2.bmp").convert()
        self.building3s = pygame.image.load("files/building-3.bmp").convert()
        self.building4s = pygame.image.load("files/building-4.bmp").convert()
        self.building5s = pygame.image.load("files/building-5.bmp").convert()
        self.building6s = pygame.image.load("files/building-6.bmp").convert()
        self.building7s = pygame.image.load("files/building-7.bmp").convert()
        self.building8s = pygame.image.load("files/building-8.bmp").convert()
        self.building9s = pygame.image.load("files/building-9.bmp").convert()
        self.building10s = pygame.image.load("files/building-10.bmp").convert()
        #explosionsnd = pygame.mixer.Sound('snd/explosion.wav')
        #shoots = pygame.mixer.Sound('snd/shoot.wav')
        self.dirtTile = pygame.image.load('files/dirt-tile.bmp').convert()
        self.dirtTiler = self.dirtTile.get_rect()
        self.cannons = pygame.image.load('files/cannon.bmp').convert()
        self.building1r = self.building1s.get_rect()
        self.building2r = self.building2s.get_rect()
        self.building3r = self.building3s.get_rect()
        self.building4r = self.building4s.get_rect()
        self.building5r = self.building5s.get_rect()
        self.building6r = self.building6s.get_rect()
        self.building7r = self.building7s.get_rect()
        self.building8r = self.building8s.get_rect()
        self.building9r = self.building9s.get_rect()
        self.building10r = self.building10s.get_rect()
        self.building1r.centery = 733
        self.building2r.centery = 730
        self.building3r.centery = 732
        self.building4r.centery = 730
        self.building5r.centery = 735
        self.building6r.centery = 732
        self.building7r.centery = 733
        self.building8r.centery = 733
        self.building9r.centery = 735
        self.building10r.centery = 733
        self.cannon1r = self.cannons.get_rect()
        self.cannon2r = self.cannons.get_rect()
        self.cannon3r = self.cannons.get_rect()
        self.cannon1r.centery = 740
        self.cannon2r.centery = 740
        self.cannon3r.centery = 740
        self.cannon1r.centerx = 20
        self.building1r.centerx = 100
        self.building2r.centerx = 180
        self.building3r.centerx = 260
        self.building4r.centerx = 340
        self.building5r.centerx = 420
        self.cannon2r.centerx = 500
        self.building6r.centerx = 580
        self.building7r.centerx = 660
        self.building8r.centerx = 740
        self.building9r.centerx = 820
        self.building10r.centerx = 900
        self.cannon3r.centerx = 980
        self.building1s.set_colorkey(KEYCOLOR)
        self.building2s.set_colorkey(KEYCOLOR)
        self.building3s.set_colorkey(KEYCOLOR)
        self.building4s.set_colorkey(KEYCOLOR)
        self.building5s.set_colorkey(KEYCOLOR)
        self.building6s.set_colorkey(KEYCOLOR)
        self.building7s.set_colorkey(KEYCOLOR)
        self.building8s.set_colorkey(KEYCOLOR)
        self.building9s.set_colorkey(KEYCOLOR)
        self.building10s.set_colorkey(KEYCOLOR)
        self.cannons.set_colorkey(KEYCOLOR)
    def draw(self, screen, buildings):
        buildings = buildings
        screen = screen
        i = 0
        if buildings[0] == 1:
            screen.blit(self.cannons, self.cannon1r)
        if buildings[1] == 1:
            screen.blit(self.building1s, self.building1r)
        if buildings[2] == 1:
            screen.blit(self.building2s, self.building2r)
        if buildings[3] == 1:
            screen.blit(self.building3s, self.building3r)
        if buildings[4] == 1:
            screen.blit(self.building4s, self.building4r)
        if buildings[5] == 1:
            screen.blit(self.building5s, self.building5r)
        if buildings[6] == 1:
            screen.blit(self.cannons, self.cannon2r)
        if buildings[7] == 1:
            screen.blit(self.building6s, self.building6r)
        if buildings[8] == 1:
            screen.blit(self.building7s, self.building7r)
        if buildings[9] == 1:
            screen.blit(self.building8s, self.building8r)
        if buildings[10] == 1:
            screen.blit(self.building9s, self.building9r)
        if buildings[11] == 1:
            screen.blit(self.building10s, self.building10r)
        if buildings[12] == 1:
            screen.blit(self.cannons, self.cannon3r)
        while i < 1024:
            screen.blit(self.dirtTile, (i,748))
            i = i + 30
