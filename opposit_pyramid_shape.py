# *********
#  *******
#   *****
#    ***
#     *



n=int(input("Enter the number :"))

i=1
while n>0:
    j=1
    while j<i:
        print(" ",end="") 
        j+=1
    s=1
    while s<=(n*2)-1:
        print("*",end="")
        s+=1
    print()
    n-=1
    i+=1

