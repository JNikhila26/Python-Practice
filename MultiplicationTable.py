# n = 10
# for i in range(1,n+1):
#     print()
#     for j in range(1,n+1):
#         res = i*j
#         print(i,"*",j,"=",res)
#
# Using function

def table(n):
    res = 0
    for i in range(1,n+1):
        print()
        for j in range(1,11):
            res = i*j
            print(i,"*",j,"=",res)

n = int(input("Enter Value : "))
table(n)
