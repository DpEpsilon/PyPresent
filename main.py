import pygame
from pygame.locals import *

WIDTH = 200
HEIGHT = 400
BACKGROUND_COLOUR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Modules will assume that pygame has been initialised, therefore they are imported after pygame.init()
pygame.init()
import wrap 

pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.get_surface()
screen.fill(BACKGROUND_COLOUR)

wrap.render_text(screen, "dkn knn n skn dknf knskjfnkj k nkn kjdsnfkjnk kn ksnk ", TEXT_COLOR, BACKGROUND_COLOUR, 1)
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			break
	else:
		continue
	break

pygame.quit()