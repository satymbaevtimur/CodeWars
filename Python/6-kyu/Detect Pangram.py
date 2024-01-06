def is_pangram(s):
    s_cleaned = ''.join(char.lower() for char in s if char.isalpha())
    
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s_cleaned))
