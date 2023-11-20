import random

class game:
    def __init__(self) :
        self.board=self.create()
        pass
    def create(self) :
        a=[[' ' for i in range (10)]for i in range(10)]
        for i in range (34):
            m=random.randrange(9)
            n=random.randrange(9)
            a[m][n]='x'

        return a
    
    def expand(self,e,d) :
        m=e
        n=d
     
      
        while m >= 0 and self.board[m][n]!='x' :
         
         
         while n<10 and self.board[m][n]!='x' :
            
            '''
            if(self.board[m+1][n + 1]=='x' ):
                self.board[m][n]='2'
                n=n+1   
            elif self.board[m+1  ][n]=='x' or self.board[m  ][n+1]=='x' :
                self.board[m][n]='1'
                n=n+1 
            else :
              '''
            self.board[m][n]='0'
            n=n+1
            
            
            
            
         m=m-1
         n=d
         
       

        while m < 10 and self.board[m][n] != 'x':
         
         
         while n >= 0 and self.board[m][n] != 'x':
            
            self.board[m][n]='0'
            n=n-1
         m=m+1
         n=d   
            
        
        

        while m >= 0 and self.board[m][n] != 'x':
         
         
       
        
         while n < 10 and self.board[m][n] != 'x':
            
            self.board[m][n]='0'
            n=n+1
            
          
         m=m-1
         n=d
         
       
      
      
        

    def __str__(self) -> str:
        b= [row[:] for row in self.board]
        l = [list(map(lambda x: x.replace('x', ' '), l)) for l in b]
        a ="\n".join([ f"| {(a+1)%10}{  ' | '.join(['',*i,'']) }" for a,i in enumerate(l)]) 
        return  a
    
        #replace('0','x')
        #return b

        pass
    def end(self):
        a ="\n".join([ " | ".join(['',*i,'']) for i in self.board]) 
       # a =' | '.join(self.board[' | '.join(self.board)])  
        return a

    

c=True
g=game()
while(c!=False) :
    print("    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 | ")
    print(g) 
    u,v=input("enter the positon row,col :").split(',')
    x=int(u)-1
    y=int(v)-1
    if (g.board[x][y]=='x'):
        g.board[x][y]='y'
        break
    else :
        g.board[x][y]='y'
        g.expand(x,y)

print(g.end())

print("thanks for playing the game")