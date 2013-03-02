# Testing git
import pygame
from pygame.locals import *

WIDTH = 200
HEIGHT = 400
BACKGROUND_COLOUR = (0, 0, 0)

# Modules will assume that pygame has been initialised,
# therefore they are imported after pygame.init()
pygame.init()
import slide

pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.get_surface()

test_image = pygame.image.load("bliss.jpg")
test_image = pygame.transform.scale(test_image, (150,250))

def test_animation(screen_surf, position):
	if position < 0.5:
		screen_surf.blit(test_image, (0,0))
	else:
		screen_surf.blit(test_image, (5,5))

def test_func():
	global s
	s.text_boxes.append(slide.TextBox(20, 300, "WORKED", 150, back_colour=(0, 0, 0)))

#s = slide.TextSlide(\
#	[slide.TextBox(20, 20, "I like muffins and cheesecacke emacs is the best", 150),\
#		 slide.TextBox(20, 100, "LOLOL overlap lol hs1917",\
#						   150, back_colour=(255, 0, 0), button_func=test_func)], \
#		[slide.ImageBox(20, 100, "bliss.jpg", 150, 250)], BACKGROUND_COLOUR)


s = slide.AnimationSlide(test_animation, 1, True)
s.start_slide()


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
					box.button_func()
		if event.type == QUIT:
			break
	else:
		continue
	break

pygame.quit()
