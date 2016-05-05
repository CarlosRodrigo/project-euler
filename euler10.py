## Project Euler - 10
## https://projecteuler.net/problem=10
## Summation of primes

import math

def is_prime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
  	if n % i == 0:
  	  return False
  return True

def sum_of_primes(n):
  sum = 2
  for i in range(3, n, 2):
    if is_prime(i):
    	sum += i
  return sum

print sum_of_primes(2000000)