def time_conversion(minutes):
    hours = minutes // 60
    minutes = minutes % 60

    hour_str = "hour" if hours == 1 else "hours"
    minute_str = "minute" if minutes == 1 else "minutes"

    hour_str = "hour" if hours == 0 else hour_str
    minute_str = "minute" if minutes == 0 else minute_str

    return f"{hours} {hour_str}, {minutes} {minute_str}"
   


if __name__ == "__main__":
    print(time_conversion(71))
    print(time_conversion(133))
    print(time_conversion(0))
    print(time_conversion(0.5))
