import pygame
import time

pygame.init()										#Init library

#constant init
display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
car_width = 73


gameDisplay = pygame.display.set_mode((display_width, display_height))	#Create canvas
pygame.display.set_caption('A bit racey')			#Set window title

clock = pygame.time.Clock() 						#Game clock is tied to framerate?
crashed = False
carImg = pygame.image.load('racecar.png')

def car(x,y):
	gameDisplay.blit(carImg, (x,y))					#draws the png to the screen

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 72) #font name and size in pt.
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

def crash():
	message_display('Now You Fucked Up...')
	time.sleep(10)
	game_loop()

def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x_change = 0
	car_speed = 0
	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:			#When a key is pressed, move car left/right accordingly
				if event.key == pygame.K_LEFT:
					x_change -= 5
				if event.key ==  pygame.K_RIGHT:
					x_change += 5
			if event.type == pygame.KEYUP:				#When a key is depressed, give it antidepressants
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change

		gameDisplay.fill(white)
		car(x,y)

		if x > display_width - car_width or x < 0:
			x_change = 0
			crash()

		pygame.display.update()
		clock.tick(60)


game_loop()
pygame.quit()
quit()
