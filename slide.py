import pygame
from pygame.locals import *
import time

import wrap

WIDTH = 800
HEIGHT = 600

default_font = pygame.font.SysFont("arial", 15)
default_colour = (255, 255, 255)
curr_slide = None
prev_box = None; next_box = None; quit_box = None

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

class Animation():
	def __init__(self, animation_func, interval, loop=True):
		self.animation_func = animation_func
		self.interval = interval
		self.loop = loop
		self.start_time = 0.0
		
	def draw(self, screen_surf, curr_time):
		if self.loop:
			self.animation_func(screen_surf,\
									((curr_time - self.start_time)/self.interval)%1.0)
		elif curr_time - self.start_time < self.interval:
			self.animation_func(screen_surf,\
									((curr_time - self.start_time)/self.interval))
		else:
			self.animation_func(screen_surf, 1.0)
		
class Slide():
	def __init__(self, text_boxes, images, animations, back_colour=None):
		self.text_boxes = text_boxes
		self.images = images
		self.animations = animations
		self.back_colour = back_colour
		self.next = None; self.prev = None

	def start_slide(self):
		# Start animation
		curr_time = time.time()
		for anim in self.animations:
			anim.start_time = curr_time
	
	def draw_slide(self, screen_surf):
		# Fill with back_colour
		if self.back_colour is not None:
			screen_surf.fill(self.back_colour)
		# Draw images
		for image in self.images:
			screen_surf.blit(image.image, (image.x, image.y))
		# Advance animations
		for anim in self.animations:
			curr_time = time.time()
			anim.draw(screen_surf, curr_time)
		# Draw text boxes
		for text_box in self.text_boxes:
			screen_surf.blit(text_box.surf, (text_box.x, text_box.y))

# Generic buttons
def prev_func(slideshow):
	slideshow.prev_slide()
def next_func(slideshow):
	slideshow.next_slide()
def quit_func(slideshow):
	pygame.event.post(pygame.event.Event(QUIT))

class Slideshow():
	def __init__(self, slides):
		prev_box = TextBox(20, HEIGHT-30, "PREV", 50, prev_func, (255, 0, 0))
		next_box = TextBox(WIDTH-70, HEIGHT-30, "NEXT", 50, next_func, (0, 255, 0))
		quit_box = TextBox(WIDTH/2 - 25, HEIGHT-30, "QUIT", 50, \
							   quit_func, (255, 255, 0))
		slides[0].text_boxes.append(quit_box)
		for slide in xrange(1, len(slides)):
			slides[slide-1].next = slides[slide]
			slides[slide-1].text_boxes.append(next_box)
			slides[slide].prev = slides[slide-1]
			slides[slide].text_boxes.append(prev_box)
			slides[slide].text_boxes.append(quit_box)
		self.slides = slides
		self.current_slide = None


	def start_slide(self, slide=0):
		self.current_slide = self.slides[slide]
		self.current_slide.start_slide()

	def next_slide(self):
		if self.current_slide.next is None:
			raise Exception("There is no next slide.")
		self.current_slide = self.current_slide.next
		self.current_slide.start_slide()

	def prev_slide(self):
		if self.current_slide.prev is None:
			raise Exception("There is no previous slide.")
		self.current_slide = self.current_slide.prev
		self.current_slide.start_slide()
		
	def draw(self, screen_surf):
		self.current_slide.draw_slide(screen_surf)
	


def init(slide_w, slide_h):
	global prev_box; global next_box; global quit_box
	prev_box = TextBox(20, slide_h-30, "PREV", 50, prev_func, (255, 0, 0))
	next_box = TextBox(slide_w-70, slide_h-30, "NEXT", 50, next_func, (0, 255, 0))
	quit_box = TextBox(slide_w/2 - 25, slide_h-30, "QUIT", 50, \
						quit_func, (255, 255, 0))

	curr_slide = slides[0]
	curr_slide.start_slide()
