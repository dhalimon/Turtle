import turtle


def main():
  # put label on top of page
  turtle.title ('Hello World')

  # setup screen size
  turtle.setup (1000, 1000, 0, 0)
 
  # move turtle to origin
  turtle.penup()
  turtle.goto (0, 0)

  # set the color to navy
  turtle.color ('navy')

  # write the message
  turtle.write ('Hello Wassup!', font = ('Times New Roman', 36, 'bold'))

  # hide the turtle
  #turtle.hideturtle()

  # persist the drawing
  turtle.done()

main()
