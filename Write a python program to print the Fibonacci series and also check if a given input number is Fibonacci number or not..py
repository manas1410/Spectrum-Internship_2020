#Write a python program to print the Fibonacci series and also check if a given input number is Fibonacci number or not.
import math#importing the math function

n=int(input("Enter the Range Number:"))#stores the range of fibonacci series
a=0#stores the 1st element of fibonacci series
b=1#stores the 2nd element of fibonacci series
c=0# c used as temporary variable
if(n<=0):
    print("Please enter a postive integer")
else:
    print("Fibonacci series upto {}:".format(n),end='')
    for i in range(0,n):
        print(str(a),end=',')#print next elements
        c=a+b
        a=b
        b=c
    u=5*n*n +4#used as temporary variable
    v=5*n*n -4#used as temporary variable
    squ=int(math.sqrt(u))#stores the square root of u
    sqv=int(math.sqrt(v))#stores the square root of v
    if(u==squ*squ or v==sqv*sqv):
        print("\n{} is a Fibonacci Number".format(n))#print entered number is a fibonacci Number
    else:
        print("\n{} is not a Fibonacci Number".format(n))#print entered number is not a fibonacci Number

   
            
        
        
    
    
