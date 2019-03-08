import fractions

def lcm(n):
	""" Return smallest positive number that is evenly divisible by all of the numbers from 1 to 20"""
    ans = 1    
    for i in range(1, n + 1): 
        ans = (ans * i)/fractions.gcd(ans, i)         
    return ans 
print(lcm(20))