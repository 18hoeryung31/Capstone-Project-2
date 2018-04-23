# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import os
import turtle
import time
import random
import math
import pickle
import platform
#Set up screen
wn = turtle.Screen()
wn.bgcolor("lightblue")


class Window(spgl.Sprite):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("Black")
		self.goto(-290, 310)
		self.score = 0 
		self.time = 30
		
	

		
class Border(spgl.Sprite):
	
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.color("white")
		self.pensize(5)
		self.width = 600
		self.height = 600
		
	def draw_border(self):
		self.penup()
		self.goto(-self.width/2, -self.height/2)
		self.pendown()
		self.goto(-self.width/2, self.height/2)
		self.goto(self.width/2, self.height/2)
		self.goto(self.width/2, -self.height/2)
		self.goto(-self.width/2, -self.height/2)
		
		
# Create Functions

# Initial Game setup
game = spgl.Game(850, 850, "light blue", "Collect balloons to fly to South American Wilderness!", 0)
game.score = 0
game.current_time = 30

# Create Sprites
	# Keep List of Sprites
sprites = []
class Russell(spgl.Sprite):
	def __init__(self,shape,color,x,y):
		spgl.Sprite.__init__(self,shape,color,x,y)
		self.penup()
		self.shape("up.gif")
		self.goto(0, 0)
		self.speed = 10
		self.direction = "stop"

	def moveleft(self):
		self.direction = "left"

	def moveright(self):
		self.direction = "right"
		
	def moveup(self):
		self.direction = "up"

	def movedown(self):
		self.direction = "down"
	
	def tick(self):
			
		if self.xcor() > ((border.width/2) - 10):
			self.direction = "left"
		if self.xcor() < (-(border.width/2) + 10):
			self.direction = "right"
		if self.ycor() > ((border.width/2) - 10):
			self.direction = "down"
		if self.ycor() < (-(border.width/2) + 10):
			self.direction = "up"
	
	
		if self.direction == "right":
			self.goto(self.xcor() + self.speed, self.ycor())
		if self.direction == "left":
			self.goto(self.xcor() - self.speed, self.ycor())
		if self.direction == "up":
			self.goto(self.xcor(), self.ycor() + self.speed)
		if self.direction == "down":
			self.goto(self.xcor(), self.ycor() - self.speed)
		
		
class Balloon(spgl.Sprite):
	def __init__(self,shape,color,x,y):
		spgl.Sprite.__init__(self,shape,color,x,y)
		self.penup()
		self.shape("balloon.gif")
		self.speed = 6
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
	
	def jump(self):
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
		
			
	
	def tick(self):
		self.forward(self.speed)

		if self.xcor() > ((border.width/2) - 10):
			self.lt(60)
		
		elif self.xcor() < (-(border.width/2) + 10):
			self.lt(60)
		elif self.ycor() > ((border.width/2) - 10):
			self.lt(60)
		elif self.ycor() < (-(border.width/2) + 10):
			self.lt(60)
	
		
class Bird(spgl.Sprite):
	
	def __init__(self,shape,color,x,y):
		spgl.Sprite.__init__(self,shape,color,x,y)
		self.penup()
		self.shape("bird.gif")
		self.speed = 9
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
	
	def jump(self):
		self.goto(random.randint(-240, 240), random.randint(-240, 240))
		self.setheading(random.randint(0,360))
		

			
	
	def tick(self):
		self.forward(self.speed)
	
			
		if self.xcor() > ((border.width/2) - 10):
			self.lt(60)
		elif self.xcor() < (-(border.width/2) + 10):
			self.lt(60)
		elif self.ycor() > ((border.width/2) - 10):
			self.lt(60)
		elif self.ycor() < (-(border.width/2) + 10):
			self.lt(60)
	
	

def update_screen(self):
        while time.time(30) < self.time + (1.0 / self.FPS):
            pass
        turtle.update()
        self.time = time.time()
        
def isCollision(t1, t2):
	a = t1.xcor()-t2.xcor()
	b = t1.ycor()-t2.ycor() 
	distance = math.sqrt((a ** 2) + (b ** 2))
	
	if distance < 20:
		return True 
	else:
		return False 
		
# Instance
window = Window()
russell = Russell("up.gif", "white", 0,0)
balloon = Balloon("balloon.gif", "white", -250,-250)
bird = Bird("bird.gif", "white", -250,-250)
border = Border()
border.draw_border()
	
balloons = []
for count in range(8):
	balloons.append(Balloon("circle", "green", random.randint(-250, 250), random.randint(-250, 250)))

birds = []
for count in range(5):
	birds.append(Bird("square", "pink", random.randint(-250, 250), random.randint(-250, 250)))
	
	
# Create Labels
# Keep List of Labels

score_label = spgl.Label("Score: 0", "white", -300, 300)
score_label.set_font_size(24)
time_label = spgl.Label("Time: 30", "white",300,-300)
time_label.set_font_size(24)

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, russell.moveup)
game.set_keyboard_binding(spgl.KEY_DOWN, russell.movedown)
game.set_keyboard_binding(spgl.KEY_LEFT, russell.moveleft)
game.set_keyboard_binding(spgl.KEY_RIGHT, russell.moveright)




while True:
	# Call the game tick method
	game.tick()
	game.current_time -= 1
	time_label.update("Time: {}".format(game.current_time))
	
	for balloon in balloons:	
		if isCollision(russell, balloon):
			balloon.jump()
			game.score += 10
			score_label.update("Score: {}".format(game.score))
			if game.score == 100:
				print ("You won!")
				exit()
				
	for bird in birds:			
		if isCollision(russell, bird):
			bird.jump()
			score_label.update("Score: {}".format(game.score))
			border.clear()
			border.width -= 100
			border.height -= 100
			border.draw_border()
			
			if border.width == 100 and border.height == 100:
				print ("The end")
				exit()
			
		
	
	
