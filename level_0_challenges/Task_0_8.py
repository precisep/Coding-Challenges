def time_conversion(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    
    
    hour_str = "hour" if hours == 1 else "hours"
    minute_str = "minute" if minutes == 1 else "minutes"
    
    if hours > 0:
        return f"{hours} {hour_str}, {minutes} {minute_str}"
    else:
        return f"{minutes} {minute_str}"

