def knight(p1, p2):
    moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    
    def algebraic_to_coordinates(pos):
        return (ord(pos[0]) - ord('a'), int(pos[1]) - 1)
    
    start = algebraic_to_coordinates(p1)
    end = algebraic_to_coordinates(p2)

    queue = [(start, 0)]
    visited = set()

    while queue:
        current, steps = queue.pop(0)
        
        if current == end:
            return steps
        
        if current not in visited:
            visited.add(current)
            
            for move in moves:
                new_x = current[0] + move[0]
                new_y = current[1] + move[1]
                new_pos = (new_x, new_y)
                
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    queue.append((new_pos, steps + 1))
    
    return None
