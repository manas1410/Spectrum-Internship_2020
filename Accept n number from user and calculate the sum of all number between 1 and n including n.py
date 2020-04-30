#Accept n number from user and calculate the sum of all number between 1 and n including n
n=int(input("Enter The value for n:"))#stores the value of n
sum=0#stores the sum
for i  in range(1,n+1):
    sum=sum+i
print ("Sum of all Numbers between 1 to {} = {}".format(n,sum))#print the sum from 1 to n 
    

    
    
