# Project Euler - 07
# https://projecteuler.net/problem=7
# 10001st prime
import math

def is_prime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def prime_number(n):
  i = 1
  count = 0
  while count < n:
    i += 1
    if is_prime(i):
      count += 1
  return i

def main():
  print prime_number(10001)

if __name__ == "__main__":
  main()