"""
Python Assignment 2
Create the pattern using nested for loop
"""
a=['*']
b='*'
n=1
i=5 #the maximum number of *'s--the centre length
c=[]
print(*a)
while 0<len(a)<=(i+(i-1)):
    if n<i:
        a.append(b)
        print(*a)
        n+=1
    if n>=i and n<(2*i):
        a.remove(b)
        print(*a)
        n+=1