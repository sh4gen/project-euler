# fibonacci Numbers? sum of the 2 previous number
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

first_term = 1
second_term = 2
temp = 0
counter = 0

user_input = int(input("Enter your border: "))

while second_term <= user_input:
    if second_term % 2 == 0:
        counter += second_term
    temp = second_term
    second_term += first_term
    first_term = temp

print(counter)