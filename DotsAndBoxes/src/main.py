# coding = UTF-8
from dots_and_boxes.game import Game
from dots_and_boxes.model import Player, Color


if __name__ == '__main__':
    game = Game(Player(Color.red), Player(Color.blue))
