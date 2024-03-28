def euclidean_algorithm(a, b):
    """
    This function implements the Euclidean Algorithm to find the Greatest Common Divisor (GCD) of two integers.

    :param a: (int) First positive integer
    :param b: (int) Second positive integer

    :returns a: (int) GCD Result
    """

    # Loop until b becomes 0
    while b != 0:
        # Store current value of b
        temp = b
        # Update b to be the remainder of a divided by b
        b = a % b
        # Update a to previous value of b
        a = temp
    # Return a as the GCD
    return a

example_gcd = euclidean_algorithm(48, 18)