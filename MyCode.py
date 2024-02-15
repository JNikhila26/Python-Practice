# n=121
# on = n
# rev_n = 0
# while n>0:
#     rem = n%10
#     rev_n = (rev_n*10) + rem
#     n = n//10
# if on == rev_n:
#     print("p")
#     print(1%10)
# else:
#     print("NP")

n = 10
for i in range(1,n+1):
    c = 0
    for j in range(1,i+1):
        if i % j == 0:
            c+=1
    if c == 2:
        print(i)



