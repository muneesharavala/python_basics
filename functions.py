#function
#def greet(name):
#    print("hello",name)
#greet('alice')
#print("iam outside the function")

#def add(n1,n2):
#    sum=n1+n2
#    print("sum is:",sum)
#add(int(input("enter first number:")),int(input("enter second number:")))

#def square(n):
#    square=n*n
#    return square
#square=square(int(input("enter a number:")))
#print("square is:",square)

#import math
#square_root=math.sqrt(4)
#print("square root is:",square_root)
#power=math.pow(2,4)
#print('power is:',power)

#def greet(name,message='hello'):
#    print(message,name)
#greet('alice')
#greet(name='muneesh',message='hi')

def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%2==0:
            return False
    return True
n=int(input('enter a number:'))
if prime(n):
    print(n,'is a prime number')
else:
    print(n,'is not a prime number')