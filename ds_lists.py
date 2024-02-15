'''l = list(range(1,21))
print(l[::-1])
print(l[::2])

# for i,value in enumerate(l):
#     print (f"Index : {i} Value : {value}")

print(sorted(l,reverse=True))
print(l)'''

items = [("p1",10),("p2",9),("p3",12)]


items.sort(key=lambda items:items[1])
print(items)

print(sorted(items))
print("org",items)