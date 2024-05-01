def love(a, b):
    while b:
        a, b = b, a % b
        return a, b
    
    print(love(10, 20))
    print(love(1071, 462))
    print(love(123456789, 123456789))
