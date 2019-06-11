from othello.board import Board


class Othello(object):

    def __init__(self, battle_order="BLACK"):
        self.board = Board()
        self.players = None
        self.battle_order = battle_order
        self.turn = 0
        self.winner = None
        # TODO
        self.game_record = None

    def skip(self):
        pass

    def wait(self):
        pass

    def move(self, x, y):
        next_reversible = []

        # ゲームが継続する条件：
        # 1: ボードにBLANKがある。かつ、どちらのプレイヤーもpassできない。
        # TODO　ゲーム終了条件：
        # 2: self.turn == 60 または、プレイヤの連続pass


        # プレイヤが、オセロを指す。
        player = self.players[self.battle_order]
        hand = player.play(self.board, x, y)

        # 置ける場所だった場合、listに座標が入って返る。
        # プレイヤのリクエストに対して、色が変わる場所のリストを、クライアント側まで返してあげる。
        if hand:
            print(f"{player.name}の手は、({x}, {y})で、リバースする座標は、{hand}です。")

            # 手を指すことに成功したので、バトルチェンジをし、ターンをインクリメント。
            self.change_battle_order()
            self.turn += 1
            next_player = self.players[self.battle_order]

            # 次のプレイヤが、置ける場所を探索する。
            # 戻り値が、空のリストの場合、passフラグを示す。
            next_reversible = self.board.positionable(next_player.stone)
            print(f"{next_player}が、次に置ける手は、{next_reversible}です。")

        return {"reverse": hand,
                "next_battle_order": self.battle_order,
                "next_reversible": next_reversible
                }

    def change_battle_order(self):
        self.battle_order = "WHITE" if self.battle_order == "BLACK" else "BLACK"

    def init_player(self, players):
        self.players = players

    def end_game(self):
        pass


if __name__ == '__main__':
    pass
    # BLACK = Stone("●")
    # WHITE = Stone("○")
    #
    # user = User("あなた", BLACK)
    # computer = Computer("CPU", WHITE)
    #
    # # BLANKがどっちで、WHITEがどっちかチェックを入れる
    # players = {"BLACK": user, "WHITE": computer}
    #
    # othello = Othello(players)
    # othello.game()
