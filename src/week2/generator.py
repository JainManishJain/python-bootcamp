# Task 1 : Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers Of 10  numbers 

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()

for _ in range(10):
    print(next(fib))


# Task 2 :  Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.

def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n


multiples = infinite_multiples(3)

for _ in range(5):
    print(next(multiples))


# Task 3 :  Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.

def repeat_word(word, times):
    for _ in range(times):
        yield word


generator = repeat_word("hello", 5)

for value in generator:
    print(value)
