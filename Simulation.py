class Simulation:

    def __init__(self):
        '''A method to initialize the simulation'''
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pi Approximation')
        self.clock = pygame.time.Clock()
        self.fontDuring = pygame.font.SysFont('timesnewroman', 100)
        self.pi = 0
        self.x = WIDTH / 2 - 500
        self.y = HEIGHT / 2 - 100
        self.radius = WIDTH / 4
        self.points = []
        self.inCount = 0
        self.count = 0
        self.values = []
        self.on = True

    def eventListener(self):
        '''A method to listen for events, specifically quit'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.on = False

    def distance(self, x, y):
        '''A method to calculate distance'''
        distance = ((self.x - x) ** 2 + (self.y - y) ** 2) ** .5
        return distance

    def shoot(self):
        '''A method to "shoot at the target"'''
        x = random.randint(self.x - self.radius, self.x + self.radius)
        y = random.randint(self.y - self.radius, self.y + self.radius)
        self.points.append((x, y))
        if self.distance(x, y) < self.radius:
            self.inCount += 1
        self.count += 1
        self.pi = 4 * self.inCount / self.count
        self.values.append(self.pi)

    def draw(self):
        '''A method to draw to the display'''
        pygame.draw.circle(self.surface, GREEN, (self.x, self.y), self.radius, 2)
        pygame.draw.rect(self.surface, RED, [self.x - self.radius, self.y - self.radius, 
                                2 * self.radius, 2 * self.radius], 3)
        for point in self.points:
            if self.distance(*point) > self.radius:
                color = RED
            else:
                color = GREEN
            pygame.draw.circle(self.surface, color, point, 2)
        fps = self.fontDuring.render(str(round(self.pi, 10)), False, WHITE)
        self.surface.blit(fps, (WIDTH / 2, HEIGHT * .9))
        #taken from http://www.pygame.org/wiki/MatplotlibPygame
        ax.plot(self.values)
        ax.hlines(math.pi, 0, len(self.values), 'Black', 'dashed')
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        self.surface.blit(surf, (WIDTH * .55, HEIGHT * .3))
                
    def updateDisplay(self):
        '''A method to update the display'''
        self.surface.fill(BLACK)
        self.shoot()
        self.draw()
        pygame.display.update()

    def run(self):
        '''A method to run the simulation'''
        while self.on:
            self.updateDisplay()
            self.eventListener()

if __name__ == "__main__":
    import pygame
    import random
    import matplotlib
    import matplotlib.backends.backend_agg as agg
    import pylab
    import math
    matplotlib.use("Agg")

    pygame.init()
    info = pygame.display.Info()
    HEIGHT = info.current_h / 1.2
    WIDTH = info.current_w / 1.2
    fig = pylab.figure(figsize=[8, 4], dpi=120)
    ax = fig.gca()
    canvas = agg.FigureCanvasAgg(fig)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    sim = Simulation()
    sim.run()