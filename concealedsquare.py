a = [] #list of numbers that has 3 or 7 as the last number
for x in range(100000000,139902663):
    y = str(x)
    if y[8] == '3' or y[8]=='7':
        a.append(y)

for x in a:
    b = int(x)**2 #this is the number that will be the answer
    b=str(b)
    if b[0]=='1' and b[2]=='2' and b[4]=='3' and b[6]=='4' and b[8]=='5' and b[10]=='6' and b[12]=='7' and b[14]=='8' and b[16]=='9':
        print ((int(b)**(1/2))*10)
        print (int(b)*100)
