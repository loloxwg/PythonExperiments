import string


def kaisa(s, k):
    '''凯撒加密'''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(before, after)
    return s.translate(table)


s = "i love python"
a = kaisa(s, 3)
print(a)
