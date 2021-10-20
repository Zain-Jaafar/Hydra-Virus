import pygame
import os
import random

win_x, win_y = 200, 200 #random.randint(200, 800), random.randint(100, 600)
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (win_x, win_y)

pygame.init()

pygame.display.set_caption("Hydra Virus, get trolled noob")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("x button pressed")

if __name__ == "__main__":
    main()