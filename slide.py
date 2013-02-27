import pygame
from pygame.locals import *
import wrap

default_font = pygame.font.SysFont("arial", 30)
default_colour = (255, 255, 255)

class TextBox():
	def __init__(self, x, y, width, height, text, font=default_font, font_colour=default_colour):
		self.x = x; self.y = y
		self.width = width; self.height = height
		self.font = font; self.font_size = self.font_size; self.font_colour = font_colour
		self.text = text
		self.surf = None

	def render(self):
		self.surf = pygame.Surface((self.width, self.height))
		wrap.render_text(self.surf, self.text, self.font, self.font_colour)
