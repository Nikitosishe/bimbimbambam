import turtle

def draw_rectangle(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(x2 - x1)
        turtle.right(90)
        turtle.forward(y1 - y2)
        turtle.right(90)

def rectangles_relation(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x4 < x1 or y2 > y3 or y4 > y1:
        return "Прямоугольники лежат вне друг друга, не касаясь"
    elif x2 == x3 or x4 == x1 or y2 == y3 or y4 == y1:
        return "Прямоугольники имеют касание"
    elif x1 < x3 and x2 > x4 and y1 > y3 and y2 < y4:
        return "Один прямоугольник лежит внутри другого, не касаясь"
    else:
        return "Прямоугольники имеют пересечение"

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
draw_rectangle(x1, y1, x2, y2)
draw_rectangle(x3, y3, x4, y4)
relation = rectangles_relation(x1, y1, x2, y2, x3, y3, x4, y4)
print(relation)
turtle.mainloop()