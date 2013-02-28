import pygame
from pygame.locals import *
import wrap

default_font = pygame.font.SysFont("arial", 15)
default_colour = (255, 255, 255)

class TextBox():
	def __init__(self, x, y, width, height, text, font=default_font, font_colour=default_colour):
		self.x = x; self.y = y
		self.width = width; self.height = height
		self.font = font; self.font_colour = font_colour
		self.text = text
		self.surf = None
		#Note: Rendering in init for now
		self.render()

	def render(self):
		self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32).convert_alpha() # This surface is transparent
		wrap.render_text(self.surf, self.text, self.font, self.font_colour)

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

class TextSlide():
	def __init__(self, text_boxes, images, back_colour):
		self.text_boxes = text_boxes
		self.images = images
		self.back_colour = back_colour

	def draw_slide(self, screen_surf):
		for image in self.images:
			screen_surf.blit(image.image, (image.x, image.y))
		for text_box in self.text_boxes:
			screen_surf.blit(text_box.surf, (text_box.x, text_box.y))