## Project Euler - 09
## https://projecteuler.net/problem=9
## Special Pythagorean triplet

def is_pythaegorean(a, b, c):
  return a**2 + b**2 == c**2
  
def find_pythaegorean(n):
  for a in range(1, n//2):
    for b in range(1, n//2):
      for c in range(1, n//2):
        if a + b + c == 1000 and is_pythaegorean(a, b, c):
          print a, b, c
          return a*b*c
  return -1

print find_pythaegorean(1000)