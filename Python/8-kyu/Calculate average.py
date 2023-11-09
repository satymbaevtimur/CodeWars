def find_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)
