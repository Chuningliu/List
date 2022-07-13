# For example, if we give 9119  the function should return  811181,
# as the  square of 9 is 81 and square of 1  is 1.

a=int(input("Enter the number:"))
i=0
while a>0:
    digit=a%10
    sum=digit*digit
    a=a//10
    d=a*a
    print(d,end=" ")
    print(sum)
    break
    
    
    