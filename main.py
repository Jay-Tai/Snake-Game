#imports
import turtle
import random
import time

#setting up point counter variable
counter=0

#setting up screen
wn=turtle.Screen()
wn.bgcolor("green")
wn.title("awshum schnaek gaem!1!!11!!")
wn.setup(width=500,height=500)
wn.tracer(0)

#snake head
head=turtle.Turtle()
head.shape("square")
head.color("blue")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction="stop"

#apple definition
apple=turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.speed(0)
apple.penup()
apple.goto(100,100)

#segment list
segments=[]

#Snake movement
def move():
  if head.direction=="up":
    y=head.ycor()
    head.sety(y+20)
  if head.direction=="down":
    y=head.ycor()
    head.sety(y-20)
  if head.direction=="left":
    x=head.xcor()
    head.setx(x-20)
  if head.direction=="right":
    x=head.xcor()
    head.setx(x+20)

#Changing head.direction
def goUp():
  head.direction="up"
  
def goDown():
  head.direction="down"

def goLeft():
  head.direction="left"

def goRight():
  head.direction="right"

wn.listen()
wn.onkeypress(goUp,"Up")
wn.onkeypress(goDown,"Down")
wn.onkeypress(goLeft,"Left")
wn.onkeypress(goRight,"Right")
wn.onkeypress(goUp,"w")
while True:
  wn.update()
  if head.xcor()>235 or head.xcor()<-235 or head.ycor()>235 or head.ycor()<-235:
    time.sleep(1)
    head.goto(0,0)
    head.direction="stop"
    head.goto(1000000000000000,1000000000000000)
    for segment in segments:
      segment.goto(1000000,1000000)
    segments.clear()
  if head.distance(apple)<20:
    #Changing position of the apple
    apple.goto(random.randint(-230,230),random.randint(-230,230))
    new_segment=turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    segments.append(new_segment)
  for index in range(len(segments) -1,0,-1):
    x=segments[index -1].xcor()
    y=segments[index -1].ycor()
    segments[index].goto(x,y)
  if len(segments)>0:
    x=head.xcor()
    y=head.ycor()
    segments[0].goto(x,y)
  move()
  time.sleep(0.1)
  
#main loop
wn.mainloop()