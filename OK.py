import turtle, math,colorsys
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800,800)
turtle.tracer(5,0)
t=turtle.Turtle()
t.speed(0);t.hideturtle()
h=0
for i in range(0,360,3):
    r,g,b=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(r,g,b);t.width(1)
    rad=math.radians(i)
    cx=80*math.cos(rad)
    cy=80*math.sin(rad)
    t.penup()
    first=True
    for j in range(0,361,2):
        jrad=math.radians(j)
        x=cx+250*math.cos(jrad)
        y=cy+250*math.sin(jrad)
        if first:
            t.goto(x,y);t.pendown();first=False
        else:
            t.goto(x,y)
    h=(h+0.008)%1
turtle.update()
turtle.done()