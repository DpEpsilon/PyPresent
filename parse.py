import json

import slide
import animations
import pygame

def load_slideshow(filename):
	slideshow_file = open(filename, "rU").read()
	slideshow_dom = json.loads(slideshow_file)
	return resolve_slideshow(slideshow_dom)

# The 'resolve' functions replace python dictionaries with
# actual objects that can be used by pypresent by traversing
# the dom tree given by the json file and replacing each
# object it comes across.
	
def resolve_slideshow(dom_tree):
	for i in xrange(len(dom_tree['slides'])):
		dom_tree['slides'][i] = resolve_slide(dom_tree['slides'][i])
	
	return slide.Slideshow(**dom_tree)

def resolve_slide(dom_tree):
	if 'type' in dom_tree:
		slide_type = dom_tree.pop('type')
	else:
		slide_type = 'normal'

	for i in xrange(len(dom_tree['text_boxes'])):
		dom_tree['text_boxes'][i] = \
			resolve_text_box(dom_tree['text_boxes'][i])

	for i in xrange(len(dom_tree['images'])):
		dom_tree['images'][i] = \
			resolve_image(dom_tree['images'][i])

	for i in xrange(len(dom_tree['animations'])):
		dom_tree['animations'][i] = \
			resolve_animation(dom_tree['animations'][i])
	
	if slide_type is 'normal':
		return slide.Slide(**dom_tree)
	elif slide_type is 'quiz':
		raise NotImplemented("There is currently no support " \
								 "for quiz slides.")
	else:
		raise Exception('invalid slide type')

def resolve_text_box(dom_tree):
	if 'font' in dom_tree:
		dom_tree['font'] = pygame.font.SysFont(dom_tree['font'])
	return slide.TextBox(**dom_tree)

def resolve_image(dom_tree):
	return slide.ImageBox(**dom_tree)

def resolve_animation(dom_tree):
	dom_tree['animation_func'] = \
		getattr(animation, dom_tree['animation_func'])
	return slide.Animation(**dom_tree)
