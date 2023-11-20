import random
#from collections import deque
import numpy as np

MAX_LINES=3
table=[]

x='💣'
y='🍫'
z='🎊'
w='⏰'
def  machine():
  A={x:2,y:4,y:6,z:8}

  item = [i for i, j in A.items() for _ in range(j)]
  #print(item)
  #B=deque(item)
  B=item[:]
  #f=random.choice(B)
  #p=lambda x:B.remove(x)4
  global table
  table=[[ B.pop(random.randrange(len(B))) for _ in range (3)] for _ in range(3)]
  #table1=np.array(table).transpose()
  #print('\n'.join([' | '.join(i) for i in table1]))
  #print(table)
  #print(*( i for i in table))
  length =len(table[0])
  print( '\n'.join(' | '.join(j[i] for j in table)for i in range(length)))
  

def check():
  A={x:5,y:4,y:3,z:2}
  win=0
  for i in range(l):
    for j in table:
      if table[0][i]!=j[i]:
        break
    else:
      win+=A[j[i]]*a
  
  c =c+win 


def credit():
  global c
  while True:
    c=input("how much credit do you have? $") 
    if c.isdigit():
      c=int(c)
      if c<=0:
        print("insuffient amount")
      else:
        break
    else :
      print("INVALID!!")

 

def lines():
  global l
  while True  :
    l = input(f"how many lines  to beton (upto{MAX_LINES}) ")
    if l.isdigit():
      l=int(l)
      if 1<l<=MAX_LINES:
        break
      else:
        print("inavlid value")
    else :
      print("INVALID!")
  

def balance():
  global a
  while True:
    a=input("how much do you like bet? $") 
    if a.isdigit():
      a=int(a)
      
      if a<=0 or a*l>c :
        print("insuffient balance")
      else:
        break
      
    else :
     print("INVALID  !!")

 


credit()
 
lines()
balance()
machine()

  






