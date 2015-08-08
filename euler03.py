# Project Euler - 03
# https://projecteuler.net/problem=3
# Largest prime factor
import math

def is_prime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def largest_prime_factor(n):
  i = 1
  largest = 0
  while i*i < n:
    i += 2
    if n % i == 0:
      if is_prime(i):
        largest = i

  return largest

def main():
  print largest_prime_factor(600851475143)

if __name__ == "__main__":
  main()