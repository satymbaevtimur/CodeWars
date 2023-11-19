def series_sum(n):
    if n == 0:
        return "0.00"
    
    series_sum_result = 0
    for i in range(n):
        series_sum_result += 1 / (1 + i * 3)

    return "{:.2f}".format(series_sum_result)
