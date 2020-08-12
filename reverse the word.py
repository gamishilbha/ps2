
"""
Python Assignment 2-Gami Shilbha
Reverse the word

"""
name = input(" Enter the word that needs to be reversed : ")

for x in range(len(name)-1, -1, -1):
    print(name[x], end="")
