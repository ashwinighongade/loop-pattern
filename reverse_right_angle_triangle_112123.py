#     1
#    12
#   123
#  1234
# 12345       

i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end="")
        j=j+1
    n=1
    while n<=i:
        print(n,end="")
        n=n+1
    print()
    i=i+1 