def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():
            position = ord(char.lower()) - ord('a') + 1
            result.append(str(position))
    
    return ' '.join(result)
