import sys

file_name = sys.argv[1]


def is_prime(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n & 1 == 0:
        return 0
    d= 3
    while d * d <= n:
        if n % d == 0:
            return 0
        d= d + 2
    return 1


with open(file_name) as input_numbers:
    for line in input_numbers:
        number = int(line)
        print(is_prime(number))
