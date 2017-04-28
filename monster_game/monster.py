#!/usr/bin/env python3
import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((512, 480))
pygame.display.set_caption('Monster Hunter')
clock = pygame.time.Clock()
bg_image = pygame.image.load('img/background.png').convert_alpha()
hero_image = pygame.image.load('img/hro.png')
monster_image = pygame.image.load('img/mnstr.png')
goblin_image = pygame.image.load('img/gbln.png')


class character:
    def __init__(self):
        self.x = 200
        self.y = 200


class Hero(character):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 200
        self.name = 'Hero'

    def Move(self, event):
        if event.key == pygame.K_LEFT:
            self.x -= 5
        elif event.key == pygame.K_RIGHT:
            self.x += 5
        elif event.key == pygame.K_UP:
            self.y -= 5
        elif event.key == pygame.K_DOWN:
            self.y += 5

        self.Wrap()

    def Wrap(self):
        if self.x > 512:
            self.x -= 512
        elif self.x < 0:
            self.x += 512

        if self.y > 480:
            self.y -= 480
        elif self.y < 0:
            self.y += 480


class Monster(character):
    def __init__(self):
        super().__init__()
        self.x = 150
        self.y = 150
        self.name = 'Monster'

    def Move(self):
        adjust = random.randint == 0
        change_dir_countdown = 120
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown == 120
            Monster.x += random.randint(0, 3)


class Goblin(character):
    def __init__(self):
        super().__init__()
        self.x = 400
        self.y = 400
        self.name = 'Goblin'


Hero = Hero()
Goblin = Goblin()
Monster = Monster()


def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    # Game initialization
    stop_game = False
    moving = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
            if event.type == pygame.KEYDOWN:
                moving = True
            elif event.type == pygame.KEYUP:
                moving = False

        # Game logic
        if moving:
            Hero.Move(event)

        # Draw background

        # Game display
        screen.blit(bg_image, (0, 0))
        screen.blit(hero_image, (Hero.x, Hero.y))
        screen.blit(monster_image, (Monster.x, Monster.y))
        screen.blit(goblin_image, (Goblin.x, Monster.y))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
