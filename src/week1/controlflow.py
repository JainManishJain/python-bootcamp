# For loop
# Task 1: Write a program that takes the input from the user and checks if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Task 2: Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”
s = input("Enter a string: ")
reversed_str = ""
for char in s:
    reversed_str = char + reversed_str
print("Reversed:", reversed_str)

if s == reversed_str:
    print("Palindrome")
else:
    print("Not a palindrome")


# Task 3: Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
n = int(input("Enter N: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Task 4: From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9. Expected output : [4, 5]
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 9:
            print([nums[i], nums[j]])



# While loop
# Task 5: Print all even numbers between 1 and 20 using a while loop.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# Break
# Task 6: Find the first occurrence of a number in a list and stop further searching. 
# numbers = [10, 20, 30, 40, 50]
# search_for = 30
numbers = [10, 20, 30, 40, 50]
search_for = 30

for num in numbers:
    if num == search_for:
        print("Found:", num)
        break


# Continue
# Task 7: Using continue statement, print only the odd numbers from 1 to 10.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# Pass
# Task 8: What will be the output 
for i in range(5):
    if i == 3:
        pass  
    print(i)

# output
#0
#1
#2
#3
#4

# Match
# Task 9: Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.
day = input("Enter day of the week: ").lower()

match day:
    case "saturday" | "sunday":
        print("Weekend")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case _:
        print("Invalid day")

