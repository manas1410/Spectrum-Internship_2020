#Accept two integer numbers from a user and return their product and if the product is greater than 1000, then return their sum
n=int(input("Enter 1st Number:"))#stores the 1st number
m=int(input("Enter 1st Number:"))#stores the 2nd number
res=0#stores the result
if(n*m>1000):
    res=n+m
    print ("Sum of {} and {} ={}".format(n,m,res))#print sum if product of n and m is greater then 1000
else:
    res=n*m
    print("Product of {} and {} ={}".format(n,m,res))#print product if product of n and m is less then equals to 1000
    
    
    
