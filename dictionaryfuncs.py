dictionary={}
d2={}
keys=list(map(str, input("Enter the keys: ").split()))
#keys=keys.split(" ")
for i in keys:
    print("Enter value for key "+i+": ")
    y=input()
    dictionary.update({i: y})
for x,y in dictionary.items():
    print(x+" : "+y)    
for x in dictionary.keys():
    print(x)
for y in dictionary.values():
    print(y)

d2=dictionary.copy()
print("Is there any new key that you want to enter?(Y/N)")
a=input()
if (a=='y'or a=='Y'):
    k1=list(map(str, input("Enter new keys: ").split()))
    for i in k1:
            print("Enter value for "+i+" : ")
            y=input()
            d2.update({i:y})
elif(a=='n' or a=='N'):
    print("Okay!")
for i in d2.keys():
    if(i in dictionary.keys()):
        print(i+" is found in both dictionaries")
    else:
        print(i+" is unique to dictionary two")