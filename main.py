# Testing git
import pygame
from pygame.locals import *

WIDTH = 200
HEIGHT = 400
BACKGROUND_COLOUR = (0, 0, 0)

# Modules will assume that pygame has been initialised, therefore they are imported after pygame.init()
pygame.init()
import slide

pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.get_surface()
screen.fill(BACKGROUND_COLOUR)

s = slide.TextSlide([slide.TextBox(20,20,150,200,"I like muffins and cheesecacke emacs is the best"), \
	slide.TextBox(20, 50, 150, 200, "LOLOL overlap lol hs1917")], \
	[slide.ImageBox(20, 100, "bliss.jpg", 150, 250)], \
	BACKGROUND_COLOUR)
s.draw_slide(screen)
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			break
	else:
		continue
	break

pygame.quit()