import pygame
from pygame.locals import *

def render_text(width, text, font, font_colour, back_colour):
	text = text.split()
	dest_height = 0
	start_line = end_line = 0
	lines = []

	while end_line <= len(text):
		while end_line <= len(text) and\
				font.size(" ".join(text[start_line:end_line]))[0] < width:
			end_line += 1
		if (end_line - start_line <= 1):
			raise Exception("Width too small")
		lines.append((font.render(" ".join(text[start_line:end_line-1]),\
									  True, font_colour), dest_height))
		dest_height += lines[-1][0].get_height()
		start_line = end_line-1

	if back_colour is None:
		# This surface is transparent
		rend_surf = pygame.Surface((width, dest_height),\
									   pygame.SRCALPHA, 32).convert_alpha()
	else:
		rend_surf = pygame.Surface((width, dest_height))
		rend_surf.fill(back_colour)
	for line in lines:
		rend_surf.blit(line[0], (0, line[1]))

	return rend_surf
