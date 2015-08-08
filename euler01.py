# Project Euler - 01
# https://projecteuler.net/problem=1
# Multiples of 3 and 5

def multiples(n):
  curr_sum = 0
  for i in range(n):
    if i % 3 == 0 or i % 5 == 0 :
      curr_sum += i
  return curr_sum

def main():
  print multiples(1000)

if __name__ == "__main__":
  main()