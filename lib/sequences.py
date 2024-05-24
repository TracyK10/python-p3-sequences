#!/usr/bin/env python3

def print_fibonacci(length):
    numbers = []
    
    if length > 0:
        numbers.append(0)
    if length > 1:
        numbers.append(1)
    if length > 2:
        for number in range(2, length):
            numbers.append(numbers[number - 1] + numbers[number - 2])
    print(numbers)
        
print(print_fibonacci(9)) # => [0, 1, 1, 2, 3, 5, 8, 13, 21]