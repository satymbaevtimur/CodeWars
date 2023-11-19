def encode_rail_fence_cipher(string, n):
    if n <= 1:
        return string
    
    rails = [''] * n
    direction = 1
    row = 0

    for char in string:
        rails[row] += char
        row += direction

        if row == n - 1 or row == 0:
            direction *= -1

    return ''.join(rails)

def decode_rail_fence_cipher(string, n):
    if n <= 1:
        return string

    cycle_len = 2 * (n - 1)
    decoded = [''] * len(string)
    index = 0

    for i in range(n):
        j = 0
        while j + i < len(string):
            decoded[j + i] = string[index]
            index += 1
            if i != 0 and i != n - 1 and j + cycle_len - i < len(string):
                decoded[j + cycle_len - i] = string[index]
                index += 1
            j += cycle_len

    return ''.join(decoded)
