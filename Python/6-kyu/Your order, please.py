def order(sentence):
    if not sentence:
        return ""

    words = sentence.split()
    sorted_words = sorted(words, key=lambda word: int(''.join(filter(str.isdigit, word))))
    
    return ' '.join(sorted_words)v
