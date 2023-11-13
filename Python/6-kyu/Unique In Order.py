def unique_in_order(sequence):
    result = []
    prev = None

    for elem in sequence:
        if elem != prev:
            result.append(elem)
            prev = elem

    return result
