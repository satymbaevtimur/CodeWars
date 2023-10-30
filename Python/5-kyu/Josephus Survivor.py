def josephus_survivor(n, k):
    if n == 1:
        return 1
    
    position = 0 
    for i in range(2, n + 1):
        position = (position + k) % i
c
    return position + 1
