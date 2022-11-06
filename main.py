import random
import numpy as np
import pygame
from perlin_noise import PerlinNoise

import threading


class Game:
    E = '7182818284590452353602874'
    WIDTH = 200
    HEIGHT = 200

    def __init__(self):

        self.running = True
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.clock = pygame.time.Clock()
        self.fps = 60

        #self.seed = int("".join(self.perm_table()))
        self.seed = 1
        self.noise1 = PerlinNoise(octaves=1, seed=self.seed)
        self.noise2 = PerlinNoise(octaves=2, seed=self.seed)
        self.noise3 = PerlinNoise(octaves=3, seed=self.seed)
        self.noise4 = PerlinNoise(octaves=4, seed=self.seed)

        self.scale = 1

        self.heights = []
        self.t1 = threading.Thread(target=self.setup)

        self.t1.start()

        #print(threading.current_thread())
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if not self.t1.is_alive():
                    if event.key == pygame.K_UP:
                        self.scale -= 1
                        self.t1 = threading.Thread(target=self.setup)
                        self.t1.start()
                    if event.key == pygame.K_DOWN:
                        self.scale += 1
                        self.t1 = threading.Thread(target=self.setup)
                        self.t1.start()

    def setup(self):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                n1 = self.noise1([x * self.scale/self.WIDTH, y * self.scale/self.HEIGHT])
                #n2 = self.noise2([x * self.scale/self.WIDTH, y * self.scale/self.HEIGHT])
                #n3 = self.noise3([x * self.scale/self.WIDTH, y * self.scale/self.HEIGHT])
                #n4 = self.noise4([x * self.scale/self.WIDTH, y * self.scale/self.HEIGHT])
                #c = abs(int((n1 + n2 + n3 + n4) * 255 / 4))
                c = abs(int(n1 * 255 / 1))
                #print((c, c, c))
                self.heights.append(c)
                self.display.set_at((x, y), (c, c, c))
                #print(len(self.heights))
                self.progress = len(self.heights)

    def perm_table(self):
        table = []
        for i in range(25):
            #for j in range(25):
            table.append(random.choice(self.E))
        return table

    def update(self):
        pygame.display.update()
        #print(threading.current_thread())

    def draw(self):
        #self.display.fill((0, 0, 0))
        #self.display.blit(self.loading_surface, (0, 0))
        pass

    def run(self):
        while self.running:

            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    #print(threading.current_thread())
    game.run()
