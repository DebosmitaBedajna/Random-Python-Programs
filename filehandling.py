"""f=open("Perogram.txt","xt")
f=open("Perogram.txt","at")
f.write("Hi I am Debosmita bedajna. ")
f.close()"""
l=[]
f=open("Perogram.txt","rt")
#print(f.read())
l=f.readlines()
count=0
for i in l:
    if i!='\n':
        count=count+1
print(count)
print(f.seek(2))
f.close()
