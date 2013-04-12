import pygame
from pygame.locals import *
import time

import wrap

WIDTH = 800
HEIGHT = 600

default_font = pygame.font.SysFont("Liberation Sans", 15)
default_colour = (0, 0, 0)
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
	def __init__(self, text_boxes, images, animations, back_colour=None,\
					 quiz_answers = None, correct_answer = 0):
		self.text_boxes = text_boxes
		self.images = images
		self.animations = animations
		self.back_colour = back_colour
		self.next = None; self.prev = None
		if quiz_answers is not None:
			generate_quiz(self, quiz_answers, correct_answer)

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


def make_image_appearence_func(x, y, image_path, width=None, height=None):
	image = ImageBox(x, y, image_path, width, height)
	def image_appearence_func(slideshow):
		slideshow.current_slide.images.append(image)
	return image_appearence_func

def generate_quiz(slideshow, quiz_answers, correct_answer):
	for i in xrange(len(quiz_answers)):
		slideshow.text_boxes.append(\
			TextBox(100, HEIGHT/2 + HEIGHT/len(quiz_answers)/2*i,\
						quiz_answers[i], 650,\
						make_image_appearence_func(\
					50, HEIGHT/2 + HEIGHT/len(quiz_answers)/2*i,\
						"tick.png" if correct_answer == i else "cross.png",\
						40, 40)))
		

# Generic buttons
def prev_func(slideshow):
	slideshow.prev_slide()
def next_func(slideshow):
	slideshow.next_slide()
def quit_func(slideshow):
	pygame.event.post(pygame.event.Event(QUIT))

key_bindings = {K_RIGHT: next_func, \
				K_LEFT: prev_func, \
				K_SPACE: next_func}

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
			return
		self.current_slide = self.current_slide.next
		self.current_slide.start_slide()

	def prev_slide(self):
		if self.current_slide.prev is None:
			return
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
