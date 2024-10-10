import pygame
from constants import *
from player import Player,Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys


def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    times = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group,drawable_group)
    Asteroid.containers = (asteroids_group,updatable_group,drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (shots_group,drawable_group,updatable_group)

    astreroids_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

     

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in updatable_group:
            object.update(dt)
        
        for asteroid in asteroids_group:
            for shot in shots_group:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()

        for object in asteroids_group:
            if object.collisions(player):
                print('Game over!')
                sys.exit()

        screen.fill('black')
        for object in drawable_group:
            object.draw(screen)
        pygame.display.flip()
        dt = (times.tick(60)/1000)
        

if __name__ == '__main__':
    main()