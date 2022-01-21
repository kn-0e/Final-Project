import math
#first I'll try to list out some perfect squares
# i = 0
# while i < math.inf:
#     i +=1 
#     i**2

#this is created to check if i found the numbers
def check(list):
    x = list[2]
    y = list[1]
    z = list[0]
    a = x + y
    b = x - y
    c = x + z
    d = x - z
    e = y + z
    f = y - z
    l = [a,b,c,d,e,f]
    for element in l:
        element = math.sqrt(element)
        if not element.is_integer :
            return False
    return True
            



# this is to create a list of three numbers

x = 0
y = 0 
z = 0
l = []
inf = 10000
while x < inf:
    x += 1
    while y < inf:
        y += 1
        while z < inf:
            z += 1
            l = [x,x+y,x+y+z]
            print (l)
            if check(l):
                break
        if z == inf:
            z = 0
    if y == inf:
            y = 0
print (l)


