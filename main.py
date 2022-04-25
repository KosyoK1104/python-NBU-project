from Game import Game
from Background import Background
from Score import Score

background = Background()
score = Score()

game = Game(score, background)

game.initialize()
