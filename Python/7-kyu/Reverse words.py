def reverse_words(text):
    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    result = " ".join(reversed_words)
    return result
