#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
i=1
while i<=5:
    j=5-i
    while j>0:
        print(" ",end="")
        j=j-1
    s=1
    while s<=i:
        print("*",end=" ")
        s=s+1
    print()
    i=i+1
i=4
while i>=1:
    j=5-i
    while j>0:
        print(" ",end="")
        j=j-1
    s=1
    while s<=i:
        print("*",end=" ")
        s=s+1
    print()
    i=i-1