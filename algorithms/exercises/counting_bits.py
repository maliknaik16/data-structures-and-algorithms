
def num_bits(num):
    """
    Returns number of bits in the binary representation of the given number.

    Time Complexity: O(logn)
    """

    if num == 0:
        return 0

    return 1 + num_bits(num >> 1)
    # or,
    # return 1 + num_bits(num // 2)



if __name__ == '__main__':

    num1 = 17
    num2 = 4

    print('Number of bits in %d are %d' % (num1, num_bits(num1)))
    print('Number of bits in %d are %d' % (num2, num_bits(num2)))

# Result:
# ---
#
# Number of bits in 17 are 5
# Number of bits in 4 are 3
