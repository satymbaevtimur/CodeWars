def duplicate_encode(word):
    word = word.lower()
    
    char_freq = {}
    for char in word:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    result = ''
    for char in word:
        if char_freq[char] > 1:
            result += ')'
        else:
            result += '('
    
    return result
