#set up pygame
import pygame
pygame.init()
block_map = pygame.PixelArray(pygame.image.load('lvl1map.png'))
for i in range(len(block_map)):
  for j in range(len(block_map[i])):
      block_map[i, j] &= 0xffffff

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
    if not self.max_index == -1:
      if type(self.images[self.index]) == img:
        return self.images[self.index].return_img()
      else:
        return self.images[self.index]


#images
background = img([pygame.image.load('textures\\background2.png')])
mario_small = img([pygame.image.load('textures\mario\small_mario.png')])
mario_super = img([pygame.image.load('textures\mario\super_mario.png')])
mario_fire = img([pygame.image.load('textures\mario\\fire_mario.png')])
mario_small_inv = img([pygame.image.load('textures\mario\invincible_small_mario\\0.png'), pygame.image.load('textures\mario\invincible_small_mario\\1.png'), pygame.image.load('textures\mario\invincible_small_mario\\2.png'), pygame.image.load('textures\mario\invincible_small_mario\\3.png')])
mario_super_inv = img([pygame.image.load('textures\mario\invincible_super_mario\\0.png'), pygame.image.load('textures\mario\invincible_super_mario\\1.png'), pygame.image.load('textures\mario\invincible_super_mario\\2.png'), pygame.image.load('textures\mario\invincible_super_mario\\3.png'), pygame.image.load('textures\mario\invincible_super_mario\\4.png')])
mario = [mario_small, mario_super, mario_fire, mario_small_inv, mario_super_inv]
goomba = img([pygame.image.load('textures\goomba\\0.png'), pygame.image.load('textures\goomba\\1.png')])
koopa_l = img([pygame.image.load('textures\koopa\left\\0.png'), pygame.image.load('textures\koopa\left\\1.png')])
koopa_r = img([pygame.image.load('textures\koopa\\right\\0.png'), pygame.image.load('textures\koopa\\right\\1.png')])
koopa = img([koopa_l, koopa_r])
koopa_shell = img([pygame.image.load('textures\green_shell.png')])
coin = img([pygame.image.load('textures\coin\\0.png'), pygame.image.load('textures\coin\\1.png'), pygame.image.load('textures\coin\\2.png'), pygame.image.load('textures\coin\\1.png'), pygame.image.load('textures\coin\\0.png')])
super_mushroom = img([pygame.image.load('textures\super_mushroom.png')])
up_mushroom = img([pygame.image.load('textures\\1_up_mushroom.png')])
star_man = img([pygame.image.load('textures\star_man\\0.png'), pygame.image.load('textures\star_man\\1.png'), pygame.image.load('textures\star_man\\2.png'), pygame.image.load('textures\star_man\\3.png')])
fire_flower = img([pygame.image.load('textures\\fire_flower\\0.png'), pygame.image.load('textures\\fire_flower\\1.png'), pygame.image.load('textures\\fire_flower\\2.png'), pygame.image.load('textures\\fire_flower\\3.png')])
empty_block = img([pygame.image.load('textures\empty_block.png')])
bricks = img([pygame.image.load('textures\\bricks.png')])
prize = img([pygame.image.load('textures\prize_block\\0.png'), pygame.image.load('textures\prize_block\\1.png'), pygame.image.load('textures\prize_block\\2.png'), pygame.image.load('textures\prize_block\\1.png'), pygame.image.load('textures\prize_block\\0.png')])
invisible = img([])

screen_width = 400
screen_height = background.return_img().get_height()
screen = pygame.display.set_mode((screen_width, screen_height))
flag_x = 3168
castle_x = 3266



#create player class
class Player(object):
#player's vars
  x1 = 0
  x2 = 0
  y1 = 0
  y2 = 0
  #(x1, y1) is top-left corner, (x2, y2) is bottom-right corner
  speed_x = 0
  speed_y = 0
  images = [None]
  img = images[0]
  mode = 0
  inv = False
  jump_height = 0
  max_jump_height = 0
  slowed_jump = False
  is_moving_right = False
  is_moving_left = False
  is_jumping = False #only part of going up of the jump
  on_ground = False
#function to move player
  def move(self, direction):
    global entities
    global blocks
    global points
    if direction == 'left' and self.can_move('left'):
      if self.on_ground:
        self.x1 -= self.speed_x
        self.x2 -= self.speed_x
      else:
        self.x1 -= 1.5 * self.speed_x
        self.x2 -= 1.5 * self.speed_x
      set_view_range()
    elif direction == 'right' and self.can_move('right'):
      if self.on_ground:
        self.x1 += self.speed_x
        self.x2 += self.speed_x
      else:
        self.x1 += 1.5 * self.speed_x
        self.x2 += 1.5 * self.speed_x
      set_view_range()
    elif direction == 'up' and self.can_move('up'):
      self.y1 -= self.speed_y
      self.y2 -= self.speed_y
      for block in blocks:
        if is_player_touch(block):
          block.give_bonus()
    elif direction == 'up':
      self.y1 -= self.speed_y
      self.y2 -= self.speed_y
      for block in blocks:
        if is_player_touch(block):
          block.give_bonus()
      self.y1 += self.speed_y
      self.y2 += self.speed_y
    elif direction == 'down' and self.can_move('down'):
      self.y1 += self.speed_y
      self.y2 += self.speed_y
      for entity in entities:
        if is_player_touch(entity):
          if entity.ent_type == 'koopa':
            entity.ent_type = 'koopa_shell'
            entity.img = koopa_shell
            entity.speed_x = 0
            self.move('up')
          elif entity.ent_type == 'koopa_shell':
            entity.ent_type = 'moving_koopa_shell'
            entity.speed_x = 3
            entity.move_dir = 'right'
          else:
            entity.kill()
          self.is_jumping = True
          self.max_jump_height = 16
          points += 100
    self.check_falling()
    if self.can_move('down'):
      self.on_ground = False
    else:
      self.on_ground = True
#function to check player's ability to move
  def can_move(self, direction):
    global block_map
    if direction == 'left':
      self.x1 -= self.speed_x
      self.x2 -= self.speed_x
    elif direction == 'right':
      self.x1 += self.speed_x
      self.x2 += self.speed_x
    elif direction == 'up':
      self.y1 -= self.speed_y
      self.y2 -= self.speed_y
    elif direction == 'down':
      self.y1 += self.speed_y
      self.y2 += self.speed_y

    x1_blocks = int((self.x1 + 16) / 16)
    x2_blocks = int((self.x2 + 16) / 16)
    y1_blocks = int(self.y1 / 16)
    y2_blocks = int(self.y2 / 16)

    if direction == 'left':
      if (block_map[x1_blocks, y1_blocks] == 0) or (block_map[x1_blocks, y2_blocks] == 0):
        result =  False
      else:
        result = True
    elif direction == 'right':
      if (block_map[x2_blocks, y1_blocks] == 0) or (block_map[x2_blocks, y2_blocks] == 0):
        result =  False
      else:
        result = True
    elif direction == 'up':
      if (block_map[x1_blocks, y1_blocks] == 0) or (block_map[x2_blocks, y1_blocks] == 0):
        result =  False
      else:
        result = True
    elif direction == 'down':
      if (block_map[x1_blocks, y2_blocks] == 0) or (block_map[x2_blocks, y2_blocks] == 0):
        result =  False
      else:
        result = True

    if direction == 'left':
      self.x1 += self.speed_x
      self.x2 += self.speed_x
    elif direction == 'right':
      self.x1 -= self.speed_x
      self.x2 -= self.speed_x
    elif direction == 'up':
      self.y1 += self.speed_y
      self.y2 += self.speed_y
    elif direction == 'down':
      self.y1 -= self.speed_y
      self.y2 -= self.speed_y
    return result
  def check_falling(self):
    global block_map
    x1_blocks = int(self.x1 / 16) + 1
    x2_blocks = int(self.x2 / 16) + 1
    y1_blocks = int(self.y1 / 16)
    y2_blocks = int(self.y2 / 16)

    if (block_map[x1_blocks, y2_blocks] == 104) or (block_map[x2_blocks, y2_blocks] == 104):
      kill_player(True)
#create entity class
class Entity(object):
  #entity's vars
  x1 = 0
  x2 = 0
  y1 = 0
  y2 = 0
  #(x1, y1) is top-left corner, (x2, y2) is bottom-right corner
  speed_x = 0
  speed_y = 0
  move_dir = 'left'
  started_moving = False
  on_ground = True
  img = None
  ent_type = None
#function to move entity
  def move(self, direction):
    if direction == 'side':
      if self.on_ground:
        if self.move_dir == 'left':
          self.x1 -= self.speed_x
          self.x2 -= self.speed_x
        else:
          self.x1 += self.speed_x
          self.x2 += self.speed_x
      else:
        if self.move_dir == 'left':
          self.x1 -= 1.5 * self.speed_x
          self.x2 -= 1.5 * self.speed_x
        else:
          self.x1 += 1.5 * self.speed_x
          self.x2 += 1.5 * self.speed_x
    elif direction == 'up' and self.can_move('up'):
      self.y1 -= self.speed_y
      self.y2 -= self.speed_y
    elif direction == 'down' and self.can_move('down'):
      self.y1 += self.speed_y
      self.y2 += self.speed_y
    self.check_falling()
    if self.can_move('down'):
      self.on_ground = False
    else:
      self.on_ground = True
    if (direction == 'side') and (not self.can_move(self.move_dir)):
      if self.move_dir == 'left':
        self.move_dir = 'right'
      else:
        self.move_dir = 'left'
#function to check entity's ability to move
  def can_move(self, direction):
    global block_map
    if direction == 'left':
      self.x1 -= self.speed_x
      self.x2 -= self.speed_x
    elif direction == 'right':
      self.x1 += self.speed_x
      self.x2 += self.speed_x
    elif direction == 'up':
      self.y1 -= self.speed_y
      self.y2 -= self.speed_y
    elif direction == 'down':
      self.y1 += self.speed_y
      self.y2 += self.speed_y

    x1_blocks = int(self.x1 / 16) + 1
    x2_blocks = int(self.x2 / 16) + 1
    y1_blocks = int(self.y1 / 16)
    y2_blocks = int(self.y2 / 16)
    if direction == 'left':
      if (block_map[x1_blocks, y1_blocks] == 0) or (block_map[x1_blocks, y2_blocks] == 0):
        result =  False
      else:
        result = True
    elif direction == 'right':
      if (block_map[x2_blocks, y1_blocks] == 0) or (block_map[x2_blocks, y2_blocks] == 0):
        result =  False
      else:
        result = True
    elif direction == 'up':
      if (block_map[x1_blocks, y1_blocks] == 0) or (block_map[x2_blocks, y1_blocks] == 0):
        result =  False
      else:
        result = True
    elif direction == 'down':
      if (block_map[x1_blocks, y2_blocks] == 0) or (block_map[x2_blocks, y2_blocks] == 0):
        result =  False
      else:
        result = True

    if direction == 'left':
      self.x1 += self.speed_x
      self.x2 += self.speed_x
    elif direction == 'right':
      self.x1 -= self.speed_x
      self.x2 -= self.speed_x
    elif direction == 'up':
      self.y1 += self.speed_y
      self.y2 += self.speed_y
    elif direction == 'down':
      self.y1 -= self.speed_y
      self.y2 -= self.speed_y
    return result

  def check_falling(self):
    global block_map
    x1_blocks = int(self.x1 / 16) + 1
    x2_blocks = int(self.x2 / 16) + 1
    y1_blocks = int(self.y1 / 16)
    y2_blocks = int(self.y2 / 16)

    if (block_map[x1_blocks, y2_blocks] == 104) or (block_map[x2_blocks, y2_blocks] == 104):
      self.kill()
  
  def kill(self):
    global entities
    my_ID = entities.index(self)
    entities.pop(my_ID)



#create block class
class Block(object):
#block's vars
  x1 = 0
  x2 = 0
  y1 = 0
  y2 = 0
  #(x1, y1) is top-left corner, (x2, y2) is bottom-right corner
  speed_y = 0
  img = None
  bonus_type = None
  times = 1
  def give_bonus(self):
    global coins
    global lives
    global points
    global entities
    if self.times > 0:
      if self.bonus_type == 'coin':
        coins += 1
        points += 100
        if coins == 100:
          coins = 0
          lives += 1
      elif self.bonus_type == 'super_mushroom':
        if player.mode == 0:
          entities.append(create_entity(self.x1, self.y1 - 16, 0.4, 1.4, super_mushroom, 'super_mushroom'))
        else:
          entities.append(create_entity(self.x1, self.y1 - 16, 0, 0, fire_flower, 'fire_flower'))
      elif self.bonus_type == 'up_mushroom':
        entities.append(create_entity(self.x1, self.y1 - 16, 0.4, 1.4, up_mushroom, 'up_mushroom'))
      elif self.bonus_type == 'star_man':
        entities.append(create_entity(self.x1, self.y1 - 16, 0.8, 1.6, star_man, 'star_man'))
      times -= 1




#create functions

#function to create player object
def create_player(x, y, speed_x, speed_y, img):
  p = Player()
  p.images = img
  p.img = img[0]
  p.x1 = x
  p.x2 = x + img[0].return_img().get_width() - 1
  p.y1 = y
  p.y2 = y + img[0].return_img().get_height() - 1
  p.speed_x = speed_x
  p.speed_y = speed_y
  return p

#function to create entity object
def create_entity(x, y, speed_x, speed_y, img, ent_type):
  e = Entity()
  e.img = img
  e.x1 = x
  e.x2 = x + img.return_img().get_width() - 1
  e.y1 = y
  e.y2 = y + img.return_img().get_height() - 1
  e.speed_x = speed_x
  e.speed_y = speed_y
  e.ent_type = ent_type
  e.started_moving = False
  return e

#function to create block object
def create_block(x, y, speed_y, img, bonus, times):
  b = Block()
  b.x1 = x
  b.x2 = x + 15
  b.y1 = y
  b.y2 = y + 15
  b.speed_y = speed_y
  b.img = img
  b.bonus_type = bonus
  b.times = times
  return b

#function to detect touch between player and entity/block
def is_player_touch(entity):
  global player
  for entity_x in range(int(entity.x1), int(entity.x2)):
    for entity_y in range(int(entity.y1), int(entity.y2)):
      if ((int(player.x1) == entity_x) or (int(player.x2) == entity_x)) and ((int(player.y1) == entity_y) or (int(player.y2) == entity_y)):
        return True
  return False

#function to detect touch between 2 entities
def is_entity_touch(entity1, entity2):
  for entity1_x in range(int(entity1.x1), int(entity1.x2)):
    for entity1_y in range(int(entity1.y1), int(entity1.y2)):
      if ((int(entity2.x1) == entity1_x) or (int(entity2.x2) == entity1_x)) and ((int(entity2.y1) == entity1_y) or (int(entity2.y2) == entity1_y)):
        return True
  return False

#function to print background
def print_frame():
  screen.blit(background.return_img(), (-view_range, 0))
  screen.blit(player.img.return_img(), (player.x1 - view_range, player.y1 - 8))
      for entity in entities:
        screen.blit(entity.img.return_img(), (entity.x1 - view_range, entity.y1 - 8))
      for block in blocks:
        if not block.img == invisible:
          screen.blit(block.img.return_img(), (block.x1 - view_range, block.y1 - 8))
  pygame.display.update()

#function to set the part that is printed on the screen
def set_view_range():
  global view_range
  global screen_width
  global background
  background_width = background.return_img().get_width() - 1
  if player.x1 <= view_range + 96:
    if not view_range <= 0:
      view_range = player.x1 - 96
    else:
      view_range = 0
  elif player.x2 >= (view_range + screen_width - 176):
    if not view_range >= (background_width - screen_width):
      view_range = player.x2 - screen_width + 176
    else:
      view_range = background_width - screen_width

#function to kill player
def kill_player(is_falling):
  global lives
  global screen_height
  if not is_falling:
    for i in range(0, 48, player.speed_y):
      player.y1 -= player.speed_y
      player.y2 -= player.speed_y
      print_frame()
      pygame.time.delay(5)
  while player.y1 <= screen_height:
    player.y1 += player.speed_y
    player.y2 += player.speed_y
    print_frame()
    pygame.time.delay(5)
  lives -= 1
  reset()

def end_level():
  global time_count
  player.move('down')
  while not player.x1 >= castle_x:
    player.move('right')
    print_frame()
    pygame.time.delay(5)

#function to reset the game
def reset():
  global player
  global entities
  global blocks
  global time_count
  global sec_count
  global view_range
  player = create_player(0, 0, 0.5, 1.5, mario)
  entities = [
  create_entity(22*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(40*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(51*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(52.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(80*16, 4*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(82*16, 4*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(97*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(98.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(114*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(115.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(124*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(125.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(128*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(129.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(174*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(175.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(107*16, 12*16, 0.4, 1.4, koopa, 'koopa')
  ]
  blocks = [
  create_block(16*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(21*16, 9*16, 0.4, prize, 'super_mushroom', 1),
  create_block(22*16, 5*16, 0.4, prize, 'coin', 1),
  create_block(23*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(64*16, 8*16, 0.4, invisible, 'up_mushroom', 1),
  create_block(78*16, 9*16, 0.4, prize, 'super_mushroom', 1),
  create_block(94*16, 9*16, 0.4, bricks, 'coin', 1),
  create_block(94*16, 5*16, 0.4, prize, 'coin', 1),
  create_block(101*16, 9*16, 0.4, bricks, 'star_man', 1),
  create_block(106*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(109*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(109*16, 5*16, 0.4, prize, 'super_mushroom', 1),
  create_block(112*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(129*16, 5*16, 0.4, prize, 'coin', 1),
  create_block(130*16, 5*16, 0.4, prize, 'coin', 1),
  create_block(170*16, 9*16, 0.4, prize, 'coin', 1)
  ]
  time_count = 0
  sec_count = 400
  view_range = 0 #the x cordinate of the left side of the part you can see on the screen





player = None
entities = None
blocks = None
time_count = None
sec_count = None
view_range = None
points = 0
coins = 0
lives = 3
running = True
reset()
#main section

def run_level(coins_in, points_in, lives_in):
  global player
  global entities
  global blocks
  global screen
  global time_count
  global sec_count
  global view_range
  global running
  global lives
  global points
  global coins
  lives = lives_in
  coins = coins_in
  points = points_in
  while running:
    #input
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          player.is_moving_left = True
        elif event.key == pygame.K_RIGHT:
          player.is_moving_right = True
        elif event.key == pygame.K_UP:
          if player.on_ground:
            player.is_jumping = True
            player.max_jump_height = 70

      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          player.is_moving_left = False
        elif event.key == pygame.K_RIGHT:
          player.is_moving_right = False

    if lives >= 0:
      #move player
      if player.is_jumping:
        player.move('up')
        player.jump_height += player.speed_y
        if player.jump_height >= player.max_jump_height:
          player.is_jumping = False
          player.jump_height = 0
          player.speed_y *= 2
          player.slowed_jump = False
        elif (player.jump_height >= (3 * player.max_jump_height) / 4) and (not player.slowed_jump):
          player.speed_y /= 2.0
          player.slowed_jump = True
      else:
        player.move('down') #gravity
      if player.is_moving_left:
        player.move('left')
      if player.is_moving_right:
        player.move('right')
      if player.x2 >= flag_x:
        end_level()
        return {'coins':coins, 'points':points, 'lives':lives}
            
      #move entities
      for entity in entities:
        if (entity.x2 >= view_range) and (entity.x1 <= view_range + screen_width):
          entity.started_moving = True
        if entity.started_moving:
          entity.move('side')
          entity.move('down')
        if is_player_touch(entity):
          if entity.ent_type == 'koopa_shell':
            entity.ent_type = 'moving_koopa_shell'
            entity.speed_x = 3
            entity.move_dir = 'right'
          else:
            kill_player(False)
        for entity2 in entities:
          if entity2.ent_type == 'moving_koopa_shell' and is_entity_touch(entity, entity2) and not entity == entity2:
            entity.kill()

      #update images
      if player.inv == True and time_count % 10 == 0:
        player.img.update()
      for entity in entities:
        if entity.ent_type == 'goomba' and time_count % 250 == 0:
          entity.img.update()
            
      #print images
      print_background()
      pygame.time.delay(5)
      time_count += 5

      print("c-" + str(coins) + " p-" + str(points) + " lives-" + str(lives))
    else:
      return {'coins':coins, 'points':points, 'lives':lives}