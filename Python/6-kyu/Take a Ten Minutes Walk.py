def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    direction_counts = {
        'n': walk.count('n'),
        's': walk.count('s'),
        'e': walk.count('e'),
        'w': walk.count('w')
    }
    
    return direction_counts['n'] == direction_counts['s'] and direction_counts['e'] == direction_counts['w']
