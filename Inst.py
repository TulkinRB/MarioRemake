#set up pygame
import pygame
pygame.init()

#animated image class
class img(object):
  images = []
  index = 0
  max_index = 0
  def __init__(self, images):
    self.images = images
    self.max_index = len(images) - 1
  def update(self):
    self.index += 1
    if self.index > self.max_index:
      self.index = 0
  def return_img(self):
    return self.images[self.index]

#images
background = img([pygame.image.load('textures\\inst\\0.png'), pygame.image.load('textures\\inst\\1.png'), pygame.image.load('textures\\inst\\2.png'), pygame.image.load('textures\\inst\\1.png'), pygame.image.load('textures\\inst\\0.png'), ])
txt_font = pygame.font.SysFont('Arial', 10, True)
title_font = pygame.font.SysFont('Arial', 16, True)

screen_width = 400
screen_height = background.return_img().get_height()
screen = pygame.display.set_mode((screen_width, screen_height))

#function to print background
def print_frame():
  screen.blit(background.return_img(), (0, 0))
  screen.blit(title_font.render("Instractions", 0, (255, 255, 255)), (20, 32))
  screen.blit(txt_font.render("The goal is to reach the flag at the end of each level", 0, (255, 255, 255)), (20, 48))
  screen.blit(txt_font.render("Use arrow keys to move, jump, and shoot fireballs", 0, (255, 255, 255)), (20, 58))
  screen.blit(txt_font.render("Avoid touching monsters and falling into pits", 0, (255, 255, 255)), (20, 68))
  screen.blit(txt_font.render("You can read the full instractions, in the Instractions.txt file", 0, (255, 255, 255)), (20, 78))
  screen.blit(txt_font.render("Press any key to get back to the title screen", 0, (255, 255, 255)), (20, 98))
  pygame.display.update()

running = True
time_count = 0

def run_level():
  global running
  global time_count
  while running:
    #input
    for event in pygame.event.get():
      print event
      if event.type == pygame.QUIT:
        return 'quit'

      elif event.type == pygame.KEYDOWN:
        return 'menu'

      #update images
    if time_count % 250 == 0:
      background.update()
            
    #print images
    print_frame()
    pygame.time.delay(5)
    time_count += 5