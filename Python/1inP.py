# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of the muliples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

counter = 0
user_input=int(input("Enter your border number: "))

for i in range (0,user_input):

    if i%3==0 or i%5==0:

        counter += i
    
print(counter)
    