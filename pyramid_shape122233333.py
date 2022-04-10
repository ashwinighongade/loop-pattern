#     1
#    222
#   33333
#  4444444
# 555555555

m=1
i=1
while i<=5:
    j=1
    while j<=(5-i):
        print(" ",end="")
        j=j+1
    n=1
    while n<=m:
        print(i,end="")
        n=n+1
    m=m+2
    print()
    i=i+1
