from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from othello.game import Othello
from othello.player import Player, User
from othello.board import Stone


app = Flask(__name__)
bootstrap = Bootstrap(app)

othello = Othello()


@app.route("/")
def index():
    print(id(othello))

    # プレイーについては別途考える。
    players = init_player()
    othello.init_player(players)
    return render_template("index.html", board=othello.board)


@app.route('/skip', methods=['POST'])
def skip():
    id = request.json['id']
    print(id)
    othello.skip()

    response = {

    }
    return jsonify(response), 200


@app.route('/wait', methods=['POST'])
def wait():
    id = request.json['id']
    print(id)
    othello.wait()

    response = {

    }
    return jsonify(response), 200


@app.route('/move', methods=['POST'])
def move():
    coordinate = request.json['id']
    x, y = [int(a) for a in coordinate]
    print((x, y))

    response = othello.move(x, y)
    print(response)

    # リターンする値は、
    # リクエストがきたプレイヤの置いた場所、リバースした場所、（つまり、色が変わる場所）
    # 次のプレイヤ（BLACK or WHITE）
    # 次のプレイヤのリバースできる場所。
    print("\n".join(" ".join(row) for row in othello.board))

    return jsonify(response), 200


def init_player():
    BLACK = Stone("●")
    WHITE = Stone("○")
    user = User("あなた", BLACK)
    computer = User("CPU", WHITE)

    return {"BLACK": user, "WHITE": computer}


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


