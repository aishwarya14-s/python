# Prime Number Checker

# Description: Ask for an integer greater than 1 and determine if it is a prime number (only divisible by 1 and itself).

# What it practices: You will use a loop to test divisibility across a range of numbers and a conditional statement to check if the remainder is zero, which instantly proves the number is not prime.
is_prime = True
number = int(input('Enter a number: '))
if number == 0 or number == 1:
    print("Non Prime Number") 
else: 
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime number")
    else:
        print("Non Prime")
