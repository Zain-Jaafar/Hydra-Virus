import pygame
import os
import random




WIDTH, HEIGHT = 500, 200
window = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    while True:
        for i in range(2):
            win_x, win_y = 200, 200 #random.randint(200, 800), random.randint(100, 600)
            os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (win_x, win_y)
            win_x = win_x + 50
            win_y = win_y + 50
        
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                print("x button pressed")

if __name__ == "__main__":
    main()