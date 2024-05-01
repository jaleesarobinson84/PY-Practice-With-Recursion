def countdown(n):
    # base case: stop when n is 0
    if n == 0:
        print("Blastoff!")
        return
    # Print current value of n
    print(n)
    # Call countdown recursively
    countdown(n - 1)
    
    # test function
    countdown(5)
    