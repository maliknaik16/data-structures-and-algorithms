
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.

def ugly_numbers(n, primes = [2, 3, 5]):
    """
    Compute first N ugly numbers.
    """

    # Set all zeroes.
    ugly_nos = [0 for _ in range(n)]

    # Set the first ugly number to 1.
    ugly_nos[0] = 1

    # Get number of primes
    num_primes = len(primes)

    # Set the indexes list.
    indexes = [0] * num_primes

    # Initialize prime multiples.
    prime_multiples = list(primes)

    for i in range(1, n):

        # Set the ugly number.
        ugly_nos[i] = min(prime_multiples)

        for j in range(num_primes):

            if ugly_nos[i] == prime_multiples[j]:

                # Increment index.
                indexes[j] += 1

                # Update the prime multiples.
                prime_multiples[j] = ugly_nos[indexes[j]] * primes[j]

    print(ugly_nos)

if __name__ == '__main__':

    ugly_numbers(15)
    ugly_numbers(150)

