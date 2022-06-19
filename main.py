from Background import Background
from Game import Game


def main():
    background = Background()
    game = Game(background)

    game.initialize()


if __name__ == '__main__':
    main()
