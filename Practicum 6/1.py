carpet = input().split('x')
if (float(carpet[0])**2 + float(carpet[1])**2) ** 0.5 > 13:
    print("нет")
else:
    print("да")