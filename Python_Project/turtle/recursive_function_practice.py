"""
def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
print(is_palindrome('hello'))
print(is_palindrome('level'))


def plus_ten(x):
    return x + 10

plus_ten(1)
"""
def f(x):
    return x > 10 and x < 20

a = [3, 23, 12, 17, 29, 40, 12, 15]
list(filter(f, a))