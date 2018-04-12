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

class Border(spgl.Sprite):
	
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.color("white")
		self.pensize(5)
		self.width = 700
		self.height = 700
		
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
game = spgl.Game(800, 800, "light blue", "Collect balloons to fly to South American Wilderness!", 0)

# Create Sprites
	# Keep List of Sprites
sprites = []
class Russell(spgl.Sprite):
	def __init__(self,shape,color,x,y):
		spgl.Sprite.__init__(self,shape,color,x,y)
		self.penup()
		self.shape("up.gif")
		self.goto(0, 0)
		self.speed = 8
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
			self.direction = "up"
		if self.ycor() < (-(border.width/2) + 10):
			self.direction = "down"
	
	
		if self.direction == "right":
			self.goto(self.xcor() + self.speed, self.ycor())
		if self.direction == "left":
			self.goto(self.xcor() - self.speed, self.ycor())
		if self.direction == "up":
			self.goto(self.ycor() + self.speed, self.xcor())
		if self.direction == "down":
			self.goto(self.ycor() - self.speed, self.xcor())
		
		
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
			self.direction = "left"
		elif self.xcor() < ((border.width/2) + 10):
			self.direction = "right"
		elif self.ycor() > ((border.width/2) - 10):
			self.direction = "up"
		elif self.ycor() < ((border.width/2) + 10):
			self.direction = "down"
	
		
class Bird(spgl.Sprite):
	
	def __init__(self,shape,color,x,y):
		spgl.Sprite.__init__(self,shape,color,x,y)
		self.penup()
		self.shape("bird.gif")
		self.speed = 9
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
	
	def jump(self):
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(random.randint(0,360))
		
	def tick(self):
		self.forward(self.speed)
		
		if self.xcor() > ((border.width/2) - 10):
			self.direction = "left"
		elif self.xcor() < ((border.width/2) + 10):
			self.direction = "right"
		elif self.ycor() > ((border.width/2) - 10):
			self.direction = "up"
		elif self.ycor() < ((border.width/2) + 10):
			self.direction = "down"
	

# Instance
russell = Russell("square", "white", 0,0)
balloon = Balloon("square", "white", -250,-250)
bird = Bird("square", "white", -250,-250)
border = Border()
border.draw_border()

# Create Labels
	# Keep List of Labels
balloons = []
for count in range(8):
	balloons.append(Balloon("circle", "green", random.randint(-250, 250), random.randint(-250, 250)))

bird = []
for count in range(3):
	bird.append(Bird("square", "pink", random.randint(-250, 250), random.randint(-250, 250)))
# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, russell.moveup)
game.set_keyboard_binding(spgl.KEY_DOWN, russell.movedown)
game.set_keyboard_binding(spgl.KEY_LEFT, russell.moveleft)
game.set_keyboard_binding(spgl.KEY_RIGHT, russell.moveright)




while True:
    # Call the game tick method
    game.tick()
