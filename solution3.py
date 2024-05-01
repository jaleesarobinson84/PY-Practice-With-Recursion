# Write code for algorithm 3 below
# RECURSIVE
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
# test function
    result = fibonacci_recursive(5)
    print("The 7th element of the Fibonacci sequence is", result)

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b
    # Test function
    result = fibonacci_iterative(5)
    print("The 7th element of the Fibonacci sequence is", result)