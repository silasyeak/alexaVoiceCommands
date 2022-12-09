import pyttsx3
import pygame
import button
from sys import exit

engine = pyttsx3.init()  
##volume = engine.getProperty('volume')
##engine.setProperty('volume', volume+1.5)
##rate = engine.getProperty('rate')
##engine.setProperty('rate', rate-20)
##voices = engine.getProperty('voices')
##engine.setProperty('voice', voices[2].id) ##2 works well


##functions for buttons
def click1():
	engine.say('Alexa, lights')
	engine.runAndWait()

def click2():
	engine.say('Alexa, lights off')
	engine.runAndWait()

def click3():
	engine.say('Alexa, turn on fancy')
	engine.runAndWait()

def click4():
	engine.say('Alexa, turn off fancy')
	engine.runAndWait()

def click5():
	engine.say('Alexa, turn on Desk')
	engine.runAndWait()

def click6():
	engine.say('Alexa, turn off Desk')
	engine.runAndWait()
def click7():
	engine.say('Alexa, turn on strip')
	engine.runAndWait()

def click8():
	engine.say('Alexa, turn off strip')
	engine.runAndWait()

def click9():
	engine.say('Alexa, turn on lamp')
	engine.runAndWait()

def click10():
	engine.say('Alexa, turn off lamp')
	engine.runAndWait()
def quit_game():
		pygame.quit()
		exit()


#create display window
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 320

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Anush Hakobyan')

#load button images
Lights_On = pygame.image.load('Lights_On.png').convert_alpha()
Lights_Off = pygame.image.load('Lights_Off.png').convert_alpha()
Fancy_On = pygame.image.load('Fancy_On.png').convert_alpha()
Fancy_Off = pygame.image.load('Fancy_Off.png').convert_alpha()
Desk_On = pygame.image.load('Desk_On.png').convert_alpha()
Desk_Off = pygame.image.load('Desk_Off.png').convert_alpha()
Strip_On = pygame.image.load('Strip_On.png').convert_alpha()
Strip_Off = pygame.image.load('Strip_Off.png').convert_alpha()
Lamp_On = pygame.image.load('Lamp_On.png').convert_alpha()
Lamp_Off = pygame.image.load('Lamp_Off.png').convert_alpha()
Quit_Program = pygame.image.load('Quit.png').convert_alpha()

#create button instances
##80 is one down
##160 is one right
y = 80
x = 160

button_1 = button.Button(0, 0, Lights_On, 0.8)
button_2 = button.Button(x, 0, Lights_Off, 0.8)
button_3 = button.Button(0, y, Fancy_On, 0.8)
button_4 = button.Button(x, y, Fancy_Off, 0.8)
button_5 = button.Button(0, 2*y, Desk_On, 0.8)
button_6 = button.Button(x, 2*y, Desk_Off, 0.8)
button_7 = button.Button(0, 3*y, Strip_On, 0.8)
button_8 = button.Button(x, 3*y, Strip_Off, 0.8)
button_9 = button.Button(0, 4*y, Lamp_On, 0.8)
button_10 = button.Button(x, 4*y, Lamp_Off, 0.8)
quit_button = button.Button(0, 5*y, Quit_Program, 0.8)


#game loop
run = True
while run:
		
		##background color
	screen.fill((0, 0, 0))

	if button_1.draw(screen):
			click1()
	if button_2.draw(screen):
			click2()
	if button_3.draw(screen):
			click3()
	if button_4.draw(screen):
			click4()
	if button_5.draw(screen):
			click5()
	if button_6.draw(screen):
			click6()
	if button_7.draw(screen):
			click7()
	if button_8.draw(screen):
			click8()
	if button_9.draw(screen):
			click9()
	if button_10.draw(screen):
			click10()
	if quit_button.draw(screen):
			quit_game()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.display.update()





