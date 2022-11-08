import turtle
t = turtle.Turtle()
s = turtle.screen()
s.bgcolor('black')
t.pencolor('red')
t.speed(0)

form i in range (150):
    t.circle(190-i,90)
    t.\t(90)
    t.circle(190-i,90)
    t.\t(18)