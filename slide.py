import pygame
from pygame.locals import *
import wrap

default_font = pygame.font.SysFont("arial", 15)
default_colour = (255, 255, 255)

class TextBox():
	def __init__(self, x, y, text, width,\
					 button_func=None, back_colour=None,\
					 font=default_font, font_colour=default_colour):
		self.x = x; self.y = y
		self.text = text
		self.width = width; self.height = None
		self.button_func = button_func
		self.back_colour = back_colour
		self.font = font; self.font_colour = font_colour
		self.surf = None
		#Note: Rendering in init for now
		self.render()

	def render(self):
		self.surf = wrap.render_text(self.width, self.text, self.font,\
										 self.font_colour, self.back_colour)
		self.height = self.surf.get_height()

class ImageBox():
	def __init__(self, x, y, image_path, width=None, height=None):
		self.x = x;	self.y = y
		self.width = width; self.height = height
		self.image_path = image_path
		self.image = None
		#Note: Loading image in init for now
		self.load_image()
	def load_image(self):
		self.image = pygame.image.load(self.image_path)
		if self.width is None:
			self.width = self.image.get_width()
		if self.height is None:
			self.height = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

class AnimationSlide():
	def __init__(self, animation_func, interval, loop=True):
		self.animation_func = animation_func
		self.interval = interval
		self.loop = loop
	def draw_slide(self, screen_surf):
		pass
		
class TextSlide():
	def __init__(self, text_boxes, images, back_colour=None):
		self.text_boxes = text_boxes
		self.images = images
		self.back_colour = back_colour

	def draw_slide(self, screen_surf):
		if self.back_colour is not None:
			screen_surf.fill(self.back_colour)
		for image in self.images:
			screen_surf.blit(image.image, (image.x, image.y))
		for text_box in self.text_boxes:
			screen_surf.blit(text_box.surf, (text_box.x, text_box.y))

