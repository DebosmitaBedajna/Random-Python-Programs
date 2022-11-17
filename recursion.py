def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def nCr(n,r):
    if n==r or r==0:
        return 1
    else:
        return (factorial(n)/((factorial(n-r)*factorial(r))))
    
choice=int(input("Enter 1 to get factorial or 2 to get combination: "))
n=int(input("Enter the number for which you want to check: "))
if choice==1:
    ans=factorial(n)
    print("Factorial is: ")
    print(ans)
elif choice==2:
    r=int(input("Enter the r value: "))
    ans=nCr(n,r)
    print("Combination is: "+str(ans))