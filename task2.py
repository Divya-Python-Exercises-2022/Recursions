def factorial(number):
    if number == 0 or number == 1:
        return 1
    if number > 1:
        return number * factorial(number - 1)

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(10))
