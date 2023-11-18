def bouncing_ball(h, bounce, window):
    if h <= 0 or not (0 < bounce < 1) or window >= h:
        return -1

    bounces_seen = 1
    
    while h * bounce > window:
        h *= bounce
        bounces_seen += 2

    return bounces_seen
