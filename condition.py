#age=int(input('enter a value:'))
#b=int(input('enter b value:'))
#if a>b:
    #print('a is greater than b')
#if a>0:
#    print('a is positive')
#if age>=18:
    #print('you are eligible to vote')
    #print('please cast your vote')
    #print('you are a responsible citizen')

#elif
#a=int(input('enter a value:'))
#b=int(input('enter b value:'))
#if a>b:
 #   print('a is greater than b')
#elif a==b:
  #  print('a is equal to b')
#elif a<b:
 #   print('a is less than b')

#score=int(input('enter your score:'))
#if score>=90:
  #  print('grade A')
#elif score>=80:
#    print('grade B')
#elif score>=70:
 #   print('grade C')
#elif score>=60:
 #   print('grade D')
#elif score>=50:
#    print('grade E')

#else:
#a=int(input('enter a number:'))
#b=int(input('enter B number:'))
#if a==b:
 #   print('a is equal to b')
#else:
 #   print(' a not equals to b')
#if a>0:
 #print('a is a positive number')
#elif a<0:
  #print('a is a negative number')
#else:
 # print('a is zero')

#a=int(input('enter a value:'))
#b=int(input('enter b value:'))
#print('a is less than b') if a<b else print('a is greater than b')

#nested if 
status=input('enter your status (married/single):')
if (status=='married'):
    age=int(input('enter your age:'))
    if age>=18:
        print('you are eligible for marriage')
    else:
        print('you are not eligible for marriage')
elif(status=='single'):
    print('you are single')
    