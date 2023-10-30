def solution(array_a, array_b):
    if len(array_a) != len(array_b):
        raise ValueError("Input arrays must have the same length")

    squared_diff = [(abs(a - b) ** 2) for a, b in zip(array_a, array_b)]

    average = sum(squared_diff) / len(squared_diff)

    return average
