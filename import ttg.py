import numpy as np

Standard= [[0,0,0],[0,0,1], [0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
R = 8 
C = 3
for i in range(R): 
    for j in range(C): 
        print(Standard[i][j], end = " ") 
    print()
print("break1")

inp= [[0,0,1],[0,1,1], [1,0,0],[0,1,1],[1,1,1],[1,0,1],[1,1,0],[0,0,0]]
for i in range(R): 
    for j in range(C): 
        print(inp[i][j], end = " ") 
    print()
print("break2")

result = [[inp[i][j] ^ Standard[i][j]  for j in range(len(inp[0]))] for i in range(len(inp))]    
for r in result: 
    print(r) 


