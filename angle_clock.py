# LC 1344 ANGLE BETWEEN HANDS OF A CLOCK
def angle_clock(hour, minutes):
    if hour == 12:
        hour = 0
    m = minutes * 6
    h = hour * 30 + minutes / 2
    return min(abs(m - h), 360 - abs(m - h))
