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
wn.title("Game")
wn.register_shape("balloon.gif")
wn.register_shape("bird.gif")
wn.register_shape("up.gif")
# Create Classes
class Game(object):
	def __init__(
				self,
				screen_width = 700,
				screen_height = 700,
				background_color = "lightblue",
				title = "Collect balloons to fly to South American Wilderness!",
				splash_time = 3):

        # Setup using Turtle module methods
		turtle.setup(width=screen_width, height=screen_height)
		turtle.bgcolor("white")
		turtle.title(title)
		turtle.tracer(0) # Stop automatic screen refresh
		turtle.listen() # Listen for keyboard input
		turtle.hideturtle() # Hides default turtle
		turtle.penup() # Puts pen up for defaut turtle
		turtle.setundobuffer(0) # Do not keep turtle history in memory
		turtle.onscreenclick(self.click)

class Border(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("white")
		self.pensize(5)
	
	def draw_border(self):
		self.penup()
		self.goto(-300, -300)
		self.pendown()
		self.goto(-300, 300)
		self.goto(300, 300)
		self.goto(300, -300)
		self.goto(-300, -300)
# Create Functions

# Initial Game setup
game = spgl.Game(800, 800, "light blue", "Collect balloons to fly to South American Wilderness!")

# Create Sprites
	# Keep List of Sprites
sprites = []
class Russell(spgl.Sprite):
	def __init__(self,shape,color,x,y):
		spgl.Sprite.__init__(self,shape,color,x,y)
		self.penup()
		self.shape("up.gif")
		self.goto(-290, 310)
		self.speed(0)
		self.speed = 5
		self.direction = "stop"
	def move(self):
		if self.direction == "left":
			self.goto(self.xcor() = self.speed, self.ycor())
		elif self.direction == "left":
			self.goto(self.xcor(), self.speed + self.ycor())
		
		elif self.direction == "up":
			self.goto(self.xcor(), self.ycor() + self.speed)
		
		elif self.direction == "down":
			self.goto(self.xcor(), self.ycor() - self.speed)
		else:
			self.goto(self.xcor(), self.ycor())
			
	def moveleft(self):
		self.direction = "left"

	def moveright(self):
		self.direction = "right"
		
	def moveup(self):
		self.direction = "up"

	def movedown(self):
		self.direction = "down"
	
	def move(self):
		self.forward(self.speed)
			
		if self.xcor() > 290 or self.xcor() < -290:
			self.left(60)
		if self.ycor() > 290 or self.ycor() < -290:
			self.left(60)
			
class Balloons(spgl.Sprite):
	def __init__(self,shape,color,x,y):
		spgl.Sprite.__init__(self,shape,color,x,y)
		self.penup()
		self.shape("balloon.gif")
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
	
	def jump(self):
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
		
	def move(self):
		self.forward(self.speed)
		
		#Border Checking
		if self.xcor() > 290 or self.xcor() < -290:
			self.left(60)
		if self.ycor() > 290 or self.ycor() < -290:
			self.left(60)

class Bird(spgl.Sprite):
	
	def __init__(self,shape,color,x,y):
		spgl.Sprite.__init__(self,shape,color,x,y)
		self.penup()
	
		self.shape("bird.gif")
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
	
	def jump(self):
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
		
	def move(self):
		self.forward(self.speed)
		
		#Border Checking
		if self.xcor() > 290 or self.xcor() < -290:
			self.left(60)
		if self.ycor() > 290 or self.ycor() < -290:
			self.left(60)

# Instance
russell = Russell("square", "white", -290,-290)
balloons = Balloons("square", "white", -250,-250)
bird = Bird("square", "white", -250,-250)

# Create Labels
	# Keep List of Labels
labels = []
# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, russell.moveup)
game.set_keyboard_binding(spgl.KEY_DOWN, russell.movedown)
game.set_keyboard_binding(spgl.KEY_LEFT, russell.moveleft)
game.set_keyboard_binding(spgl.KEY_RIGHT, russell.moveright)

while True:
    # Call the game tick method
    game.tick()
