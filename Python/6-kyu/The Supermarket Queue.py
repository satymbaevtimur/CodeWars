def queue_time(customers, n):
    tills = [0] * n
    
    for customer in customers:
        min_till = min(tills)
        
        tills[tills.index(min_till)] += customer
    
    return max(tills)
