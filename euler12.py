## Project Euler - 12
## https://projecteuler.net/problem=12
## Highly divisible triangular number

def number_of_divisors(n):
  divisors = 0
  for i in range(1, n+1):
    if n % i == 0:
      divisors += 1
  return divisors

def triangle_sequence(n):
  triangle = 0
  # for i in range(1, n+1):
  found = False
  i = 0
  while not found:
    i += 1
    triangle += i
    if number_of_divisors(triangle) > n:
      found = True
  return triangle
    
print triangle_sequence(100)
