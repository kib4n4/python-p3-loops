#!/usr/bin/env python3

# The happy_new_year() function uses a while loop to count down from 10 to 1
# and prints each number. After reaching 1, it prints "Happy New Year!"
def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i = i - 1
    print("Happy New Year!")

# The square_integers() function takes a list of integers as input
# and returns a new list with the squared values of each integer
def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list

# The fizzbuzz() function prints the numbers from 1 to 100
# If the number is divisible by 3, it prints "Fizz"
# If the number is divisible by 5, it prints "Buzz"
# If the number is divisible by both 3 and 5, it prints "FizzBuzz"
# Otherwise, it just prints the number
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
