def isPrime(num):
  for i in range(2, num):
    if num%i==0:
      return False
  return True

def sum_Prime(n):
	"""Return sum of all the primes below two million."""
	sum=0;
	for i in range(2,int(n)):
	    if isPrime(i):
	        sum += i
	return sum
print(sum_Prime(10))