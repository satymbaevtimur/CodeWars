def permutations(s):
    if len(s) == 1:
        return [s]
    
    unique_permutations = set()

    for i in range(len(s)):
        smaller_string = s[:i] + s[i+1:]
        
        smaller_permutations = permutations(smaller_string)
        
        for perm in smaller_permutations:
            unique_permutations.add(s[i] + perm)

    return list(unique_permutations)
