import pygame
import random


def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    canvas_width = 512
    canvas_height = 480

    pygame.init()
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption('Monster Hunter')
    clock = pygame.time.Clock()
    bg = pygame.image.load('img/background.png').convert_alpha()
    hero = pygame.image.load('img/hero.png')
    monster = pygame.image.load('img/monster.png')
    goblin = pygame.image.load('img/goblin.png')
    hero_x = 200
    hero_y = 200
    monster_x = 150
    monster_y = 150
    goblin_x = 300
    goblin_y = 300
    adjust = random.randint == 0
    change_dir_countdown = 120

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
        if event.type == pygame.KEYDOWN:
            change_dir_countdown -= 1
            if change_dir_countdown == 0:
                change_dir_countdown == 120
                monster_x += random.randint(0, 3)

            if event.key == pygame.K_LEFT:
                hero_x -= 5
            elif event.key == pygame.K_RIGHT:
                hero_x += 5
            elif event.key == pygame.K_UP:
                hero_y -= 5
            elif event.key == pygame.K_DOWN:
                hero_y += 5

                # monster movements
            # if event.key == pygame.K_LEFT:
                #monster_x -= 5
            # elif event.key == pygame.K_RIGHT:
                #monster_x += 5
            # elif event.key == pygame.K_UP:
                #monster_y -= 5
            # elif event.key == pygame.K_DOWN:
                #monster_y += 5
                # Goblin movements
            # if event.key == pygame.K_LEFT:
                #goblin_x -= 5
            # elif event.key == pygame.K_RIGHT:
            #   goblin_x += 5
            # elif event.key == pygame.K_UP:
                #goblin_y -= 5
            # elif event.key == pygame.K_DOWN:
                #goblin_y += 5

        # Game logic
        # hero_x += hero_dir_x
        # hero_y += hero_dir_y

        if monster_x > 512:
            monster_x -= 512
        elif monster_x < 0:
            monster_x += 512

        if monster_y > 480:
            monster_y -= 480
        elif monster_y < 0:
            monster_y += 480

        if hero_x > 512:
            hero_x -= 512
        elif hero_x < 0:
            hero_x += 512

        if hero_y > 480:
            hero_y -= 480
        elif hero_y < 0:
            hero_y += 480

        if goblin_x > 512:
            goblin_x -= 512
        elif goblin_x < 0:
            goblin_x += 512

        if goblin_y > 480:
            goblin_y -= 480
        elif goblin_y < 0:
            goblin_y += 480

    # Draw background
        screen.blit(bg, (0, 0))
        screen.blit(hero, (hero_x, hero_y))
        screen.blit(monster, (monster_x, monster_y))
        screen.blit(goblin, (goblin_x, monster_y))

    # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
