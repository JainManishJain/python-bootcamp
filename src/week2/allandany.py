# Task 1 : Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()

numbers = [1, 2, 3, 4, 5]
result = all(num > 0 for num in numbers)
print(result)

# Task 2 : Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()

numbers = [1, 3, 5, 7, 8]
result = any(num % 2 == 0 for num in numbers)
print(result)

# Task 3 : Determine if any number in a list is divisible by 5 an print.

numbers = [1, 3, 5, 7, 8, 10]
result = any(num % 5 == 0 for num in numbers)
print(result)
