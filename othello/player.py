from abc import ABCMeta
from abc import abstractmethod


class Player(metaclass=ABCMeta):

    def __init__(self, name, stone):
        self.name = name
        self.stone = stone

    def __repr__(self):
        # クラス名なら返せる。
        return self.__class__.__name__

    @abstractmethod
    def play(self, board, x, y):
        pass

    @abstractmethod
    def think(self, board):
        pass


class User(Player):

    def play(self, board, x, y):
        reversed = board.put(x, y, self.stone)
        if reversed:
            # リバースしたコマと、自分の置いたコマの座標をすべて返す。
            reversed.append((x, y))

        return reversed

    def think(self, board):
        pass


class Computer(Player):

    def play(self, board, x, y):
        x, y = self.think(board)
        reversed = board.put(x, y, self.stone)
        if reversed:
            # リバースしたコマと、自分の置いたコマの座標をすべて返す。
            reversed.append((x, y))

        return reversed

    def think(self, board):



        return (x, y)


if __name__ == '__main__':
    pass

