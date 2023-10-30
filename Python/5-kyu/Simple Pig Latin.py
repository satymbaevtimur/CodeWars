def pig_it(text):
    words = text.split()
    
    modified_words = []
    
    for word in words:
        if word.isalpha():
            modified_word = word[1:] + word[0] + 'ay'
            modified_words.append(modified_word)
        else:
            modified_words.append(word)

    modified_text = ' '.join(modified_words)
    
    return modified_text
