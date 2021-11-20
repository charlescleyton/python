from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%d/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%H:%M:%S"))


