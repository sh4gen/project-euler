#A palindromic number reads the same both ways. The largest palindrome made from the product of two (2)- digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3 digit numbers.

list_of_palindromes = []
    
def is_palindrome(x):
    if len(x) <= 1:
        return True
    elif x[0] == x[-1]:
        return is_palindrome(x[1:-1])
    else:
        return False

def range_of_multipliers():    
    for i in range(99,999):
        for y in range(99,999):
            if is_palindrome(list(str(i*y))):
                list_of_palindromes.append(i*y)
            else:
                continue

range_of_multipliers()
print(max(list_of_palindromes))
