list_of_palindromes = []

def is_palindrome(x):
    
    x = list(str(x))
    z = list(reversed(x))
    count = 0
    
    for i in range(len(x)):
        if x[i] != z[i]:
            count += 1
            
    return count < 1

def range_of_multipliers():    
    for i in range(99,999):
        for y in range(99,999):
            if is_palindrome(i*y):
                list_of_palindromes.append(i*y)
            else:
                continue

range_of_multipliers()
print(max(list_of_palindromes))