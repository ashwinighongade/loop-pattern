# col=0
# while col<=4:
#     # s=0
#     # while s<(4-col):
#     #     print(" ",end="")
#     #     s+=1
#     row=0
#     while row<=col:
#         # if col==0 or row==4 or col==row:
#         if col+row==col or col+row==(4+row)or col+row==(col*2): 
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         row+=1
#     print()
#     col+=1


col=0
while col<=4:
    row=0
    while row <=4:
        if col+row==col or col+row==(4+row) or row+col==row or row+col==(4+col):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        row+=1
    print()
    col+=1
