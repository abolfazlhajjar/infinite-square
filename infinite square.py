import turtle

turtle.speed(0)
turtle.bgcolor('black')
turtle.hideturtle()
r, g, b = 255, 0, 0

for x in range(255*2):
    turtle.colormode(255)

    if x < 255//3:
        g += 3
    elif x < (255*2)//3:
        r -= 3
    elif x < 255:
        b += 3
    elif x < (255*4)//3:
        g -= 3
    elif x < (255*5)//3:
        r += 3
    else:
        b -= 3

    turtle.fd(50+x)
    turtle.rt(90)
    turtle.pencolor (r, g, b)
