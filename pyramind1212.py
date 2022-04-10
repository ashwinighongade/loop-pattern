#     1
#    212
#   32123
#  4321234
# 543212345

i=1
while i<=5:
    j=1
    while j<=(5-i):
        print(" ",end=" ")
        j=j+1
    s=i
    while s>0:
        print(s,end=" ")
        s=s-1
    m=2
    while m<=i:
        print(m,end=" ")
        m=m+1
    print()
    i=i+1