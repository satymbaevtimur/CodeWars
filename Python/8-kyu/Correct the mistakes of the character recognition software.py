def correct(text):
    corrected_text = text.replace('5', 'S').replace('0', 'O').replace('1', 'I')
    return corrected_text
