##powerset using backtracking

list1 =set()
b=set()

def power(l,b):
  if list(b) not in list(list1):
    list1.add(frozenset(b))

  for i in l :
    if i not in b :
      b.add(i)
      power(l,b)
      b.remove(i)
  return b

lst1 = [item for item in input("specify the number do you want the powerset of \n\tELSE \n enter the elements :\n").split()]

if len(lst1) ==1:
  lst1=[i+1 for i in range(int(lst1[0]))]
power(lst1,b)

print(list(list(i) for i in list1))
'''
normal method to do it
for  i in set1:
    n = len(result)
    for j in range(n):
        r = result[j] + [i]
        result.append(r)
'''