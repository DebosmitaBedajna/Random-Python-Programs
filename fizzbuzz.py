#Fizzbuzz problem: 1. print all numbers from 1-100 with following restrictions:
    #when the number is divisible by 3, instead of number print Fizz
    #when the number is divisible by 5, print Buzz
    #else if divisible by both 3 and 5, the number should print FizzBuzz

for i in range (1, 101):
    if(i%3==0):
        if(i%5==0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif(i%5==0 and i%3!=0):
        print("Buzz")
    else:
        print(i)
        