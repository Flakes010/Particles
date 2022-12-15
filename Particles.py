import pygame, sys, random


class Particle:
    def __init__(self):
        self.particles = []
        
    def add(self):
        xpos = pygame.mouse.get_pos()[0] # x position
        ypos = pygame.mouse.get_pos()[1] # y position
        r = 10 # radius yarıçap
        xdir = random.randint(-3, 3) # random integer
        ydir = random.randint(-3, 3)
        circle = [
                   [xpos, ypos], # 1
                   r,  # 2
                   [xdir, ydir]    # 3
                  ]
        self.particles.append(circle)

    def check(self):
        self.particles = [p for p in self.particles if p[1] > 0]

    def draw(self, color):
        if self.particles: #returns False if it contains nothing
            self.check() #cleaning
            for circle in self.particles:
                circle[0][0] += circle[2][0]
                circle[0][1] += circle[2][1]
                circle[1] -= 0.2
                pygame.draw.circle(surface=win, color=pygame.Color(color), center=circle[0], radius=int(circle[1]))

p1 = Particle()
p2 = Particle()
p3 = Particle()

WIDTH, HEIGHT = 500, 500

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("Particles")
win = pygame.display.set_mode((WIDTH, HEIGHT))

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 60)

while True:

    win.fill((30, 30, 30))
    p1.draw("yellow")
    p2.draw("red")
    p3.draw("green")
    pygame.display.update() 
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == PARTICLE_EVENT:
            p1.add()
            p2.add()
            p3.add()
