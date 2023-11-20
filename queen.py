import random
class queen:
  def __init__(self) -> None:
    a=input("how large is the chess board")
    self.board=[ [j for j in range (a)]for i in range (a)]
    self.q=a
  def place(self,bd):
    q=random.choice(self.board)
    bd=[]
    pass
  def win(self):
    pass
  def loss(self):
   pass
  def __str__(self) -> str:
    
   pass
#kJ$2*iG
q=queen()
#kJ$2*iG
def play(q,bd):
    a= q.avial(bd)

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