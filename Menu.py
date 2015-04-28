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
background = img([pygame.image.load('textures\\menu\\0.png'), pygame.image.load('textures\\menu\\1.png'), pygame.image.load('textures\\menu\\2.png'), pygame.image.load('textures\\menu\\1.png'), pygame.image.load('textures\\menu\\0.png'), ])
cursor = img([pygame.image.load('textures\cursor.png')])
txt_font = pygame.font.SysFont('Arial', 16, True)

screen_width = 400
screen_height = background.return_img().get_height()
screen = pygame.display.set_mode((screen_width, screen_height))

#function to print background
def print_frame():
  screen.blit(background.return_img(), (0, 0))
  screen.blit(txt_font.render("Points", 0, (255, 255, 255)), (40, 8))
  screen.blit(txt_font.render("Coins", 0, (255, 255, 255)), (136, 8))
  screen.blit(txt_font.render("Lives", 0, (255, 255, 255)), (232, 8))
  screen.blit(txt_font.render("Time", 0, (255, 255, 255)), (328, 8))
  screen.blit(txt_font.render("0", 0, (255, 255, 255)), (40, 24))
  screen.blit(txt_font.render("0", 0, (255, 255, 255)), (136, 24))
  screen.blit(txt_font.render("3", 0, (255, 255, 255)), (232, 24))
  screen.blit(txt_font.render("400", 0, (255, 255, 255)), (328, 24))

  screen.blit(txt_font.render("Play", 0, (255, 255, 255)), (40, 112))
  screen.blit(txt_font.render("Quit", 0, (255, 255, 255)), (40, 136))
  screen.blit(cursor.return_img(), (24, 117.5 + (selected_item * 24)))
  pygame.display.update()

items = ['play', 'quit']
selected_item = 0
max_items = 1
running = True
time_count = 0

def run_level():
  global running
  global selected_item
  global max_items
  global time_count
  while running:
    #input
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          if selected_item > 0:
            selected_item -= 1
        elif event.key == pygame.K_DOWN:
          if selected_item < max_items:
            selected_item += 1
        elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
          return items[selected_item]

    #update images
    if time_count % 250 == 0:
      background.update()
            
    #print images
    print_frame()
    pygame.time.delay(5)
    time_count += 5
  return 'quit'