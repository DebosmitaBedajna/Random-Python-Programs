def cube(n):
    return n*n*n

l1=tuple(map(int, input("Enter the numbers: ").split()))
l1=list(l1)
l3=[]
for i in l1:
    l3.append((i,cube(i)))
l3=tuple(l3)
print(l3)