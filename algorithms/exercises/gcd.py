
def gcd(m, n):
    """
    Euclid’s algorithm is based on repeated application of equality:

        gcd(m,n) = gcd(n, m mod n)

    until the second number becomes 0, which makes the problem trivial.

    Time Complexity: O(min(m, n))
    """

    if n == 0:
        return m

    return gcd(n, m % n)

def gcd_iterative(m, n):
    """
    Computes the GCD of two positive integers iteratively.

    Time Complexity: O(min(m, n))
    """

    while n > 0:
        remainder = m % n
        m = n
        n = remainder

    return m

if __name__ == '__main__':

    # Get the GCD (Greatest Common Divisor) with the recursive algorithm.
    result1 = gcd(60, 24)

    # Get the GCD with the iterative algorithm.
    result2 = gcd_iterative(60, 24)

    assert result1 == result2, "GCD is not same..."

    print('GCD of 60 and 24:', result1)
    print('GCD of 60 and 24:', result2)

# Result:
# ---
#
# GCD of 60 and 24: 12
# GCD of 60 and 24: 12

