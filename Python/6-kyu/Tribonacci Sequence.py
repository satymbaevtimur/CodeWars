def tribonacci(signature, n):
    if n == 0:
        return []

    sequence = signature[:]

    for i in range(3, n):
        next_element = sum(sequence[-3:])
        sequence.append(next_element)

    return sequence[:n]
