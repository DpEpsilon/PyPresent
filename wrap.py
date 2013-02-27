import pygame
from pygame.locals import *

def render_text(surface, text, font, font_colour):
	text = text.split()
	dest_height = 0
	start_line = end_line = 0
	width = surface.get_width()
	height = surface.get_height()
	render_font = None

	while end_line <= len(text):
		while end_line <= len(text) and font.size(" ".join(text[start_line:end_line]))[0] < width:
			end_line += 1
		if (start_line == end_line):
			raise Exception("Width too small")
		temp_surf = font.render(" ".join(text[start_line:end_line-1]), True, font_colour)
		surface.blit(temp_surf, (0, dest_height))
		dest_height += font.size(" ".join(text[start_line:end_line-1]))[1]
		start_line = end_line-1
		if (dest_height > height):
			raise Exception("Height too small")