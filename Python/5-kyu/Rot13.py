def rot13(message):
    result = []

    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()

            rotated_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            
            rotated_char = rotated_char.upper() if is_upper else rotated_char

            result.append(rotated_char)
        else:
            result.append(char)

    return ''.join(result)
