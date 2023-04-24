def time_conversion(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    
    if hours == 1:
        hour_str = "hour"  
    else :
        hour_str = "hours"

    if minutes == 1: 
        minute_str = "minute" 
    else:
        
        minute_str = "minutes"
    
    if hours > 0:
        return f"{hours} {hour_str}, {minutes} {minute_str}"
    else:
        return f"{minutes} {minute_str}"

