import turtle as trt
xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())
trt.penup()
trt.setpos(xc, yc)
trt.right(90)
trt.forward(r)
trt.left(90)
trt.pendown()
trt.begin_fill()
trt.circle(r)
trt.end_fill()
trt.penup()
trt.setpos(x, y)
trt.pendown()
trt.begin_fill()
trt.dot(10, "red")
trt.end_fill()
trt.penup()
trt.setpos(xc - r - 20, yc - r - 20)
trt.pendown()
if (xc - x) ** 2 + (yc - y) ** 2 > r ** 2:
    trt.write("точка вне окружности")
elif (xc - x) ** 2 + (yc - y) ** 2 == r ** 2:
    trt.write("точка на окружности")
else:
    trt.write("точка внутри окружности")
trt.mainloop()
