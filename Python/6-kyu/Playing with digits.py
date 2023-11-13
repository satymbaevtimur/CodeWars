def dig_pow(n, p):
    digits = [int(digit) for digit in str(n)]
    digit_sum = sum(digit ** (p + i) for i, digit in enumerate(digits))

    if digit_sum % n == 0:
        return digit_sum // n
    else:
        return -1
