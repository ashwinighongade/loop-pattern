# i=0
# while i<=4:
#     space=5-1
#     while space > 0:
#         print(" ",end="")
#         space=space-1
#     j=0
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     space=5-1
#     while space>0:
#         print(" ",end="")
#         space-=1
#     j=0
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1


# *        *
# **      **
# ***    ***
# ****  ****
# **********

m=10
i=0
while i<=5:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    s=1
    while s<=m:
        print(" ",end="")
        s+=1
    n=1
    while n<=i:
        print("*",end="")
        n=n+1
    print()
    m=m-2
    i+=1
