# import pygame as pg
import sys
import pygame
import pygame_menu

from Background import Background
from Game import Game
from Menu import Menu
from Score import Score

background = Background()
score = Score()
menu = Menu()

game = Game(score, background, menu)

game.initialize()
