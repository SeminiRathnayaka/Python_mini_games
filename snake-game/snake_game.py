# Simple snake game 
# by Orayan


import turtle 
import time
import random
delay = 0.2

# Score
score = 0
high_score = 0

# Set up the screen 
window=turtle.Screen()
window.title("Snake game by @Orayan")
window.bgcolor("green")
window.setup(width =600,height=600)
window.tracer(0) # Turn off the screen update

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "right"

# Snake food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write ("Score: 0  High Score: 0",align ="center",font=("Curier",24,"normal"))


# Functions
def go_up():
    head.direction !="down"
    head.direction = "up"

def go_down():
    head.direction !="up" 
    head.direction ="down"

def go_left():
    head.direction !="right"
    head.direction ="left"

def go_right():
    head.direction !="left"
    head.direction ="right"     

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y + 20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y - 20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x - 20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x + 20)

# Keyboard bindings
window.listen()
window.onkey(go_up,"Up")
window.onkey(go_down,"Down")
window.onkey(go_left,"Left")
window.onkey(go_right,"Right")

# Main game loop
while True:
    window.update()

# Check for collosion with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
      time.sleep(1)
      head.goto(0,0)
      head.direction ="stop"

      # Hide the segments 
      for segment in segments:  
          segment.goto(1000,1000)  

      # Clear the segment list 
      segments.clear() 

      # Reset the score 
      score = 0

      # Rest the delay
      score=0.1

      pen.clear()
      pen.write("Score:{} High score:{}".format(score,high_score),align="center",font=("Curier",24,"normal"))     
       
             
# Check for a collision with the food 

    if head.distance(food)<20 :
        # Move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # Shrten the delay
        delay-=0.001

        # Increase the score 
        score += 10

        if  score >high_score:
            high_score=score 
        pen.clear()
        pen.write("Score:{} High score:{}".format(score,high_score),align="center",font=("Curier",24,"normal"))     

# Move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):   
         x=segments[index-1].xcor()
         y=segments[index-1].ycor()
         segments[index].goto(x,y)

# Move the segment 0 to whre the head is 
    if len(segments)>0:
         x=head.xcor()
         y=head.ycor()
         segments[0].goto(x,y)
    
        

    move()

    # Check for head collosion with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments :
                segment.goto(1000,1000)

            # Clear the segment list
            segment.clear() 

            # Reset the score 
            score = 0

            # Reset the delay
            delay=0.1

            pen.clear()
            pen.write("Score:{} High score:{}".format(score,high_score),align="center",font=("Curier",24,"normal"))  

    time.sleep(delay)







window.mainloop()