import math as math
blind_zone = int(input())
reception_radius = int(input())
print(abs(math.pi*reception_radius**2 - math.pi*blind_zone**2   ))