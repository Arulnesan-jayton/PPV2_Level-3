import turtle as t
def rectangle(horizontal,verticl,color):
  t.pendown()
  t.pensize(1)
  t.color(color)
  t.begin_fill()
  for counter in range (1,3):
    t.forward(horizontal)
    t.right(90)
    t.forward(verticl)
    t.right(90)
  t.end_fill()
  t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

#feet
t.goto(-100,-150)
rectangle(50,20,'seashell')
t.goto(-30,-150)
rectangle(50,20,'seashell')

#legs
t.goto(-25,-50)
rectangle(15,100,'goldenrod')
t.goto(-55,-50)
rectangle(-15,100,'goldenrod')

#body
t.goto(-90,100)
rectangle(100,150,'goldenrod')

#arms
t.goto(-150, 70)
rectangle(60,15,'goldenrod')
t.goto(-150, 110)
rectangle(15,40,'seashell')

t.goto(10, 70)
rectangle(60,15,'goldenrod')
t.goto(55, 110)
rectangle(15,40,'seashell')

#neck
t.goto(-50,120)
rectangle(15,20,'seashell')

#head
t.goto(-85,170)
rectangle (80,50,'seashell')

#eyes
t.goto(-60,160)
rectangle(30,10,'white')
t.goto(-55,155)
rectangle(5,5,'black')
t.goto(-40,155)
rectangle(5,5,'black')

#mouth
t.goto(-65,135)
t.right(0)
rectangle(40,5,'black')

t.hideturtle()



