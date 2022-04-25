import pygame as pg
import sys

if __name__ == '__main__':
    pg.init()

    size = width, height = 800, 600
    speed = [1, 1]
    black = 0, 0, 0

    screen = pg.display.set_mode(size)


    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

        screen.fill(black)
        pg.display.flip()
