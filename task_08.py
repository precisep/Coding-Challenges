def time_conversion(minutes):
    hours = minutes // 60
    minutes = minutes % 60

    if hours == 1:
        hour_str = "hour"
    else:
        hour_str = "hours"

    if minutes == 1:
        minute_str = "minute"
    else:
        minute_str = "minutes"

    if hours == 0:
        hour_str = "hour"
    if minutes == 0:
        minute_str = "minute"
    

    return f"{hours} {hour_str}, {minutes} {minute_str}"
   


if __name__ == "__main__":
    print(time_conversion(71))
    print(time_conversion(133))
    print(time_conversion(0))
    print(time_conversion(0.5))
