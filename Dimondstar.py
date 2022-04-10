#   *
#  ***
# *****
#  ***
#   *

m=1
i=1
while i<=3:
    j=1
    while j<=(3-i):
        print(" ",end="")
        j=j+1
    s=1
    while s<=m:
        print("*",end="")
        s=s+1
    m+=2
    print()
    i+=1
i=2
# m=3
while i>0:
    j=(3-i)
    j-=1
    # print(j)
    # while j>0:
    print(" "*j,end=" ")
    
    s=1
    while s<=(i*2)-1:
        print("*",end="")
        s+=1
    # m-=2
    print()
    i-=1

