import pygame
from pygame.locals import *

# Modules will assume that pygame has been initialised,
# therefore they are imported after pygame.init()
pygame.init()
from slide import WIDTH, HEIGHT, key_bindings
pygame.display.set_mode((WIDTH, HEIGHT))

import parse
import slide

from data import slideshow, BACKGROUND_COLOUR
screen = pygame.display.get_surface()

test_image = pygame.image.load("bliss.jpg")
test_image = pygame.transform.scale(test_image, (150,250))

slideshow.start_slide()

while True:
	screen.fill(BACKGROUND_COLOUR)
	slideshow.draw(screen)
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			for box in slideshow.current_slide.text_boxes:
				if box.button_func is None:
					continue
				if event.pos[0] >= box.x and event.pos[0] <= box.x+box.width and\
						event.pos[1] >= box.y and event.pos[1] <= box.y+box.height:
					box.button_func(slideshow)
		if event.type == KEYDOWN and event.key in key_bindings:
			key_bindings[event.key](slideshow)
		if event.type == QUIT:
			break
	else:
		continue
	break

pygame.quit()
