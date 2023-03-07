n = int(input("Введите число - "))
def convert(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60

    return "%d:%02d:%02d" % (hour, min, sec)


print(convert(n))