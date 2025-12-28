# Task 1 : Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Total Time Taken: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


@measure_time
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers


append_numbers()


# Task 2 : Create a parameterised decorator retry that retries a function a specified number of times.

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
            print("All retry attempts failed")
        return wrapper
    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")
    raise ValueError("Something went wrong")
	

# Task 3 : Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.

def validate_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be a positive number")
        return func(x)
    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5


print(square_root(9))


# Task 4 : Create a decorator cache that caches the result of a function based on its arguments.
# Write a cache decorator for it to check if the calculation is already performed then return the result.

def cache(func):
    stored_results = {}

    def wrapper(*args):
        if args in stored_results:
            print("Returning cached result")
            return stored_results[args]
        print("Performing computation...")
        result = func(*args)
        stored_results[args] = result
        return result

    return wrapper


@cache
def expensive_computation(x):
    return x * x


print(expensive_computation(5))
print(expensive_computation(5))


# Task 5 : Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.

 	 
def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' not in user.get('permissions', []):
            print("Access denied")
            return
        return func(user, *args, **kwargs)
    return wrapper


@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 101)
delete_user(user2, 102)
delete_user(user3, 103)




