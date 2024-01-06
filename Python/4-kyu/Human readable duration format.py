def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    time_units = {
        'year': 365 * 24 * 60 * 60,
        'day': 24 * 60 * 60,
        'hour': 60 * 60,
        'minute': 60,
        'second': 1
    }
    
    result = []
    
    for unit, value in time_units.items():
        if seconds >= value:
            count = seconds // value
            seconds %= value
            if count > 1:
                unit += 's'
            result.append(f"{count} {unit}")
    
    if len(result) > 1:
        return ', '.join(result[:-1]) + ' and ' + result[-1]
    else:
        return result[0]
