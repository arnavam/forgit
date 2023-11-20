import random

class Game:
    def __init__(self) -> None:
        self.board = [str(i+1) for i in range(9)]

    def __str__(self):
        a = [self.board[i*3:(i+1)*3] for i in range(3)]
        return '\n'.join(' | '.join(i) for i in a)

    def win(self, bd=None):
        bd = self.board if bd is None else bd
        for i in range(3):
            row = bd[i*3:(i+1)*3]
            col = [x for y, x in enumerate(bd) if (y+i+1) % 3 == 0]
            if len(set(row)) == 1 or len(set(col)) == 1:
                return True

        d1 = [bd[i] for i in range(0, 9, 4)]
        d2 = [bd[i] for i in range(2, 7, 2)]
        if len(set(d1)) == 1 or len(set(d2)) == 1:
            return True
        return False

    def avail(self, bd=None):
        bd = self.board if bd is None else bd
        count = []
        for i in set(map(str, range(1, 10))):
            if i in bd:
                count.append(bd.index(i))
        return count

    def play(self, player):
      stack = []
      avail = self.avail()
      b = {}

      for ch in avail:
          stack.append((self.board.copy(), ch, player))

      while stack:
          bd_copy, ch, player = stack.pop()
          bd_copy[ch] = player

          if self.win(bd_copy) and player == 'o':
              b[ch] = -1 * len(avail) - 1
          elif self.win(bd_copy) and player == 'x':
              b[ch] = 1 * len(avail) + 1
          elif len(self.avail(bd_copy)) == 0:
              b[ch] = 0
          else:
              stack.extend((bd_copy.copy(), i, 'x' if player == 'o' else 'o') for i in self.avail(bd_copy))

      if player == 'x':
          item = max(b, key=lambda x: b[x])
          value = max(b.values())
      else:
          item = min(b, key=lambda x: b[x])
          value = min(b.values())

      return item, value



key = 'x'
p = 1
game_instance = Game()
unavail = []

while True:
    print(game_instance)

    a = input("where do you like to place? ")
    if a.isdigit():
        a = int(a) - 1
        if 0 > a or 8 < a:
            print("please, select a number between 1 to 9!")
            continue
    else:
        print("invalid input")
        continue

    if a not in unavail:
        key = 'x' if key == 'o' else 'o'
        game_instance.board[a] = key
        unavail.append(a)
    else:
        print("choose a valid square")
        continue

    if game_instance.win():
        print(game_instance)
        print("congrats! you have won the game")
        break
    if len(game_instance.avail()) == 0:
        print(game_instance)
        print("seems it's a draw")
        break

    best_move, _ = game_instance.play(key)
    key = 'x' if key == 'o' else 'o'
    game_instance.board[best_move] = key
    unavail.append(best_move)

    if game_instance.win():
        print(game_instance)
        print("sorry, you have lost the game")
        break
