#Password Generator
import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','-','_','+','=']
Password=''
hpass=[]

#Easy 
m=int(input("Enter number of letters: "))
n=int(input("Enter number of numbers: "))
o=int(input("Enter number of symbols: "))
for i in range (1,m+1):
    Password=Password+random.choice(letters)
for i in range (1,n+1):
    Password=Password+random.choice(numbers)
for i in range (1,o+1):
        Password=Password+random.choice(symbols)
print("Easy password is : "+Password)

#Hard
m=int(input("Enter number of letters: "))
n=int(input("Enter number of numbers: "))
o=int(input("Enter number of symbols: "))
for i in range (1,m+1):
    hpass.append(random.choice(letters))
for i in range (1,n+1):
    hpass.append(random.choice(numbers))
for i in range (1,o+1):
    hpass.append(random.choice(symbols))
    
random.shuffle(hpass)
for i in hpass:
    Password+=i
print("The hard part is: ", Password)