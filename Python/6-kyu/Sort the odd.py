def sort_array(source_array):
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])
    sorted_array = [num if num % 2 == 0 else odd_numbers.pop(0) for num in source_array]
    return sorted_array
