#Accept string from a user and display only those characters which are present at an even index number.
s=input("Enter The String:")#stores the String
print("Characters which are present at even index number are:")
for i in range(len(s)):
    if(i%2==0):
        print(s[i])#print the character which are at even index
        
    
    

    
    
