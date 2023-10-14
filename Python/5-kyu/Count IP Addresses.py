def ips_between(start, end):
    start_segments = list(map(int, start.split('.')))[::-1]
    end_segments = list(map(int, end.split('.')))[::-1]

    num_addresses = 0
    multiplier = 1

    for i in range(4):
        num_addresses += (end_segments[i] - start_segments[i]) * multiplier
        multiplier *= 256

    return num_addresses
