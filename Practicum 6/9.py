import turtle
import math
def draw_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)
def circle_relation(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance > r1 + r2:
        return "Окружности лежат одна вне другой, не касаясь"
    elif distance == r1 + r2:
        return "Окружности имеют внешнее касание"
    elif distance < abs(r1 - r2):
        return "Одна окружность лежит внутри другой, не касаясь"
    elif distance == abs(r1 - r2):
        return "Окружности имеют внутреннее касание"
    else:
        return "Окружности пересекаются"
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
draw_circle(x1, y1, r1)
draw_circle(x2, y2, r2)
relation = circle_relation(x1, y1, r1, x2, y2, r2)
print(relation)
turtle.mainloop()