def in_array(a1, a2):
    result = set()
    
    for word1 in a1:
        for word2 in a2:
            if word1 in word2:
                result.add(word1)
                break
    
    return sorted(result)
