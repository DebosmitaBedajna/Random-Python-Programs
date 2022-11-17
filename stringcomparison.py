def compare(str1, str2):
    if(len(str1)!=len(str2)):
        return 0
    else:
        for i in range (len(str1)):
            if(str1[i]!=str2[i]):
                return 0
                break
    return 1
   
 
str1=input("String 1: ")
str2=input("String 2: ")
i=int(compare(str1,str2))
if(i==1):
    print("They are same words")
else:
    print("Not same words")