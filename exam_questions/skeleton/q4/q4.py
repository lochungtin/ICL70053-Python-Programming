# def convert(seconds):
#     hour = seconds // 3600
#     mins = (seconds % 3600) // 60
#     secs = seconds % 60

#     return (hour, mins, secs)


def convert(seconds):
    return seconds // 3600, (seconds % 3600) // 60, seconds % 60
