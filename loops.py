#for loop
#fruits=["apple", "banana", "cherry"]
#for fruit in fruits:
#   print('I like', fruit)

#print 1 to 10 numbers using for loop
#for i in range(1,11):
#    print(i)

#print i to 100 even numbers using for loop
#for i in range(1,101):
#    if i%2==0:
#        print(i)

#sum of first n numbers
#n=int(input('enter a number:'))
#sum=0
#for i in range(1,n+1):
 #   sum+=i
#print('sum is:',sum)

#multiplication usingg for loop
n=int(input('enter a number:'))
#for i in range(1,10):
#    print(n,'x',i,'=',n*i)

#n=int(input('enter a number:'))
#fact=1
#for i in range(1,n+1):
#    fact=fact*i
#    print("factorial of:",fact)

#n=int(input("enter a number:"))
#a,b=0,1
#for i in range(n):
#    print(a,end=' ')
#    c=a+b
#    a=b
#    b=c

#reverse
#num=int(input('enter a number:'))
#rev=0
#lenght=len(str(num))

#for i in range(lenght):
#    digit=num%10
#    rev=rev * 10 + digit
#   num=num//10
#     print(rev)

#sum of even and odd numbers
#n=int(input('enter a number:'))
#even=0
#odd=0
#for i in range(1,n+1):
#    if i%2==0:
#        even+=i
#    else:
#        odd=odd+i
#print('sum of even is:',even)
#print('sum of odd is:',odd)

#*pattern
#n=int(input('enter a number:'))
#for i in range(1,n+1):
#    for j in range(1,i+1):
#        print('*',end=' ')
#    print()

#while loops
#i=1
#while i<=10:
#    print(i,end=" ")
#    i+=1

#sum of first n natural numbers using while loop
#n=int(input('enter a number:'))
#i=1
#total=0
#while i<=n:
#    total=total+i
#    i+=1
#    print('sum is:',total)

n = int(input('Enter a number: '))
rev = 0
while n > 0:
    digit = n % 10          # Get the last digit
    rev = rev * 10 + digit  # Add it to reversed number
    n = n // 10             # Remove the last digit

print('Reverse is:', rev)
