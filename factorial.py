
# Bottom-up and Top-down Dynamic Programming example for Factorial program.

# Initialize factorial list with all -1's
factorial = [-1 for _ in range(30)]

# Set 0! to 1
factorial[0] = 1

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


if __name__ == '__main__':

    print(bottom_up_factorial(7))
    print(bottom_up_factorial(8))

    print(top_down_factorial(7))
    print(top_down_factorial(6))

