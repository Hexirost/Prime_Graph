MAX = 100000000

lis = [True for i in range(MAX+1)] 
n = 2
while (n * n <= MAX): 
        
    if (lis[n] == True): 
            
        for i in range(n * 2, MAX+1, p): 
            lis[i] = False
    n += 1
    
file = open("prime_" + str(MAX)+ ".txt","w+")

for p in range(2, MAX): 
    if lis[p]: 
        file.write(str(p) + "\n")

file.close()