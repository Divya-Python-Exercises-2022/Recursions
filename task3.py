def harmonic_sum(number):
    if number == 1:
        return 1
    if number > 1:
        return (1/number)+(harmonic_sum(number-1))

if __name__ == '__main__':
    print(harmonic_sum(7))
    print(harmonic_sum(4))

