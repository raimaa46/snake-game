import turtle
import time
import random

delay=0.1
#score
score=0
high_score=0

wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)#turns off the screen update
#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"
#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High Sore:0", align="center", font=("courier",20,"normal"))

def go_up():
    if (head.direction!="down"):
       head.direction="up"
def go_down():
    if (head.direction!="up"):
        head.direction="down"
def go_left():
    if (head.direction!="right"):
       head.direction="left"
def go_right():
    if (head.direction!="left"):
        head.direction="right"

#functions
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
#keyword
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
#main game loop
while True:
    wn.update()
    #check for a collison with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        #head the  segments
        for segment in segments:
            segment.goto(1000,1000)
        #clear the segment list
        segments.clear()
        #reset score
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score:{}  High Score:{} ".format(score,high_score),align="center" , font=("courier",20,"normal"))
    #check for collison with food
    if head.distance(food)<20:
        #move to a random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        #shorten delay
        delay-=0.001
        #increase score
        score=score+10
        if  score>high_score:
                high_score=score
        pen.clear()
        pen.write("Score:{} High Score:{} ".format(score,high_score),align="center" , font=("courier",20,"normal"))
        #move the end segment first
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if(len(segments)>0):
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    #check for head collison with body
    for segment in segments:
        if(segment.distance(head)<20):
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
        #head segments
            for segment in segments:
                segment.goto(1000,1000)
                #clear segments:
            segments.clear()
            #reset score
            score=0
            #reset delay
            delay=0.1
            pen.clear()
            pen.write("Score:{} High Score:{} ".format(score,high_score),align="center" , font=("courier",20,"normal"))
    time.sleep(delay)
wn.mainloop()