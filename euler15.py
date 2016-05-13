## Project Euler - 15
## https://projecteuler.net/problem=15
## Lattice paths

def fac(n):
  if n > 1:
    return n * fac(n - 1)
  else:
    return 1
    
def factorial(n):
  fac = 1
  for i in range(1, n+1):
    fac *= i
  return fac

def binomial(n, k):
  return factorial(n)/(factorial(k)**2)
  
print binomial(40, 20)
