#     1
#    22
#   333
#  4444
# 55555


i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end="")
        j=j+1
    n=1
    while n<=i:
        print(i,end="")
        n=n+1
    print()
    i=i+1 
    
#     1
#    22
#   333
#  2222 
# 11111  
  
# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(" ",end="")
#         j=j+1
#     n=1
#     while n<=i:
#         print(j,end="")
#         n=n+1
#     print()
#     i=i+1 