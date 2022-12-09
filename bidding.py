from replit import clear


dictionary={}
print("Welcome to the Bidding club!")
while(1):
    name=input("Enter your name please: ")
    bid=int(input("Enter your bid in Rupees: "))
    dictionary.update({name:bid})
    ans=input("Are there any other bidders?(Y/N):")
    if(ans.upper()=='Y'):
        clear()
        continue
    elif(ans.upper()=='N'):
        break
    else:
        print("Invalid answer try again.")
        

clear()
minbid=0
for keys in dictionary:
    if dictionary[keys]>minbid:
        key=keys
        minbid=dictionary[keys]
        
print("The maximum bidder is {} and their bid is Rupees {}".format(key,minbid))