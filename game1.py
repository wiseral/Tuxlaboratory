#Stage
array = [["■","■","G","■","■"],["□","□","□","□","□"],["□","□","□","■","□"],["□","■","□","□","□"],["□","□","□","□","□"],["■","■","x","■","■"]]


#first position
i = 5
j = 2

#display stage
for a in array:
    print(a)

#First Time (Game start)
print("Aim to \"G\"!!")
while True:
    z = input('enter \"w\"  quit press \"q\":')
    if z == "w" or z == "q":
        break
    elif z!="w": 
        pass
if z=="w":
    array[i][j]="■"
    array[i-1][j]="x"
    i = i-1
    j = j
    #Now position
    pos = [i,j]
    for a in array:
        print(a)

#Second Time ~

while True:
    if z == "q":
        break
    if(i == 4):
        if(j == 2 or j == 3):
            z = input('enter \"w\" or \"a\" or \"d\"  quit press \"q\":')
        
        if(j == 0):
            while True:
                z = input('enter \"w\" or \"d\"  quit press \"q\":')
                if z != "a" and z != "s":
                    break
                elif z =="a" and z== "s":
                    pass
                
        if(j == 1):
            z = input('enter \"a\" or\"d\"  quit press \"q\":')
           
        if(j == 4):
            while True:
                z = input('enter \"w\" or \"a\"  quit press \"q\":')
                if z != "d":
                    break
                elif z =="d":
                    pass
    if (z == "q"):
        break
    
    if(i == 3):
        if(j == 2):
            z = input('enter \"w\" or \"d\" or \"s\"  quit press \"q\":')
            
        if(j == 0):
            while True:
                z = input('enter \"w\" or \"s\"  quit press \"q\":')
                if z != "a":
                    break
                elif z =="a":
                    pass           
        if(j == 3):
            z = input('enter \"a\" or\"d\" or \"s\" quit press \"q\":')
            
        if (j == 4):
            while True:
                z = input('enter \"w\" or \"a\" or \"s\" quit press \"q\":')
                if z != "d":
                    break
                elif z =="d":
                    pass
                
    if (z == "q"):
        break

    if(i == 2):
        if(j == 0):
            while True:
                z = input('enter \"w\" or \"s\"  quit press \"q\":')
                if z != "a":
                    break
                elif z =="a":
                    pass
        if(j == 1):
            z = input('enter \"w\" or \"d\" or \"a\"  quit press \"q\":')
         
        if(j == 2):
            z = input('enter \"w\" or \"a\" or\"s\"  quit press \"q\":')
            
        if(j == 4):
            while True:
                z = input('enter \"w\" or \"s\"  quit press \"q\":')
                if z != "d":
                    break
                elif z =="d":
                    pass
    if (z == "q"):
        break
    
    if(i == 1):
        if(j == 0):
            while True:
                z = input('enter \"s\" or \"d\"   quit press \"q\":')
                if z != "a":
                    break
                elif z =="a":
                    pass    
        if(j == 1):
            z = input('enter \"s\" or \"a\" or \"d\"  quit press \"q\":')
            
        if(j == 2):
            z = input('enter \"w\" or \"a\" or \"d\" or\"s\"  quit press \"q\":')
          
        if(j == 3):
            z = input('enter \"a\" or \"d\"  quit press \"q\":')
            
        if(j == 4):
            while True:
                z = input('enter \"a\" or \"s\"  quit press \"q\":')
                if z != "d":
                    break
                elif z =="d":
                    pass
    if (z == "q"):
        break

    if(z == "w"):
        array[i][j] = "■"
        i = i-1
        j = j 
    elif(z == "a"):
        array[i][j] = "■"
        i = i
        j = j-1
    elif(z == "d"):
        array[i][j] = "■"
        i = i
        j = j +1
    elif(z == "s"):
        array[i][j] = "■"
        i = i + 1
        j = j
    
    if array[i][j] == "■":
        break 
    array[i][j] = "x"

    for a in array:
        print(a)

    if (i == 0 and j == 2):
        break
    



#Clear Condition
f = []
for e in array:
    for g in e:
        f.append(g)

if ("□" in f ):
    array.append(0)

if all(array):
    print("GAME CLEAR") 
else:
    print("GAME OVER")