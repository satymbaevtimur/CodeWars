def is_palindrome(s):
    s = s.lower()
    
    s = ''.join(char for char in s if char.isalnum())
    
    return s == s[::-1]
