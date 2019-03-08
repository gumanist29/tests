def fcn(v):
	""" Return sum of all the multiples of 3 or 5 """
	sum=0
	for i in range(v):
		if(i%3==0 or i%5==0):
			sum=sum+i
	return sum
print(fcn(10))
