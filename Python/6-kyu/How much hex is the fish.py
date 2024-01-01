def fish_hex(name):
    hex_values = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

    result = 0

    for char in name.lower(): 
        if char in hex_values:
            result ^= hex_values[char]

    return result
