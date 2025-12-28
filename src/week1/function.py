# Task 1 : Define a function calculate_area that calculates the area of a rectangle and return the result. If no width is provided, it defaults to 10.
def calculate_area(length, width=10):
    return length * width

print(calculate_area(5))        
print(calculate_area(5, 4))     


# Task 2.  Write a recursive function to compute the factorial of a non-negative integer.
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) 


# Task 3. Write a function that takes one parameter as a string and reverse it and return.
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("hello"))


# Task 4. Write a Python function that takes two parameters as lists and to sum all the numbers in a list. 

def sum_two_lists(list1, list2):
    return sum(list1) + sum(list2)

a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
print(sum_two_lists(a, b))


# Task 5. Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list. a = [4,1,2,3,3,1,3,4,5,1,7]
def distinct_sorted_list(lst):
    return sorted(set(lst))

a = [4,1,2,3,3,1,3,4,5,1,7]
print(distinct_sorted_list(a))

