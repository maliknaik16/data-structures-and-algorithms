
import math

def sieve_of_eratosthenes(n):
    """
    Efficiently Finds all the prime numbers until the given number (<= n).

    Time Complexity: O(n log log n)
    """

    # Initialize the empty list to store the primes.
    primes = []

    # Create a list of consecutive integers from 2 to n.
    A = [True for i in range(n + 1)]

    for p in range(2, int(math.sqrt(n))):

        if A[p]:

            # Get all the multiples of p.
            j = p * p

            while j <= n:

                # Mark the jth number as eliminated since it's not prime.
                A[j] = False

                j = j + p

    for i in range(2, n + 1):

        if A[i]:
            primes.append(i)

    return primes

if __name__ == '__main__':

    print('Printing prime numbers < 113:')
    print(sieve_of_eratosthenes(113))

# Result:
# ---
# Printing prime numbers < 113:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
