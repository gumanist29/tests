
def isPrime(num):
  for i in range(2, num):
    if num%i==0:
      return False
  return True

def LargestPrimeFactor(num):
	"""Return the largest divisors of prime numbers"""
  result=[]
  for i in range(2, num):
    if isPrime(i):
      if num%i==0:
        result.append(i)
  return result
print(max(LargestPrimeFactor(13195)))
