# a=[12,23,34,23,45,32,67]
# list1=[]
# i=0
# k=0
# while i<len(a):
#     j=0
#     b=[]
#     while j<2 and k!=len(a):
#         b.append(a[k])
#         j+=1
#         k+=1
#     list1.append(b)
#     if k==len(a):
#         break
#     i+=1
# print(list1)

# s=["ab","abcd","abd"]
# i=0
# max=0
# a=""
# while i<len(s):
#     if len(s[i])>max:
#         max=(len(s[i]))
#         a=s[i]
#     i+=1
# print(max,a)

# a={"b":"10", "c":"20"}
# b=[]
# c=[]

# for i in a:
#     b.append(i)
#     c.append(a[i])
    
# print(b)
# print(c)
# dict={}
# for i in range(len(b)):
#     dict.update({c[i]:b[i]})
# print(dict)

a={"a":10,"b":{"c":20}}
sum=0
for i in a:
    