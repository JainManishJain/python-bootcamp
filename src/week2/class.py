# Task 1 : Define a class Person with attributes name and age. Create an instance of this class and print its attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 30)
print(person1.name)
print(person1.age)


# Task 2 :Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")


account = BankAccount("12345", "John")
account.deposit(500)
account.withdraw(200)
account.check_balance()


# Task 3 :Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(", ")
        return cls(title, author)


book = Book.from_string("Python Programming, John Doe")
print(book.title)
print(book.author)


# Task 4 :Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# Task 5 :Write a code to perform multiple inheritance.

class Engine:
    def engine_type(self):
        print("Petrol Engine")


class Wheels:
    def wheel_count(self):
        print("4 wheels")


class Car(Engine, Wheels):
    def car_info(self):
        print("This is a car")


car = Car()
car.engine_type()
car.wheel_count()
car.car_info()
