def high_and_low(numbers):
    number_list = [int(num) for num in numbers.split()]
    
    highest = max(number_list)
    lowest = min(number_list)
    
    return f"{highest} {lowest}"
