def sum_array(arr):
    if arr is None or len(arr) == 0 or len(arr) == 1:
        return 0
    
    highest, lowest = max(arr), min(arr)
    return sum(arr) - highest - lowest 
