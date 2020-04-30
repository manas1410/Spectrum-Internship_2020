#Write a python program to print all the prime number in a given interval and also check is a given input number is prime or not.
def prime(x):#function to check a number is prime or not
    c=0#counter value
    for i in range(1,x+1):
        if(x%i==0):
            c=c+1
    if(c==2):
        return (True)
    else:
        return (False)
if __name__=="__main__":#main function
    n=int(input("Enter the starting Number:"))#stores the starting number
    m=int(input("Enter the ending Number:"))#stores the ending number
    v=int(input("Enter Number which you want to check:"))#stores the number which you want to check
    print("Prime Numbers from {} to {} are:".format(n,m),end='')
    for i in range(n,m+1):
        if(prime(i)==True):
            print(i,end=',')#print the prime number in the interval        
    if(prime(v)==True):
        print("\n{} is  a prime number".format(v))#print if it is a prime number
    else:
        print("\n{} is not a prime number".format(v))#print it is not a prime number
   
