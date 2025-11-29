import turtle 

t = turtle.Turtle()
t.speed(10)

tc=['red', 'blue', 'yellow', 'green', 'purple', 'pink']
t.color(tc[0])

def pg(n,d):
    for i in range (n):
        t.forward (d)
        t.right (360/n)def tmowing (x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

for i in range (12):
    pg(4,30)
    t.right (30)
    
tmowing(100,70)
t.color(tc[1])

for i in range (12):
    pg(4,30)
    t.right (30)

tmowing(-100,-50)
t.color(tc[2])

angle=60
turn=360/angle

for i in range (turn):
    pg(4,60)
    t.right (angle)
    
turtle.done()
