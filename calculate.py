a=float(input('enter a value:'))
b=float(input('enter b value:'))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def floor_div(a,b):
    return a//b
def mod(a,b):
    return a%b
def exp(a,b):
    return a**b
operator={'+':add,'-':sub,'*':mul,'/':div,'//':floor_div,'%':mod,'**':exp}
op=input("enter operator(+,-,*,/,//,%,**):")
result=operator[op](a,b)
print('result is:',result)
