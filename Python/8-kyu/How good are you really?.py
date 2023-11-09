def better_than_average(class_points, your_points):
    total_points = sum(class_points) + your_points
    average = total_points / (len(class_points) + 1)
    
    return your_points > average
