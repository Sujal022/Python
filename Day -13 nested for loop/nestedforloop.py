# for i in range(5):
#     print("*")

# for i in range(5):
#     print("*",end=" ")    

# for i in range(5):
#     print("*"*3) #incorrect way of writing

# row=int(input("Enter number = "))
# col=int(input("Enter number = "))
# for i in range(row):
#     for j in range(col):
#         print("*",end=" ")
#     print()

# row=int(input("Enter number = "))
# col=int(input("Enter number = "))
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         print(i,end=" ")
#     print()

# row=int(input("Enter number = "))
# col=int(input("Enter number = "))
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         print(j,end=" ")
#     print()

# row=int(input("Enter number = "))
# col=int(input("Enter number = "))
# counter=0
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         counter+=1
#         print(counter,end=" ")
#     print()

# WAP to show multiplication table
row=int(input("Enter number = "))
col=int(input("Enter number = "))
for i in range(1,row+1):
    for j in range(1,col+1):
        print(i*j,end=" ")
    print()