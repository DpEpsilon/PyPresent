import pygame
from pygame.locals import *

default_font = pygame.font.SysFont("arial", 30)

def render_text(surface, text, colour, back_colour, use_default, font="arial", size=20):
	text = text.split()
	dest_height = 0
	start_line = end_line = 0
	width = surface.get_width()
	height = surface.get_height()
	render_font = None

	if use_default:
		render_font = default_font
	else:
		render_font = pygame.font.SysFont(font, size)

	while end_line <= len(text):
		while end_line <= len(text) and render_font.size(" ".join(text[start_line:end_line]))[0] < width:
			end_line += 1
		if (start_line == end_line):
			raise Exception("Width too small")
		temp_surf = render_font.render(" ".join(text[start_line:end_line-1]), True, colour, back_colour)
		surface.blit(temp_surf, (0, dest_height))
		dest_height += render_font.size(" ".join(text[start_line:end_line-1]))[1]
		start_line = end_line-1
		if (dest_height > height):
			raise Exception("Height too small")