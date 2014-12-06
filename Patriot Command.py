import os, pygame, random, sys, math, myMath, highscoreclass, store
import classes
from pygame.locals import *
from easygui import *
pygame.init()
pygame.mixer.init()
BLACK = (0,0,0)
BLUE = (50, 130, 255)
LBLUE = (120, 150, 255)
RED = (255,0,0)
KEYCOLOR = (255,0,200)

# Main Class Main Class Main Class Main Class Main Class Main Class Main Class
class Main:
    def __init__(self):
        self.WIDTH = 1024
        self.HEIGHT = 775
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE)
        pygame.display.set_caption('Patriot Command')
        self.cursor = pygame.image.load('files/crossHairs.bmp').convert()
        self.cursorrect = self.cursor.get_rect()
        self.cursor.set_colorkey(KEYCOLOR)
        self.gameOver = pygame.mixer.Sound('files/GameOver.wav')
        self.intros = pygame.mixer.Sound('files/intro.wav')
        self.emptyclip = pygame.mixer.Sound('files/emptyclip.wav')
        self.last_score = -1
        self.last_money = -1
        self.last_ammo = -1
        
        self.store = store.store(self.screen)
        self.clock = pygame.time.Clock()
        self.timer = pygame.time.Clock()
        self.tfnt = pygame.font.Font(None,70)
        self.fnt = pygame.font.Font(None,12)
        self.gamestate = 'title'
        self.framecap = True
        self.debug = False
        self.clock = pygame.time.Clock()
        self.FRAMES_PER_SECOND = 60
        self.fps = 0
        self.frames = 0
        self.explosionsnd = pygame.mixer.Sound('files/explosion.wav')
        self.shoots = pygame.mixer.Sound('files/shoot.wav')
        self.cannon = pygame.image.load('files/cannon.bmp').convert()
        self.cannon.set_colorkey(KEYCOLOR)
        self.cannonrect = self.cannon.get_rect()
        self.cannonrect.centerx = 380
        self.cannonrect.centery = 350
        self.city = pygame.image.load('files/building-1.bmp').convert()
        self.city.set_colorkey(KEYCOLOR)
        self.cityrect = self.city.get_rect()
        self.cityrect.centerx = self.cannonrect.centerx
        self.cityrect.centery = self.cannonrect.centery + 50

        self.titleFont = pygame.font.SysFont(None, 72)
        self.basicFont = pygame.font.SysFont(None, 48)
        self.smallFont = pygame.font.SysFont(None, 26)
        self.title = self.titleFont.render('Patriot Command', True, LBLUE)
        self.by = self.basicFont.render('By Tanner Swenson', True, BLUE)
        self.intros.play()
    def newgame(self):
        self.money = 0
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
        self.buildings = [0,1,1,1,1,1,1,1,1,1,1,1,0]
        self.building = classes.building()
        self.explosions = []
        self.ammo = 18
        self.levelOver = False
    def step(self):
        i = 0
        e = 0
        if sum(self.buildings) == 0:
            self.gamestate = 'highscores'
            #self.gameOver.play()
        while e < self.explosionCount:
            self.explosions[e].step()
            e +=1
        self.levelOver = True
        for m in self.missiles:
            m.step()
            if m.alive == True:
                self.levelOver = False
            if m.alive == True and m.y > 736:
                m.alive == False
                self.buildings[m.target] = 0
                self.explosionCount += 1
                self.explosions.append(classes.Explosion((m.x, m.y)))
                #self.score -= 10
        while i < self.bulletCount:
            self.bullets[i].step()
            if myMath.dist_to((self.bullets[i].x, self.bullets[i].y), (self.bullets[i].destx, self.bullets[i].desty)) < 10 and self.bullets[i].alive == True:
                self.deadBullets += 1
                self.explosionCount += 1
                self.explosions.append(classes.Explosion((self.bullets[i].x, self.bullets[i].y)))
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
                        self.explosionsnd.play()
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
        x,y = pygame.mouse.get_pos()
        self.cursorrect.centerx = x
        self.cursorrect.centery = y
        self.screen.blit(self.cursor, self.cursorrect)
        x = 0
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif e.key == K_RETURN:
                    if self.gamestate == 'highscores':
                        self.gamestate = 'title'
                    elif self.gamestate == 'title':
                        self.gamestate = 'toplaying'
                    elif self.gamestate == 'playing':
                        self.gamestate = 'highscores'
                    elif self.gamestate == 'store':
                        self.gamestate = 'playing'
                elif e.key == K_d:
                    self.debug = not self.debug
                    self.framecap = not self.framecap
                elif e.key == K_m:
                    self.money += 1000
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN:
                if self.gamestate == 'playing':
                    if self.ammo > 0:
                        if e.pos[0] < 250 and self.buildings[0] == 1 or self.buildings[6] == 0 and self.buildings[12] == 0 and self.buildings[0] == 1:
                            x = 20
                            self.ammo -= 1
                            self.score -= 1
                            self.bullets.append(classes.bullet())
                            self.bullets[self.bulletCount].create(RED, e.pos, x)
                            self.bulletCount += 1
                            self.shoots.play()
                        elif e.pos[0] <  740 and self.buildings[6] == 1 or e.pos[0] < 740 and self.buildings[0] == 0 and self.buildings[6] == 1 or self.buildings[6] == 1 and self.buildings[12] == 0:
                            x = 500
                            self.ammo -= 1
                            self.score -= 1
                            self.bullets.append(classes.bullet())
                            self.bullets[self.bulletCount].create(RED, e.pos, x)
                            self.bulletCount += 1
                            self.shoots.play()
                        elif self.buildings[12] == 1:
                            x = 980
                            self.ammo -= 1
                            self.score -= 1
                            self.bullets.append(classes.bullet())
                            self.bullets[self.bulletCount].create(RED, e.pos, x)
                            self.bulletCount += 1
                            self.shoots.play()
                        else:
                            self.emptyclip.play()
                if self.gamestate == 'store':
                    if cannonrect.collidepoint(e.pos) and self.money > 499:
                        if self.buildings[0] == 0 or self.buildings[6] == 0 or self.buildings[12] == 0:
                            self.money -= 500
                            if self.buildings[0] == 0:
                                self.buildings[0] = 1
                            elif self.buildings[6] == 0:
                                self.buildings[6] = 1
                            else:
                                self.buildings[12] = 1
                    if cityrect.collidepoint(e.pos) and self.money > 499:
						loopcounter = 0
						for building in self.buildings:
							if building == 0 and loopcounter != 0 and loopcounter != 6 and loopcounter != 12:
								self.money -= 500
								self.buildings[loopcounter] = 1
								break
							loopcounter += 1
    def odd_level(self):
        self.score += self.ammo * 10
        self.ammo = self.lines + 10 + self.store.ammo
        self.missileCount = 0
        self.bulletCount = 0
        del self.bullets[:]
        del self.missiles[:]
        self.mspeed += 0.08
        self.mcolor = (RED)
        self.level += 1
        self.leveltxt = self.smallFont.render('Level  ' + str(self.level), True, BLUE)

        while self.missileCount <= self.lines:
            self.missiles.append(classes.missile())
            self.missiles[self.missileCount].create(self.mcolor, self.mspeed)
            self.missileCount += 1
    def scoreBoard(self):
        if self.score != self.last_score:
            self.scoretxt = self.smallFont.render('Score ' + str(self.score), True, BLUE)
        if self.last_money != self.money:
            self.moneytxt = self.smallFont.render('Money: $' + str(self.money), True, BLUE)
        if self.last_ammo != self.ammo:
            self.ammotxt = self.smallFont.render('Ammo: ' + str(self.ammo), True, BLUE)
        if self.debug == True:
            self.fps = int(self.fps)
            self.fpstxt = self.smallFont.render("FPS: " + str(self.fps), True, BLUE)

            self.screen.blit(self.fpstxt,(460, 50))
        self.screen.blit(self.leveltxt, (900, 30))
        self.screen.blit(self.scoretxt, (10, 30))
        self.screen.blit(self.moneytxt, (10, 50))
        self.screen.blit(self.ammotxt, (460, 30))
        self.last_score = self.score
        self.last_ammo = self.ammo
        self.last_money = self.money
    def getname(self):
        return enterbox(msg = 'Enter your name'
                , title = 'Enter your name'
                )
    def even_level(self):
        self.score += self.ammo * 10
        self.missileCount = 0
        self.bulletCount = 0
        del self.missiles[:]
        del self.bullets[:]
        self.lines += 1
        self.mcolor = (BLUE)
        self.level += 1
        self.ammo = self.lines + 10 + self.store.ammo
        self.leveltxt = self.smallFont.render('Level  ' + str(self.level), True, BLUE)

        while self.missileCount <= self.lines:
            self.missiles.append(classes.missile())
            self.missiles[self.missileCount].create(self.mcolor, self.mspeed)
            self.missileCount += 1
    def draw_store(self):
        self.scoretxt = self.smallFont.render('Score ' + str(self.score), True, BLUE)
        self.leveltxt = self.smallFont.render('Level  ' + str(self.level), True, BLUE)
        self.ammotxt = self.smallFont.render('Ammo: ' + str(self.ammo), True, BLUE)
        self.moneytxt = self.smallFont.render('Money: $' + str(self.money), True, BLUE)
        self.cannontxt = self.smallFont.render('Extra Cannon - $500', True, BLUE)
        self.citytxt = self.smallFont.render('Buy back city - $500', True, BLUE)
        self.screen.blit(self.cannon, self.cannonrect)
        self.screen.blit(self.city, self.cityrect)
        self.screen.blit(self.citytxt,(self.cityrect.centerx + 30, self.cityrect.centery))
        self.screen.blit(self.cannontxt, (self.cannonrect.centerx + 30, self.cannonrect.centery - 5))
        self.screen.blit(self.leveltxt, (10, 70))
        self.screen.blit(self.scoretxt, (10, 30))
        self.screen.blit(self.moneytxt, (10, 50))
        self.screen.blit(self.ammotxt, (10, 90))
    def loop(self):

        self.highscores = highscoreclass.highScore()

        c = 0
        self.intros.play()
        while True:
            s = 0
            while self.gamestate == 'title':
                if s < 1:
                    self.intros.play()
                    s +=1
                self.newgame()
                self.screen.fill(BLACK)
                self.screen.blit(self.by,(350, 500))
                self.screen.blit(self.title,(300,300))
                self.building.draw(self.screen, self.buildings)
                self.event()
                pygame.display.flip()
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
                    self.scoreBoard()
                    if c > 5:
                        self.collisions()
                        c = 0
                    c += 1
                    if self.levelOver == True:
                        for g in self.buildings:
                            if g == 1:
                                self.money += 10
                        self.gamestate = 'store'
                    pygame.display.flip()
                    if self.framecap == True:
                        deltat = self.clock.tick(self.FRAMES_PER_SECOND)
                    else:
                        self.clock.tick()
                    self.fps = self.clock.get_fps()
                    print self.fps
                while self.gamestate == 'store':
                    self.screen.fill((0,0,0))
                    self.event()
                    self.draw_store()
                    pygame.display.flip()
                    deltat = self.clock.tick(self.FRAMES_PER_SECOND)
                    #self.gamestate = 'playing'
                while self.gamestate == 'highscores':
                    self.name = self.getname()
                    self.gameOver.play()
                    self.highscores.load()
                    self.highscores.add(self.name, int(self.score), int(self.level))
                    self.highscores.save()
                    self.highscores.load()
                    while self.gamestate == 'highscores':
                        self.highscores.draw(self.screen)
                        self.event()
                        pygame.display.flip()
                        deltat = self.clock.tick(self.FRAMES_PER_SECOND)
pygame.mouse.set_visible(False)
Main().loop()
