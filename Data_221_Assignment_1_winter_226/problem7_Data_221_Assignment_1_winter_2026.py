def time_conversion(seconds_since_midnight):
    if seconds_since_midnight < 0:
        return "negative number not countable"
    counter_of_hours = 0
    counter_of_minutes = 0
    while seconds_since_midnight >= 3600:
        seconds_since_midnight -= 3600
        counter_of_hours += 1
    while seconds_since_midnight >= 60:
        seconds_since_midnight -= 60
        counter_of_minutes += 1

    am_or_pm = ""
    if counter_of_hours%24 > 12:
        am_or_pm = "PM"
    elif counter_of_hours%24 < 12:
        am_or_pm = "AM"

    string_returned = f"{counter_of_hours} {counter_of_minutes} {seconds_since_midnight} {am_or_pm}"



    return string_returned

print(time_conversion(12233))