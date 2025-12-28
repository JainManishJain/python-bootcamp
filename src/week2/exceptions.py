# Task 1 : Write a Python program that attempts to divide two numbers a = 10  b = 0 and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error

a = 10
b = 0
try:
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print("Error:", e)


# Task 2 : Apply exception handling to below code and handle an exception if the index is out of range. 

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print("Error:", e)



# Task 3 : Correct this below code with appropriate exception handlings. And finally print “Execution completed”

def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid input types")
    finally:
        print("Execution completed")


safe_divide(1, 0)
safe_divide(1, "a")

