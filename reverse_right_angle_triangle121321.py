#     1
#    21
#   321
#  4321 
# 54321


i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end="")
        j=j+1
    s=i
    while s>0:
        print(s,end="")
        s=s-1
    print()
    i=i+1