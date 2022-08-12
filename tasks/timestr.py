__all__ = (
    'seconds_to_str',
)

def cap(num):
    if len(num) == 1:
        return ('0'+num)
    return num


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    res = ""
    if seconds // 86400 >=1:
        day = seconds // 86400
        hour = (seconds - day*86400) // 3600
        min = (seconds - day*86400 - hour*3600) // 60
        sec = (seconds//60) % 60
        return res+cap(str(day))+'d'+cap(str(hour))+'h'+cap(str(min))+'m'+cap(str(sec))+'s'

    if seconds // 3600 >= 1:
        hour = seconds // 3600
        min = (seconds - hour*3600) // 60
        sec = seconds % 60
        return res+cap(str(hour))+'h'+cap(str(min))+'m'+cap(str(sec))+'s'

    if seconds // 60 >= 1:
        min = seconds//60
        sec = seconds % 60
        return res+cap(str(min))+'m'+cap(str(sec))+'s'
    return res+cap(str(seconds))+'s'


a=864000
print(seconds_to_str(a))

