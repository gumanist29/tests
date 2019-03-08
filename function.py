#1-------------------------------------------*--
# import unittest

# def fcn(v):
# 	""" Return sum of all the multiples of 3 or 5 """
# 	sum=0
# 	for i in range(v):
# 		if(i%3==0 or i%5==0):
# 			sum=sum+i
# 	return sum
# print(fcn(10))

# 2---------------------------

# import unitesst
# def fib(num):
# 	""" Return sum even numbers"""
#     a ,b = 1,2
#     sum = 0
#     while b<num:
#         if b%2 ==0:
#             sum=sum+b
#         a=b
#         b=a+b
#     return sum
# print(fib(40000000))


# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fib(14), 24)

# if __name__ == '__main__':
#     unittest.main()



#3----------------------------------------------
# import unittest 

# def isPrime(num):
#   for i in range(2, num):
#     if num%i==0:
#       return False
#   return True

# def LargestPrimeFactor(num):
	# """Return the largest divisors of prime numbers"""
#   result=[]
#   for i in range(2, num):
#     if isPrime(i):
#       if num%i==0:
#         result.append(i)
#   return result
# print(max(LargestPrimeFactor(13195)))

# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(LargestPrimeFactor(13195), 29)

# if __name__ == '__main__':
#     unittest.main()


#4-------------------------------------------

	# 	n = 0
	# 	for a in range(999, 100, -1):
	# 	    for b in range(a, 100, -1):
	# 	         x = a * b
	# 	         if x > n:
	# 	            s = str(a * b)
	# 	            if s == s[::-1]:
	# 	                n = a * b


	# print(n)
#5----------------------------------------------
import fractions

def lcm(n): 
    ans = 1    
    for i in range(1, n + 1): 
        ans = (ans * i)/fractions.gcd(ans, i)         
    return ans 
print(lcm(20))

#6--------------------------------------------------
# def function(num):
# 	"""Return difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
# 	sum=0
# 	sum1=0
# 	for i in range(num):
# 		sum=sum+i**2
# 	for i  in range(num):
# 		sum1=sum1+i
# 	return (sum1**2)-sum
# print(function(11))
#7-------------------------------------------------------
# def isPrime(num):
#   for i in range(2, num):
#     if num%i==0:
#       return False
#   return True
# counter = 1
# num = 1
# while counter < 10001:
#     num += 2
#     if isPrime(num):
#         counter += 1
# print(num)
# import prime
# print(prime.prime(10000))
#8---------------------------------------------
# import numpy as np

# data = '''
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
# '''.replace('\n', '')


# # Convert str -> list of digits using list comprehension
# digits = [int(c) for c in data]

# # Use np.array(iterable, dtype) to create array
# # Use list comprehension to create all arrays
# # Use np.vstack to create 2d array
# mat = np.vstack([
#     np.array(digits[i:i+13], dtype=np.int)
#     for i in range(len(digits)-12)
# ])

# # Use prod on axis 1 to calculate product row wise, then print the max
# print(mat.prod(axis=1).max())




#10-----------------------------------------------------
# import unittest
# def isPrime(num):
#   for i in range(2, num):
#     if num%i==0:
#       return False
#   return True

# def sum_Prime(n):
# 	sum=0;
# 	for i in range(2,int(n)):
# 	    if isPrime(i):
# 	        sum += i
# 	return sum
# print(sum_Prime(10))


# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(sum_Prime(10), 17)
#     def test_prime(self):
#     for i in range(2, 11):
#         with self.subTest(i=i):
#             self.assertEqual(11%i, !0)


# if __name__ == '__main__':
#     unittest.main()

	