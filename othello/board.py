# OPPONENT = {BLACK: WHITE, WHITE: BLACK}


class Stone(str):
    pass


class Board(object):
    SIZE = 8
    BLACK = Stone("●")
    WHITE = Stone("○")
    BLANK = Stone("×")
    VECTOR = ((-1, -1), (+0, -1), (+1, -1),
              (-1, +0),           (+1, +0),
              (-1, +1), (+0, +1), (+1, +1))

    def __init__(self):
        self._cells = [[self.BLANK for i in range(self.SIZE)] for j in range(self.SIZE)]
        self._cells[3][3] = self.WHITE
        self._cells[3][4] = self.BLACK
        self._cells[4][3] = self.BLACK
        self._cells[4][4] = self.WHITE

    # いらなかった。。。
    # def __iter__(self):
    #     yield self

    def __repr__(self):
        return "\n".join(" ".join(row) for row in self._cells)

    def __getitem__(self, x):
        return self._cells[x]

    # put()できない条件：
    # 1: 石が既に置いてある
    # 2: reverseできない場所に置こうとする
    def put(self, x, y, stone):
        if self[x][y] is not self.BLANK:
            return []

        reversible = self.reversible(x, y, stone)
        if not reversible:
            return []

        self[x][y] = stone
        for x, y in reversible:
            self[x][y] = stone

        return reversible

    # オセロとは、リバーシブルであるかどうかなんだな～
    # ココきれいにならんかね。。。
    #
    # リバース可能な座標を、list型で返す。(ただし、引数自身の座標は返さない。)
    # listが莫大に大きくならないので、ジェネレータ型は考えない。
    def reversible(self, x, y, stone):
        reverse_list = []
        for dx, dy in self.VECTOR:
            tmp = []
            depth = 0
            while True:
                depth += 1
                rx = x + (dx * depth)
                ry = y + (dy * depth)

                if 0 <= rx < self.SIZE and 0 <= ry < self.SIZE:
                    check_stone = self[rx][ry]
                    if check_stone == self.BLANK:
                        break
                    elif check_stone == stone:
                        reverse_list.extend(tmp)
                        break
                    else:
                        tmp.append((rx, ry))
                else:
                    break

        return reverse_list

    # 置ける場所の探索
    # ジェネレータではなく、list型で返す。
    # 理由は、条件式において、listの中身がnullの場合、falseになるから。
    def positionable(self, stone):
        return [(x, y)
                for x in range(self.SIZE)
                for y in range(self.SIZE)
                if self.reversible(x, y, stone)]

    # 置いていない場所の探索
    # Ture or Falseで返す。
    def is_playable(self):
        # BLANKがあった場合、Trueを返し、ゲームができる状態であることを伝える。
        return any(col == self.BLANK
                   for row in self._cells
                   for col in row)


def check_stone(stone):
    for x, y in b.positionable(stone):
        b[x][y] = CHWCK


if __name__ == '__main__':
    BLACK = Stone("●")
    WHITE = Stone("○")
    CHWCK = Stone("-")
    b = Board()

#    check_stone(BLACK)
    print("\n".join(" ".join(row) for row in b._cells))
    print("---------------------------------------")
    b.put(4, 5, BLACK)
#    check_stone(WHITE)
    print("\n".join(" ".join(row) for row in b._cells))
    print("---------------------------------------")

    b.put(3, 5, WHITE)
    check_stone(BLACK)
    print("\n".join(" ".join(row) for row in b._cells))
    print("---------------------------------------")




