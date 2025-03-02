degrees = float(input())
hours = degrees / 30
minutes = (hours - float(int(hours))) * 60
print(int(hours), int(minutes))