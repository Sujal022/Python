# row=int(input("enter number="))
# col=int(input("enter number="))
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         if i in (1,row) or j in (1,col):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()    


# row=int(input("enter number ="))
# count=0
# for i in range(1,row+1):
#     for j in range(1,row+1):
#         if i%2==0:
#             print(count,end=" ")
#             count-=1
#         else:
#             count+=1
#             print(count,end=" ")
#     count+=row       
#     print()             

row=int(input("Enter number ="))
a=0
b=1

for i in range(1,row+1):
    for j in range(1,row+1):
        
        if i==1 and j==1:
            print(a,end=" ")
        elif i==1 and j==2:
            print(b,end=" ")
        else:
            c=a+b
            print(c,end=" ")
            a=b
            b=c
    print()
        
