#!/usr/bin/env python3
import pygame
from random import randint

#pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode((512, 480))
pygame.display.set_caption('Monster Hunter')
# pygame.mixer.init()
win_sound = pygame.mixer.Sound('sound/win.wav')
#lose_sound = pygame.mixer.Sound('sound/loose.wav')
bg_image = pygame.image.load('img/background.png').convert_alpha()
hero_image = pygame.image.load('img/hro.png')
monster_image = pygame.image.load('img/mnstr.png')
goblin_image = pygame.image.load('img/gbln.png')
clock = pygame.time.Clock()

# background music
pygame.mixer.music.load('sound/music.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


class character:
    def __init__(self):
        self.x = 200
        self.y = 200

    def Wrap(self):
        if self.x > 512:
            self.x -= 512
        elif self.x < 0:
            self.x += 512

        if self.y > 480:
            self.y -= 480
        elif self.y < 0:
            self.y += 480


class Hero(character):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 200
        self.name = 'Hero'

    def Move(self, event):
        if event.key == pygame.K_LEFT:
            self.x -= 2
        elif event.key == pygame.K_RIGHT:
            self.x += 2
        elif event.key == pygame.K_UP:
            self.y -= 2
        elif event.key == pygame.K_DOWN:
            self.y += 2


class Monster(character):
    def __init__(self):
        super().__init__()
        self.x = 150
        self.y = 150
        self.name = 'Monster'
        self.randx = randint(-3, 3)
        self.randy = randint(-3, 3)

    def Move(self, count):
        if count == 0:
            self.randx = randint(-5, 5)
            self.randy = randint(-5, 5)

        self.x += self.randx
        self.y += self.randy
        self.Wrap()


class Goblin(character):
    def __init__(self):
        super().__init__()
        self.x = 400
        self.y = 400
        self.name = 'Goblin'


class Player:
    def __init__(self):
        self.rect = pygame.rect(0, 512),


Hero = Hero()
Goblin = Goblin()
Monster = Monster()


def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    red_color = (255, 25, 25)

    # Game initialization
    stop_game = False
    moving = False
    count = 120
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
            if event.type == pygame.KEYDOWN:
                moving = True
            elif event.type == pygame.KEYUP:
                moving = False
        # collision Detection
            if Hero.x + 32 < Monster.x:
                collide = True
            elif Monster.x + 32 < Hero.x:
                collide = True
            elif Hero.y + 32 < Monster.y:
                collide = True
            elif Monster.y + 32 < Hero.y:
                collide = True

        # Game logic
        if moving:
            Hero.Move(event)
        Monster.Move(count)

        # Game display
        screen.blit(bg_image, (0, 0))
        screen.blit(hero_image, (Hero.x, Hero.y))
        screen.blit(monster_image, (Monster.x, Monster.y))
        screen.blit(goblin_image, (Goblin.x, Monster.y))

        pygame.display.update()
        clock.tick(60)
        count -= 1
        if count < 0:
            count = 120

    pygame.quit()


if __name__ == '__main__':
    main()
