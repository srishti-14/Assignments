# LOWER TRIANGLE
rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()
    
    
 # UPPER TRIANGLE   
rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print()
    
    
# PYRAMID
rows = int(input("Enter the number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()