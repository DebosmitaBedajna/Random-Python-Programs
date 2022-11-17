def cmp(l1,l2):
    return lambda l1,l2: (l1 if l1>l2 else l2)

#tup1=tuple((input("enter tuple1: ").split()))
#tup2=tuple((input("enter tuple2: ").split()))
tup1=("apple", 2, 7)
tup2=("Banana", 4.5, "sheep")
tup1=list(tup1)
tup2=list(tup2)
tup3=[]
compare= cmp(len(tup1),len(tup2))
l=compare(len(tup1),len(tup2))
for i in range (l):
    try:
        tup3.append(tup1[i]+tup2[i])
    except TypeError:
        tup3.append(str(tup1[i])+str(tup2[i]))
tup3=tuple(tup3)
for i in tup3:
    print(i)