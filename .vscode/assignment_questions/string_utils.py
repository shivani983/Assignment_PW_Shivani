#string_utils module
rev_string=[]
def reverse(string):
    rev_string.append(string[::-1])
    return rev_string
def make_capital(string):
    return string.capitalize()    