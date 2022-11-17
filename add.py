name=input("Enter your name: ")
name=name.split(" ")
l=name.pop()
modname=[]
for i in name:
        modname.append(i[0].upper()+".")
modname.append(l.lower())
print(' '.join(map(str,modname)))