def countdown(number):
    if number == 0:
        print(number)
    if number > 0:
        print(f'{number}')
        countdown(number - 1)

if __name__ == '__main__':
    countdown(5)