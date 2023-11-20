from  random import randrange
from time import sleep
#from termcolor import colored, cprint
class player :
    def __init__(self,i) :
        self.score =0
        self.name=input(f'enter the name of the player {i+1} : ')
        self.table=[]
    def play (self):
        input("press a key to play\033[5m !")
        b='y'
        while(b!='n'):
          print("rolling the dice \033[5m..\033[0m")
          sleep(2)
          print()
          a= randrange(6) +1
          if(a!=1) :
            self.score =self.score+a
            print("rolling the dice ..")

            print(f"you have played  {a}")
            print(f"your current score is {self.score} ")
          else :
             self.score =0
             print(f"you have played {a}")
             print(f"sry ,your score is {self.score} ")
             break
          b=input("do you want 1 more round? y/n : ")
        self.table.append(self.score)
        
x=int(input("enter no of players : "))
obj=[player(i) for i in range(x)]

n=2
for _ in range(n):
  for i in range(x) :
    print('\n------------------')
    print(f' player {obj[i].name}`s turn')
    print('------------------')
    obj[i].play()
a= 0
q= max(obj, key=lambda x: x.score)
e ="\n".join([i.name]+[ "  |  ".join([str(j) for j in i.table]) for i in obj])
sleep(0.5)
print('------------------')
print(f"congrats {q.name} you have won the game! , with a score of {q.score}")
print(e)
print('------------------')