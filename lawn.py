import math
import time
from pygame.locals import *
import pygame
import requests


NINETY = math.pi/2 + 0
SIZE = 20
SCALE = 20

class Mower:
    x = 0
    y = 1
    w = SCALE
    dir = NINETY
    exhaust_x = 0
    exhaust_y = 1

    speed = 1

    def rotate(self, angle):
        self.dir = angle
        self.exhaust_x = int(math.cos(self.dir))
        self.exhaust_y = int(math.sin(self.dir))

    def moveRight(self):
        self.rotate(NINETY)
        if self.x < SIZE - 2:
            self.x = self.x + self.speed
        time.sleep(.1)

    def moveLeft(self):
        self.rotate(3 * NINETY)
        if self.x > 1:
            self.x = self.x - self.speed
        time.sleep(.1)

    def moveUp(self):
        self.rotate(0)
        if self.y > 1:
            self.y = self.y - self.speed
        time.sleep(.1)

    def moveDown(self):
        self.rotate(2 * NINETY)
        if self.y < SIZE - 2:
            self.y = self.y + self.speed
        time.sleep(.1)

    def draw(self, DISPLAY):
        pygame.draw.rect(DISPLAY, (255, 0, 0), (self.x * self.w, self.y * self.w, self.w, self.w))
        pygame.draw.rect(DISPLAY, (0, 50, 0), ((self.x + self.exhaust_x) * self.w, (self.y + self.exhaust_y) * self.w, self.w, self.w))



class Lawn:
    def __init__(self):
        self.M = SIZE
        self.N = SIZE
        self.w = SCALE
        self.height = [0 if x < SIZE or (self.M * self.N - x) < SIZE or x % SIZE == 0 or x % SIZE == SIZE - 1 else 1 for x in range(self.M * self.N)]
        self.clippings = [0 for x in range(self.M * self.N)]

    def draw(self, DISPLAY=None):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            pygame.draw.rect(DISPLAY, (0, 160 * self.height[bx*self.M + by], min(255, 160 * self.clippings[bx*self.M + by]), 0), (bx * self.w, by * self.w, self.w, self.w))

            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1

    def mowed(self, x, y, exhaust_x, exhaust_y):
        height = self.height[x * self.M + y]
        self.height[x * self.M + y] = 0
        self.clippings[(x + exhaust_x) * self.M + (y + exhaust_y)] = self.clippings[(x + exhaust_x) * self.M + (y + exhaust_y)] + self.clippings[x * self.M + y] + .3 * height



class App:
    windowWidth = SCALE * SIZE
    windowHeight = SCALE * SIZE

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.mower = Mower()
        self.lawn = Lawn()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.lawn.draw(self._display_surf)
        self.mower.draw(self._display_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.mower.moveRight()
                self.lawn.mowed(self.mower.x, self.mower.y, self.mower.exhaust_x, self.mower.exhaust_y)

            if (keys[K_LEFT]):
                self.mower.moveLeft()
                self.lawn.mowed(self.mower.x, self.mower.y, self.mower.exhaust_x, self.mower.exhaust_y)

            if (keys[K_UP]):
                self.mower.moveUp()
                self.lawn.mowed(self.mower.x, self.mower.y, self.mower.exhaust_x, self.mower.exhaust_y)

            if (keys[K_DOWN]):
                self.mower.moveDown()
                self.lawn.mowed(self.mower.x, self.mower.y, self.mower.exhaust_x, self.mower.exhaust_y)

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    # theApp = App()
    # theApp.on_execute()
    a = {'b': 4, 'c': False, 'd':True}
    if a.get('b'):
        print(a.get('b'))
    if a.get('c'):
        print('c')
    if a.get('d'):
        print('d')
    if a.get('e'):
        print('e')
    campaigns = requests.get(
        "https://campaigndesktop.bestegg.com/api/campaignParticipants?product=PERSONAL_LOAN").json()
    print(len(campaigns))

