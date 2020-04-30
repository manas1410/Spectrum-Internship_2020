#Given a number count the total number of digits in a number
n=int(input("Enter The Number:"))#stores the number
n1=n#temporarily stores the number
c=0#counts the total Number of digits in n
while(n1>0):
    n1=n1//10
    c=c+1
print("Total Number of digits in {}={}".format(n,c))#print the total Numbers of digits in n    
    

    
    
