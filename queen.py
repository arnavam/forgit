import random
class queen:
  def __init__(self) -> None:
    a=input("how large is the chess board")
    self.board=[ [j for j in range (8)]for i in range (8)]
    self.list=[' ' for i in range(9)]
    self.q=a
  def place(self,bd):
    
    bd=[]
    pass
  def win(self):
    pass
  def loss(self):
   pass
  def avail(self):
    pass
  def __str__(self) -> str:
    
   pass
q=queen()
avail=[i for i  in range(9)]
bd =q.board

def place(avail):
  n=q.q
  j=0
  for i in avail:
    bd[i] =j
    if i == n-1 :
      return True
    else:
      soln= place(avail)
      if soln :
        return True 
      else:
        pass
        #undo move 
        #return false
  else :
    return False
  #if no more moves are possible we need to stop 
  # return false
  #undo move
    

def play(q,bd):
    a= q.avial(bd)
#gaudl sf'

    if q.win():
      print(bd)
      return bd
    elif q.loss():
      #make the previous move null
      #continue to place in other square
      return
      
    for i in a:
      q.play(bd)

play(q,q.board)