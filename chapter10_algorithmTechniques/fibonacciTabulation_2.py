def fib(n):
    """
    Calculate the Fibonacci's series value for integer n

    Parameters:
    - n: The number to use in the Fibonacci's series.

    Returns: The calculated value of the Fibonacci's series for n
    """
    if n == 0 or n == 1:
        return 1

    prev2 = 1   # fib(0)
    prev1 = 1   # fib(1)

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1