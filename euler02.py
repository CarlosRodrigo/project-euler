# Project Euler - 02
# https://projecteuler.net/problem=2
# Even Fibonacci numbers

def even_fib_sum(n):
  fib_sum = 0
  a, b =  0, 1
  while a < n:
    a, b = b, a+b
    if(a % 2 == 0):
      fib_sum += a
  return fib_sum

def main():
  print even_fib_sum(4000000)

if __name__ == "__main__":
  main()