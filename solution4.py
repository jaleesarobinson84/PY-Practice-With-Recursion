# Write code for algorithm 4 below
def power(x, n):
    if x == 0:
        return 1
    elif x == 1:
        return x
    else:
        return x * power(x, n - 1)
    
    print(power(2, 3))
    print(power(5, 2))
    