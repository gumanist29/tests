def fib(num):
	""" Return sum even numbers"""
    a ,b = 1,2
    sum = 0
    while b<num:
        if b%2 ==0:
            sum=sum+b
        a=b
        b=a+b
    return sum
print(fib(40000000))