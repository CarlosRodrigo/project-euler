# Project Euler - 06
# https://projecteuler.net/problem=6
# Sum square difference

def sum_of_squares(n):
  curr_sum = 0
  for i in range(1, n+1):
    curr_sum += i**2
  return curr_sum

def square_of_sums(n):
  curr_sum = 0
  for i in range(1, n+1):
    curr_sum += i
  return curr_sum**2

def difference_sum_squares(n):
  return square_of_sums(n) - sum_of_squares(n)

def main():
  print difference_sum_squares(100)

if __name__ == "__main__":
  main()