# Task 1 : Write a program that asks the user for their name and then prints a greeting  message using their name.
name = input('Please enter your name : ')
print('Hello ' + name)


# Task 2 : Ask the user to enter two numbers from the user and print their sum, multiplication, and division.
num1 = int(input('Please enter 1st number : '))
num2 = int(input('Please enter 2nd number : '))
print('Sum = '+ str(num1 + num2))
print('Multiplication = '+ str(num1 * num2))
if num2 != 0:
    print('Division = ' + str(num1 / num2))
else:
    print('Division not possible (division by zero)')


# Task 3 : Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
names = input('Please enter names seperated by comma : ')
nameList = names.split(',')
print(nameList)


# Task 4 : Ask the user to enter their age and check if they are eligible to vote based on their age.
age = int(input('Please enter your age : '))
if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')


# Task 5 : For value = 3.14159, Using f-string print output for only up to 2 decimal places. 
value = 3.14159
print(f"{value:.2f}")

