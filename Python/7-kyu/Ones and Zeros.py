def binary_array_to_number(arr):
    result = 0
    for bit in arr:
        result = (result << 1) | bit
    return result
