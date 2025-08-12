# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group() #objects that can be updated
    drawable = pygame.sprite.Group() #objects that can be drawn
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    

    while True:

        updatable.update(dt)

        screen.fill("black")

        for p in drawable:
            p.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    

if __name__ == "__main__":
    main()
