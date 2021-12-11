
# Bottom-up and Top-down Dynamic Programming example for Factorial program.
from utils import *
import time

# Initialize factorial list with all -1's
factorial = [-1 for _ in range(901)]

# Set 0! to 1
factorial[0] = 1

def classic_factorial(n):
    """
    Factorial function without Dynamic Programming
    """

    if n <= 1:
        return 1
    else:
        return n * classic_factorial(n - 1)

def bottom_up_factorial(n):
    """
    Tabulation or Bottom-up approach to finding factorial of a number.
    """

    global factorial

    if factorial[n] != -1:

        return factorial[n]

    for i in range(1, n + 1):

        factorial[i] = factorial[i - 1] * i

    return factorial[n]

def top_down_factorial(n):
    """
    Memoization or Top-down approach to finding factorial of a number.
    """

    global factorial

    if factorial[n] != -1:

        return factorial[n]

    factorial[n] = n * top_down_factorial(n - 1)

    return factorial[n]

def print_time(func_name):

    start = get_current_time()
    print('Running %s function to compute 900!' % (func_name.__name__, ))
    answer = func_name(900)
    diff = get_time_diff_ms(start)
    print('Execution taken: %f ms' % (diff, ))

if __name__ == '__main__':

    print_time(classic_factorial)
    print_time(bottom_up_factorial)
    print_time(top_down_factorial)

# Results
#
# Running classic_factorial function to compute 900!
# Execution taken: 1.060247 ms
# Running bottom_up_factorial function to compute 900!
# Execution taken: 0.600815 ms
# Running top_down_factorial function to compute 900!
# Execution taken: 0.008583 ms
