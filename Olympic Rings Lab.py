import turtle
olympic = turtle.Turtle()
olympic.penup() # hide the pen for move
olympic.pensize(7) # play with this it determines the outline width
olympic.color("aqua")
olympic.goto(-200,100) # center of the circle is 100,100
olympic.pendown() # get ready to draw
olympic.circle(50) # radius of the circle is 20
olympic.penup()
olympic.goto(-140,50)
olympic.pendown()
olympic.color('gold')
olympic.circle(50)
olympic.penup()
olympic.goto(-80,100)
olympic.color('black')
olympic.pendown()
olympic.circle(50)
olympic.penup()
olympic.goto(-20,50)
olympic.pendown()
olympic.color('green')
olympic.circle(50)
olympic.penup()
olympic.goto(40,100)
olympic.pendown()
olympic.color('red')
olympic.circle(50)

turtle.done() # this keeps the screen up until you close it
