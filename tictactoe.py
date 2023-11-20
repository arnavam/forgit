import random

class game:
  def __init__(self) -> None:
    self.board=[str(i+1) for i in range (9)]


  def __str__(self) :
    a=[self.board[i*3:(i+1)*3]for i in range(3)]

    return '\n'.join(' | '.join(i)for i in a)
  

  def win(self,bd=None):
    bd = self.board if bd==None else  bd
    for i in range(3) :
      row=bd[i*3:(i+1)*3]
      col=[x for y,x in enumerate(bd) if(y+i+1)%3==0]
      if len(set(row))==1 or len(set(col))==1:
        return True
      
    d1=[bd[i] for i in range(0,9,4)]
    d2=[bd[i] for i in range(2,7,2)]
    if len(set(d1))==1 or len(set(d2))==1 :
      return True 
    return False
  

  def avail(self,bd=None) :
    bd =self.board if bd==None else bd
    count=[]
    set={str(i) for i in range(1,10)}
    for i in set:
      if i in bd:
        count.append(bd.index(i))
    return count

import copy

def play(bd, player):
    avail = g.avail(bd)
    b = {}

    for ch in avail:
        new_bd = copy.copy(bd)
        #new_bd=bd[:]  # Make a deep copy of the board
        new_bd[ch] = player
        next_player = 'x' if player == 'o' else 'o'

        if g.win(new_bd) and player == 'o':
            b[ch] = -1 * len(avail) - 1
        elif g.win(new_bd) and player == 'x':
            b[ch] = 1 * len(avail) + 1
        elif len(g.avail(new_bd)) == 0:
            b[ch] = 0
        else:
            result = play(new_bd, next_player)
            b[ch] = list(result.values())[0]  # Update with the result from the recursive call

    if player == 'x':
        item = max(b, key=lambda x: b[x])
        value = max(b.values())
        #print(b)
        return {item: value}
    elif player == 'o':
        item = min(b, key=lambda x: b[x])
        value = min(b.values())
        #print(b)
        return {item: value}

# Example usage:
# bd = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Initial empty board
# player = 'x'
# result = play(bd, player)
# print(result)
 

key='x'

p=1
g=game()
unavail=[]
while True:
  
  print(g)
  

  a=input("where do you like to place? ")
  if a.isdigit():
    a=int(a)-1
    if 0>a or 9<a :
      print("please,select a number b/w 0 to 9!")
      continue
  else:
      print("invalid input")
      continue
  
  
  if a  not in unavail:
   key ='x' if key  =='o' else 'o'
   g.board[a]=key
   unavail.append(a)

  else:
    print("choose a vaild square")
    continue
  if g.win()==True:
    print(g)
    print("congrats! you have won the game")
    break
  if len(g.avail())==0:
    print(g)
    print("seems its an draw")
    break
  new=g.board[:]
  sm=list(play(new,key))[0]
  print(play(new,key))
  print(g.avail())
  key ='x' if key  =='o' else 'o'
  g.board[sm] =key
  unavail.append(sm)

  

  if g.win()==True:
    print(g)
    print("sry, you have lost the game")
    break
  