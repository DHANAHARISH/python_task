def Task(num1,num2):
    if num1 and num2 % 2==0:
        a=num1+num2
        print(a,'is even')
        return a
    else:
        a=num1*num2
        print(a,'is odd')
        return a