days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

out = 0
year = 1900
dayOfWeek = 0
for year in range(1901, 2000):
    for month in months:
            if year % 4 == 0 and year % 400 != 0 and month == 28:
                for i in range(0, 29):
                    if i == 0 and dayOfWeek == 6:
                        out += 1
                    dayOfWeek = (dayOfWeek+1) % 7
            else:
                for i in range(0, month):
                    if i == 0 and dayOfWeek == 6:
                        out += 1
                    dayOfWeek = (dayOfWeek+1) % 7

print(out)
