# Testing git
import pygame
from pygame.locals import *

WIDTH = 200
HEIGHT = 400

# Modules will assume that pygame has been initialised,
# therefore they are imported after pygame.init()
pygame.init()
import slide

pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.get_surface()

test_image = pygame.image.load("bliss.jpg")
test_image = pygame.transform.scale(test_image, (150,250))

slide.init(WIDTH, HEIGHT)
s.start_slide(1, 3)

while True:

	screen.fill(BACKGROUND_COLOUR)
	s.draw_slide(screen)
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			for box in s.text_boxes:
				if box.button_func is None:
					continue
				if event.pos[0] >= box.x and event.pos[0] <= box.x+box.width and\
						event.pos[1] >= box.y and event.pos[1] <= box.y+box.height:
					box.button_func(slide.curr_slide)
		if event.type == QUIT:
			break
	else:
		continue
	break

pygame.quit()
