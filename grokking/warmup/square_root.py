
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

def squareRoot(num):
  if num < 2:
    return 1

  low = min(2, num)
  high = num // 2

  while low <= high:
    mid = high - ((high - low) // 2)

    if mid * mid == num:
      return mid
    elif mid * mid > num:
      high = mid - 1
    else:
      low = mid + 1

  return high


x = 8
print(squareRoot(x))

x = 4
print(squareRoot(x))

x = 2
print(squareRoot(x))

x = 16
print(squareRoot(x))