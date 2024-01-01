def to_jaden_case(string):
    words = string.split()
    jaden_cased_words = [word.capitalize() for word in words]

    jaden_cased_string = ' '.join(jaden_cased_words)

    return jaden_cased_string
