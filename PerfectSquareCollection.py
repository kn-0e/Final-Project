import math
#first I'll try to list out some perfect squares
# i = 0
# while i < math.inf:
#     i +=1 
#     i**2
# this is to create a list of three numbers
x = 0
y = 0 
z = 0
l = []
inf = 1000
while x < inf:
    x += 1
    while y < inf:
        y += 1
        while z < inf:
            z += 1
            l = [x,x+y,x+y+z]
            print (l)
        if z == inf:
            z = 0
    if y == inf:
            y = 0
