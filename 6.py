def function(num):
	"""Return difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
	sum=0
	sum1=0
	for i in range(num):
		sum=sum+i**2
	for i  in range(num):
		sum1=sum1+i
	return (sum1**2)-sum
print(function(11))