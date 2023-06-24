user_input = int(input("Enter your number for largest prime factor: "))
largestNumber = 1

for i in range(1,user_input):             # We want to check the divisors.

    if user_input % i == 0:               
        primeNumber = True

        for j in range(2,i):              # We are looking at whether the divisor we are checking is a prime number.

            if (i % j == 0):

                primeNumber = False
                break

        if primeNumber:

            largestNumber = i
    

print(largestNumber)



