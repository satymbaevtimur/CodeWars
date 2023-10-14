def next_bigger(n):
    digits = [int(d) for d in str(n)]

    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i < 0:
        return -1

    j = len(digits) - 1
    while j > i and digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = sorted(digits[i + 1:])
    next_bigger_number = int(''.join(str(d) for d in digits))

    return next_bigger_number
