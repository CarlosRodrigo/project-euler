# Project Euler - 04
# https://projecteuler.net/problem=4
# Largest palindrome

def is_palindrome(string):
  return string == string[::-1]

def max_palindrome_digits():
  max_palindrome = 0
  for x in range(100, 1000):
    for y in range(100, 1000):
      product = x * y
      if is_palindrome(str(product)) and product > max_palindrome:
        max_palindrome = product
  return max_palindrome
  
def main():
  print max_palindrome_digits()

if __name__ == "__main__":
  main()