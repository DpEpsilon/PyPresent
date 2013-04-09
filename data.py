import slide
import pygame
#def test_animation(screen_surf, position):
#	if position < 0.5:
#		screen_surf.blit(test_image, (0,0))
#	else:
#		screen_surf.blit(test_image, (5,5))

def test_func(slideshow):
	slideshow.current_slide.text_boxes.append(\
		slide.TextBox(20, 300, "WORKED", 150, back_colour=(0, 0, 0)))

image = pygame.image.load("bliss.jpg")
def animation(screen, upto):
	if upto < 0.5:
		screen.blit(image, (200,200))
	else:
		screen.blit(image, (250,250))
	
BACKGROUND_COLOUR = (0, 0, 0)
slideshow = slide.Slideshow([slide.Slide(\
			[slide.TextBox(20, 20,\
							   "I like muffins and cheesecacke emacs is the best", 150),
			 slide.TextBox(20, 100, "LOLOL overlap lol hs1917",\
							   150, back_colour=(255, 0, 0), button_func=test_func)], \
				[slide.ImageBox(20, 100, "bliss.jpg", 150, 250)], \
				[slide.Animation(animation, 2)], BACKGROUND_COLOUR), \
						   slide.Slide(\
						 [slide.TextBox(20, 20, "This is slide 2", 150),\
							  slide.TextBox(20, 100, "LOLOL overlap lol hs1917",\
												150, back_colour=(0, 255, 0),\
												button_func=test_func)],\
							 [slide.ImageBox(20, 100, "bliss.jpg", 150, 250)], \
							 [], BACKGROUND_COLOUR)])
