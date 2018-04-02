# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
# Create Classes
class Russell(spgl.Sprite):
	def __init__(self):
		spgl.Sprite.__init__(self)
		self.penup()
		self.speed(0)
		self.shape(circle)
		self.speed(0)
		self.speed = 1
# Create Functions

# Initial Game setup
game = spgl.Game(600, 600, "light blue", "Collect balloons to fly to South American Wilderness!")

# Create Sprites

# Create Labels

# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
    game.tick()
