import os, pygame, random, sys, math, myMath, classes, highscoreclass, easygui
from pygame.locals import *
pygame.init()
#pygame.mixer.init()
BLACK = (0,0,0)
BLUE = (50, 130, 255)
LBLUE = (120, 150, 255)
RED = (255,0,0)
#pygame.mixer.init()
#explosionsnd = pygame.mixer.Sound('explosion.wav')
#shoots = pygame.mixer.Sound('shoot.wav')
# Main Class Main Class Main Class Main Class Main Class Main Class Main Class
class Main:
    def __init__(self):
        #self.gameOver = pygame.mixer.Sound('GameOver.wav')
        #self.intros = pygame.mixer.Sound('intro.wav')
        self.WIDTH = 1024
        self.HEIGHT = 775
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        #self.tfnt = pygame.font.Font('freesansbold.ttf',70)
        #self.fnt = pygame.font.Font('freesansbold.ttf',12)
        self.gamestate = 'title'
        self.clock = pygame.time.Clock()
        self.FRAMES_PER_SECOND = 30
    def newgame(self):
        #self.intros.play()
        self.mspeed = 1
        self.mcolor = RED
        self.lines = 7
        self.paused = False
        self.missiles = []
        self.missileCount = 0
        self.explosionCount = 0
        self.score = 0
        self.deadBullets = 0
        self.gameover = False
        self.bullets = []
        self.bulletCount = 0
        self.level = 0
        self.buildings = [1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.building = classes.building()
        self.explosions = []
        self.levelOver = False
    def step(self):
        i = 0
        e = 0
        if sum(self.buildings) == 0:
            self.gamestate = 'highscores'
            print('Highscores')
        while e < self.explosionCount:
            self.explosions[e].step()
            e +=1
        for m in self.missiles:
            m.step()
            if m.alive == True and m.y > 736:
                m.alive == False
                self.buildings[m.target] = 0
                self.explosionCount += 1
                self.explosions.append(classes.Explosion((m.x, m.y)))
                #explosionsnd.play()
                #self.score -= 10
        while i < self.bulletCount:
            self.bullets[i].step()
            if myMath.dist_to((self.bullets[i].x, self.bullets[i].y), (self.bullets[i].destx, self.bullets[i].desty)) < 10 and self.bullets[i].alive == True:
                self.deadBullets += 1
                self.explosionCount += 1
                self.explosions.append(classes.Explosion((self.bullets[i].x, self.bullets[i].y)))
                #explosionsnd.play()
                self.bullets[i].alive = False
            i += 1
    def collisions(self):
        i = 0
        v = 0
        while i < self.missileCount:
            if self.missiles[i].alive:
                while v < self.explosionCount:
                    if myMath.dist_to((self.missiles[i].x, self.missiles[i].y), (self.explosions[v].x, self.explosions[v].y)) < 20 and self.explosions[v].dead == False and self.missiles[i].alive:
                        self.missiles[i].alive = False
                        self.score += 10
                        self.explosionCount += 1
                        self.explosions.append(classes.Explosion((self.missiles[i].x, self.missiles[i].y)))
                    v += 1
                v = 0
            i += 1
    def draw(self):
        [m.draw(self.screen) for m in self.missiles]
        i = 0
        for e in self.explosions:
            if e.alive == True:
                e.draw(self.screen)
        while i < self.bulletCount:
            self.bullets[i].draw(self.screen)
            i += 1
        self.building.draw(self.screen, self.buildings)

    def event(self):
        x = 0
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if e.key == K_RETURN:
                    if self.gamestate == 'highscores':
                        self.gamestate = 'title'
                    elif self.gamestate == 'title':
                        self.gamestate = 'toplaying'
                    elif self.gamestate == 'playing':
                        self.gamestate = 'highscores'
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN and self.gamestate == 'playing':
                #shoots.play()
                if e.pos[0] < 250 and self.buildings[0] == 1 or self.buildings[6] == 0 and self.buildings[12] == 0 and self.buildings[0] == 1:
                    x = 20
                    self.score -= 1
                    self.bullets.append(classes.bullet())
                    self.bullets[self.bulletCount].create(BLUE, e.pos, x)
                    self.bulletCount += 1
                elif e.pos[0] <  740 and self.buildings[6] == 1 or e.pos[0] < 740 and self.buildings[0] == 0 and self.buildings[6] == 1 or self.buildings[6] == 1 and self.buildings[12] == 0:
                    x = 500
                    self.score -= 1
                    self.bullets.append(classes.bullet())
                    self.bullets[self.bulletCount].create(BLUE, e.pos, x)
                    self.bulletCount += 1
                elif self.buildings[12] == 1:
                    x = 980
                    self.score -= 1
                    self.bullets.append(classes.bullet())
                    self.bullets[self.bulletCount].create(BLUE, e.pos, x)
                    self.bulletCount += 1
    def odd_level(self):
        self.missileCount = 0
        self.bulletCount = 0
        del self.bullets[:]
        del self.missiles[:]
        self.mspeed += 0.1
        self.mcolor = (RED)
        self.level += 1
        while self.missileCount <= self.lines:
            self.missiles.append(classes.missile())
            self.missiles[self.missileCount].create(self.mcolor, self.mspeed)
            self.missileCount += 1
    def scoreBoard(self):
        self.scoretxt = self.smallFont.render('score ' + str(self.score), True, BLUE)
        self.leveltxt = self.smallFont.render('Level  ' + str(self.level), True, BLUE)
        self.screen.blit(self.leveltxt, (900, 30))
        self.screen.blit(self.scoretxt, (10,30))
    def getname(self):
        return easygui.enterbox(msg = 'Enter your name'
                , title = 'Enter your name'
                )
        return input('please type your name')
    def even_level(self):
        self.missileCount = 0
        self.bulletCount = 0
        del self.missiles[:]
        del self.bullets[:]
        self.lines += 1
        self.mcolor = (BLUE)
        self.level += 1
        while self.missileCount <= self.lines:
            self.missiles.append(classes.missile())
            self.missiles[self.missileCount].create(self.mcolor, self.mspeed)
            self.missileCount += 1
    def loop(self):
        pygame.display.set_caption('Patriot Command')
        #self.titleFont = pygame.font.Font('freesansbold.ttf', 60)
        #self.basicFont = pygame.font.Font('freesansbold.ttf', 40)
        #self.smallFont = pygame.font.Font('freesansbold.ttf', 20)
        #self.title = self.titleFont.render('Patriot Command', True, LBLUE)
        self.highscores = highscoreclass.highScore()
        #self.by = self.basicFont.render('By Tanner Swenson', True, BLUE)
        c = 0
        #self.intros.play()
        while True:
            s = 0
            while self.gamestate == 'title':
                if s < 1:
                    #self.intros.play()
                    s +=1
                self.newgame()
                self.screen.fill(BLACK)
                #self.screen.blit(self.by,(345, 500))
                #self.screen.blit(self.title,(285,300))
                self.building.draw(self.screen, self.buildings)
                self.event()
                pygame.display.flip()
                #self.gamestate = 'toplaying'
            while self.gamestate == 'toplaying':
                self.newgame()
                self.gamestate = 'playing'
            while self.gamestate == 'playing':
                if self.level%2 == 0:
                    self.even_level()
                else:
                    self.odd_level()
                self.levelOver = False
                while not self.levelOver and self.gamestate == 'playing':
                    self.screen.fill((0,0,0))
                    self.step()
                    self.event()
                    self.draw()
                    #self.scoreBoard()
                    if c > 10:
                        self.collisions()
                        c = 0
                        self.levelOver = True
                        m = 0
                        while m < self.missileCount:
                            if self.missiles[m].alive == True:
                                self.levelOver = False
                            m += 1
                    c += 1
                    pygame.display.flip()
                    deltat = self.clock.tick(self.FRAMES_PER_SECOND)
                while self.gamestate == 'highscores':
                    #self.gameOver.play()
                    self.name = self.getname()
                    self.highscores.load()
                    self.highscores.add(self.name, int(self.score), int(self.level))
                    self.highscores.save()
                    while self.gamestate == 'highscores':
                        #self.highscores.draw(self.screen)
                        self.event()
                        pygame.display.flip()
                        deltat = self.clock.tick(self.FRAMES_PER_SECOND)
Main().loop()
