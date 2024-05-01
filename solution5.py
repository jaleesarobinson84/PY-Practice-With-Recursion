# Write code for algorithm 5 below
def is_palindrome(s):
    # remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # check if the string is a palindrome
    if s == s[::-1]:
        return True
    else:
        return False
    print(is_palindrome("radar"))
    print(is_palindrome("welcome"))
    print(is_palindrome("logic whens overflow"))