import pickle, pygame
playing = 'yes'
yellow = (255, 245, 0)
class highScore:
    def __init__(self):
        self.scores = []
        self.scoretxt = []
        self.filename = 'files/highScores.txt'
        self.smallFont = pygame.font.Font('freesansbold.ttf', 32)
    def load(self):
        self.FILE = open(self.filename, 'rb')
        self.scores = pickle.load(self.FILE)
        self.FILE.close()
    def add(self, name, score, level):
        self.scores.append((score, name, level))
    def draw(self, screen):
        i = 0
        screen = screen
        self.hightxt = self.smallFont.render('High Scores', True, yellow)
        self.nlstxt = self.smallFont.render('Name Level Score', True, yellow)
        self.scores.sort()
        self.scores.reverse()
        screen.blit(self.hightxt,(430, 40))
        screen.blit(self.nlstxt,(395,75))
        while i < 10:
            self.scoretxt.append(self.smallFont.render(self.scores[i][1] + ' ' + str(self.scores[i][2]) + '     ' + str(self.scores[i][0]), True, yellow))
            screen.blit(self.scoretxt[i], (390, i*50 + 120))
            i += 1
        del self.scoretxt[:]
    def save(self):
        i = 0
        self.FILE = open(self.filename, 'wb')
        pickle.dump(self.scores, self.FILE)
        self.FILE.close()
