import pygame
pygame.init()
class store:
	def __init__(self, screen):
		#self.ammosprite = pygame.image.load('files/ammo.bmp')
		#self.ammorect = ammosprite.get_rect()
		#self.ammorect.centerx = 512
		#self.ammorect.centery = 768
		self.screen = screen
		self.ammo = 0
		self.explosion = 0
		self.citys = 0
		self.autoturrets = 0
		self.shields = 0
		self.missilespeed = 0
		self.turrrets = 0
	def draw(self,screen):
		self.screen.blit(self.ammosprite, self.ammorect)
##	def handleevents():
##            for event in pygame.event.get():
##        	if event.type == pygame.QUIT:
##                    pygame.quit()
##            	    sys.exit()
##        	if event.type == pygame.KEYDOWN:
##            	    if event.key == pygame.K_ESCAPE:
##                	pygame.quit()
##                	sys.exit()
##            	elif event.key == pygame.K_UP:
##                	return(True)
##            	else:
##                	return(False)
##        	if event.type == pygame.KEYUP:
##            	if event.key == pygame.K_UP:
##                	return(False)
##			if event.type == mousebuttondown:
##				x,y = mouse.get_pos()
##				if x is in ammo rect and y is in ammo rect and money > 99:
##					self.ammo += 1
##					self.money -= 100
