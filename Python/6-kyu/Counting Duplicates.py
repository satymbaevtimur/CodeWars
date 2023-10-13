def duplicate_count(s):
    s = s.lower()
    char_count = {}
    count = 0

    for char in s:
        if char.isalnum():
            if char in char_count:
                char_count[char] += 1
                if char_count[char] == 2:
                    count += 1
            else:
                char_count[char] = 1

    return count
