def sum_series(number):
    if number < 1:
        return 0
    if number >= 1:
        return number + sum_series(number-2)

if __name__ == '__main__':
    print(sum_series(7))
    print(sum_series(8))
    print(sum_series(15))
