











































  
            
            
                entity.kill()
                kill_player(False)
                player.img = player.images[player.mode]
                player.mode = 0
                player.x2 = player.x1 + player.img.return_img().get_width() - 1
                player.y1 = player.y2 - player.img.return_img().get_height() + 1
              else:
              entity.ent_type = 'koopa_shell'
              entity.ent_type = 'moving_koopa_shell'
              entity.ent_type = 'moving_koopa_shell'
              entity.img = koopa_shell
              entity.kill()
              entity.move_dir = 'right'
              entity.move_dir = 'right'
              entity.speed_x = 0
              entity.speed_x = 3
              entity.speed_x = 3
              if player.mode > 0:
              player.img = player.images[3]
              player.img = player.images[4]
              player.img = player.images[4]
              player.img = player.images[player.mode]
              player.mode = 2
              player.move('down')
              player.move('left')
              player.x2 = player.x1 + player.img.return_img().get_width() - 1
              player.y1 = player.y2 - player.img.return_img().get_height() + 1
              self.move('up')
              self.move('up')
            e = create_entity(player.x2, player.y1, 0.6, 1.6, fire_ball, 'fire_ball')
            e = create_entity(self.x1, self.y1 - 16, 0, 0, fire_flower, 'fire_flower')
            e = create_entity(self.x1, self.y1 - 16, 0.4, 1.4, super_mushroom, 'super_mushroom')
            e.move_dir = 'right'
            elif entity.ent_type == 'koopa_shell':
            else:
            else:
            else:
            else:
            entities.append(e)
            entity.kill()
            entity.kill()
            entity.kill()
            entity.kill()
            entity.kill()
            entity.kill()
            entity2.kill()
            if entity.ent_type == 'koopa':
            if entity.ent_type == 'koopa_shell':
            if player.inv:
            if player.mode == 0:
            if player.mode > 2:
            inv_count = 10000
            lives += 1
            player.inv = True
            player.is_jumping = True
            player.max_jump_height = 70
            player.mode += 1
            player.x2 = player.x1 + player.img.return_img().get_width() - 1
            player.y1 = player.y2 - player.img.return_img().get_height() + 1
            points += 100
            self.is_jumping = True
            self.max_jump_height = 16
            while not player.can_move('right'):
            while not player.can_move('up'):
          block.give_bonus()
          block.give_bonus()
          block.img.update()
          coins = 0
          e = create_entity(self.x1, self.y1 - 16, 0.4, 1.4, up_mushroom, 'up_mushroom')
          e = create_entity(self.x1, self.y1 - 16, 0.6, 1.6, star_man, 'star_man')
          elif entity.ent_type == 'star_man':
          elif entity.ent_type == 'up_mushroom':
          elif entity2.ent_type == 'fire_ball' and is_entity_touch(entity, entity2) and not entity == entity2:
          elif not entity.ent_type == 'fire_ball':
          elif player.inv:
          else:
          entity.img.return_next_level().update()
          entity.img.update()
          entity.img.update()
          entity.move('down')
          entity.move('side')
          entity.started_moving = True
          if entity.ent_type == 'super_mushroom' or entity.ent_type == 'fire_flower':
          if entity2.ent_type == 'moving_koopa_shell' and is_entity_touch(entity, entity2) and not entity == entity2:
          if is_player_touch(entity):
          if player.mode == 0:
          if player.mode == 2:
          if player.on_ground:
          lives += 1
          player.img = player.images[player.mode]
          player.inv = False
          player.is_jumping = False
          player.is_moving_left = False
          player.is_moving_left = True
          player.is_moving_right = False
          player.is_moving_right = True
          player.jump_height = 0
          player.slowed_jump = False
          player.slowed_jump = True
          player.speed_y *= 2
          player.speed_y /= 2.0
          return {'coins':coins, 'points':points, 'lives':lives, 'goto':'menu'}
          self.x1 += 1.5 * self.speed_x
          self.x1 += self.speed_x
          self.x1 -= 1.5 * self.speed_x
          self.x1 -= self.speed_x
          self.x2 += 1.5 * self.speed_x
          self.x2 += self.speed_x
          self.x2 -= 1.5 * self.speed_x
          self.x2 -= self.speed_x
        coins += 1
        e.move_dir = 'right'
        elif (player.jump_height >= (3 * player.max_jump_height) / 4) and (not player.slowed_jump):
        elif event.key == pygame.K_DOWN:
        elif event.key == pygame.K_ESCAPE:
        elif event.key == pygame.K_RIGHT:
        elif event.key == pygame.K_RIGHT:
        elif event.key == pygame.K_UP:
        elif self.bonus_type == 'star_man':
        elif self.bonus_type == 'up_mushroom':
        else:
        else:
        end_level()
        entities.append(e)
        for entity2 in entities:
        if (entity.ent_type == 'fire_flower' or entity.ent_type == 'star_man') and time_count % 50 == 0:
        if (entity.x2 >= view_range) and (entity.x1 <= view_range + screen_width):
        if block.img == invisible and time_count % 250 == 0:
        if coins == 100:
        if entity.ent_type == 'goomba' and time_count % 250 == 0:
        if entity.ent_type == 'koopa' and time_count % 250 == 0:
        if entity.started_moving:
        if event.key == pygame.K_LEFT:
        if event.key == pygame.K_LEFT:
        if inv_count < 0:
        if is_player_touch(block):
        if is_player_touch(block):
        if is_player_touch(entity):
        if not (entity.ent_type == 'super_mushroom' or entity.ent_type == 'fire_flower' or entity.ent_type == 'up_mushroom' or entity.ent_type == 'star_man' or entity.ent_type == 'fire_ball'):
        if player.jump_height >= player.max_jump_height:
        if self.bonus_type == 'super_mushroom':
        if self.move_dir == 'left':
        if self.move_dir == 'left':
        inv_count -= 5
        kill_player(False)
        player.img.update()
        player.jump_height += player.speed_y
        player.move('down') #gravity
        player.move('left')
        player.move('right')
        player.move('up')
        points += 100
        result =  False
        result =  False
        result =  False
        result =  False
        result =  False
        result =  False
        result =  False
        result =  False
        result = True
        result = True
        result = True
        result = True
        result = True
        result = True
        result = True
        result = True
        return self.images[self.index]
        return self.images[self.index]
        return self.images[self.index].return_img()
        return True
        return True
        return {'coins':coins, 'points':points, 'lives':lives, 'goto':'congratulations'}
        running = False
        sec_count -= 1
        self.img.update()
        self.kill()
        self.move_dir = 'left'
        self.move_dir = 'right'
        self.on_ground = False
        self.on_ground = False
        self.on_ground = True
        self.on_ground = True
        self.x1 += 1.5 * self.speed_x
        self.x1 += self.speed_x
        self.x1 -= 1.5 * self.speed_x
        self.x1 -= self.speed_x
        self.x2 += 1.5 * self.speed_x
        self.x2 += self.speed_x
        self.x2 -= 1.5 * self.speed_x
        self.x2 -= self.speed_x
      #move entities
      #move player
      #print images
      #update images
      block_map[i, j] &= 0xffffff
      elif event.type == pygame.KEYDOWN:
      elif event.type == pygame.KEYUP:
      elif self.ent_type == 'fire_ball':
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      else:
      for block in blocks:
      for block in blocks:
      for block in blocks:
      for entity in entities:
      for entity in entities:
      for entity in entities:
      i += player.speed_y
      if ((int(entity2.x1) == entity1_x) or (int(entity2.x2) == entity1_x)) and ((int(entity2.y1) == entity1_y) or (int(entity2.y2) == entity1_y)):
      if ((int(player.x1) == entity_x) or (int(player.x2) == entity_x)) and ((int(player.y1) == entity_y) or (int(player.y2) == entity_y)):
      if (block_map[x1_blocks, y1_blocks] == 0) or (block_map[x1_blocks, y2_blocks] == 0):
      if (block_map[x1_blocks, y1_blocks] == 0) or (block_map[x1_blocks, y2_blocks] == 0):
      if (block_map[x1_blocks, y1_blocks] == 0) or (block_map[x2_blocks, y1_blocks] == 0):
      if (block_map[x1_blocks, y1_blocks] == 0) or (block_map[x2_blocks, y1_blocks] == 0):
      if (block_map[x1_blocks, y2_blocks] == 0) or (block_map[x2_blocks, y2_blocks] == 0):
      if (block_map[x1_blocks, y2_blocks] == 0) or (block_map[x2_blocks, y2_blocks] == 0):
      if (block_map[x2_blocks, y1_blocks] == 0) or (block_map[x2_blocks, y2_blocks] == 0):
      if (block_map[x2_blocks, y1_blocks] == 0) or (block_map[x2_blocks, y2_blocks] == 0):
      if event.type == pygame.QUIT:
      if player.inv and time_count % 50 == 0:
      if player.inv:
      if player.is_jumping:
      if player.is_moving_left:
      if player.is_moving_right:
      if player.x2 >= flag_x:
      if sec_count < 0:
      if self.bonus_type == 'coin':
      if self.can_move('down'):
      if self.can_move('down'):
      if self.ent_type == 'koopa':
      if self.move_dir == 'left':
      if self.on_ground:
      if self.on_ground:
      if self.on_ground:
      if time_count % 1000 == 0:
      if type(self.images[self.index]) == img:
      kill_player(True)
      player.y1 -= player.speed_y
      player.y2 -= player.speed_y
      print_frame()
      print_frame()
      pygame.time.delay(5)
      pygame.time.delay(5)
      return True
      return True
      return {'coins':coins, 'points':points, 'lives':lives, 'goto':'game_over'}
      screen.blit(block.img.return_img(), (block.x1 - view_range, block.y1 - 8))
      self.index = 0
      self.kill()
      self.times -= 1
      self.x1 += self.speed_x
      self.x1 += self.speed_x
      self.x1 += self.speed_x
      self.x1 += self.speed_x
      self.x1 -= self.speed_x
      self.x1 -= self.speed_x
      self.x1 -= self.speed_x
      self.x1 -= self.speed_x
      self.x2 += self.speed_x
      self.x2 += self.speed_x
      self.x2 += self.speed_x
      self.x2 += self.speed_x
      self.x2 -= self.speed_x
      self.x2 -= self.speed_x
      self.x2 -= self.speed_x
      self.x2 -= self.speed_x
      self.y1 += self.speed_y
      self.y1 += self.speed_y
      self.y1 += self.speed_y
      self.y1 += self.speed_y
      self.y1 += self.speed_y
      self.y1 += self.speed_y
      self.y1 += self.speed_y
      self.y1 -= self.speed_y
      self.y1 -= self.speed_y
      self.y1 -= self.speed_y
      self.y1 -= self.speed_y
      self.y1 -= self.speed_y
      self.y1 -= self.speed_y
      self.y1 -= self.speed_y
      self.y2 += self.speed_y
      self.y2 += self.speed_y
      self.y2 += self.speed_y
      self.y2 += self.speed_y
      self.y2 += self.speed_y
      self.y2 += self.speed_y
      self.y2 += self.speed_y
      self.y2 -= self.speed_y
      self.y2 -= self.speed_y
      self.y2 -= self.speed_y
      self.y2 -= self.speed_y
      self.y2 -= self.speed_y
      self.y2 -= self.speed_y
      self.y2 -= self.speed_y
      set_view_range()
      set_view_range()
      time_count += 5
      view_range = 0
      view_range = background_width - screen_width
      view_range = player.x1 - 96
      view_range = player.x2 - screen_width + 176
    #input
    elif direction == 'down' and self.can_move('down'):
    elif direction == 'down' and self.can_move('down'):
    elif direction == 'down':
    elif direction == 'down':
    elif direction == 'down':
    elif direction == 'down':
    elif direction == 'down':
    elif direction == 'down':
    elif direction == 'right' and self.can_move('right'):
    elif direction == 'right':
    elif direction == 'right':
    elif direction == 'right':
    elif direction == 'right':
    elif direction == 'right':
    elif direction == 'right':
    elif direction == 'up' and self.can_move('up'):
    elif direction == 'up' and self.can_move('up'):
    elif direction == 'up':
    elif direction == 'up':
    elif direction == 'up':
    elif direction == 'up':
    elif direction == 'up':
    elif direction == 'up':
    elif direction == 'up':
    else:
    else:
    else:
    entities.pop(my_ID)
    for entity1_y in range(int(entity1.y1), int(entity1.y2) + 1):
    for entity_y in range(int(entity.y1), int(entity.y2) + 1):
    for event in pygame.event.get():
    global block_map
    global block_map
    global block_map
    global block_map
    global blocks
    global coins
    global entities
    global entities
    global entities
    global lives
    global points
    global points
    i = 0
    if (block_map[x1_blocks, y2_blocks] == 104) or (block_map[x2_blocks, y2_blocks] == 104):
    if (block_map[x1_blocks, y2_blocks] == 104) or (block_map[x2_blocks, y2_blocks] == 104):
    if (direction == 'side') and (not self.can_move(self.move_dir)):
    if direction == 'left' and self.can_move('left'):
    if direction == 'left':
    if direction == 'left':
    if direction == 'left':
    if direction == 'left':
    if direction == 'left':
    if direction == 'left':
    if direction == 'side':
    if lives >= 0:
    if not block.img == invisible:
    if not self.check_falling():
    if not self.check_falling():
    if not self.max_index == -1:
    if not self.max_index == -1:
    if not view_range <= 0:
    if not view_range >= (background_width - screen_width):
    if self.index > self.max_index:
    if self.times > 0:
    my_ID = entities.index(self)
    player.move('right')
    player.y1 += player.speed_y
    player.y2 += player.speed_y
    print_frame()
    print_frame()
    pygame.time.delay(5)
    pygame.time.delay(5)
    return False
    return False
    return result
    return result
    screen.blit(entity.img.return_img(), (entity.x1 - view_range, entity.y1 - 8))
    self.images = images
    self.index += 1
    self.max_index = len(images) - 1
    while i <= 48:
    x1_blocks = int((self.x1 + 16) / 16)
    x1_blocks = int(self.x1 / 16) + 1
    x1_blocks = int(self.x1 / 16) + 1
    x1_blocks = int(self.x1 / 16) + 1
    x2_blocks = int((self.x2 + 16) / 16)
    x2_blocks = int(self.x2 / 16) + 1
    x2_blocks = int(self.x2 / 16) + 1
    x2_blocks = int(self.x2 / 16) + 1
    y1_blocks = int(self.y1 / 16)
    y1_blocks = int(self.y1 / 16)
    y1_blocks = int(self.y1 / 16)
    y1_blocks = int(self.y1 / 16)
    y2_blocks = int(self.y2 / 16)
    y2_blocks = int(self.y2 / 16)
    y2_blocks = int(self.y2 / 16)
    y2_blocks = int(self.y2 / 16)
  #(x1, y1) is top-left corner, (x2, y2) is bottom-right corner
  #(x1, y1) is top-left corner, (x2, y2) is bottom-right corner
  #(x1, y1) is top-left corner, (x2, y2) is bottom-right corner
  #entity's vars
  4s = [None]
  ]
  ]
  b = Block()
  b.bonus_type = bonus
  b.img = img
  b.speed_y = speed_y
  b.times = times
  b.x1 = x
  b.x2 = x + 15
  b.y1 = y
  b.y2 = y + 15
  background_width = background.return_img().get_width() - 1
  blocks = [
  bonus_type = None
  coins = coins_in
  create_block(101*16, 9*16, 0.4, bricks, 'star_man', 1),
  create_block(106*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(109*16, 5*16, 0.4, prize, 'super_mushroom', 1),
  create_block(109*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(112*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(129*16, 5*16, 0.4, prize, 'coin', 1),
  create_block(130*16, 5*16, 0.4, prize, 'coin', 1),
  create_block(16*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(170*16, 9*16, 0.4, prize, 'coin', 1)
  create_block(21*16, 9*16, 0.4, prize, 'super_mushroom', 1),
  create_block(22*16, 5*16, 0.4, prize, 'coin', 1),
  create_block(23*16, 9*16, 0.4, prize, 'coin', 1),
  create_block(64*16, 8*16, 0.4, invisible, 'up_mushroom', 1),
  create_block(78*16, 9*16, 0.4, prize, 'super_mushroom', 1),
  create_block(94*16, 5*16, 0.4, prize, 'coin', 1),
  create_block(94*16, 9*16, 0.4, bricks, 'coin', 1),
  create_entity(107*16, 12*16-8, 0.4, 1.4, koopa, 'koopa')
  create_entity(114*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(115.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(124*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(125.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(128*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(129.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(174*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(175.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(22*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(40*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(51*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(52.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(80*16, 4*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(82*16, 4*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(97*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  create_entity(98.5*16, 12*16, 0.4, 1.4, goomba, 'goomba'),
  def __init__(self, images):
  def can_move(self, direction):
  def can_move(self, direction):
  def check_falling(self):
  def check_falling(self):
  def give_bonus(self):
  def kill(self):
  def move(self, direction):
  def move(self, direction):
  def return_img(self):
  def return_next_level(self):
  def update(self):
  e = Entity()
  e.ent_type = ent_type
  e.img = img
  e.speed_x = speed_x
  e.speed_y = speed_y
  e.started_moving = False
  e.x1 = x
  e.x2 = x + img.return_img().get_width() - 1
  e.y1 = y
  e.y2 = y + img.return_img().get_height() - 1
  elif player.x2 >= (view_range + screen_width - 176):
  ent_type = None
  entities = [
  for block in blocks:
  for entity in entities:
  for entity1_x in range(int(entity1.x1), int(entity1.x2) + 1):
  for entity_x in range(int(entity.x1), int(entity.x2) + 1):
  for j in range(len(block_map[i])):
  global background
  global blocks
  global blocks
  global coins
  global entities
  global entities
  global lives
  global lives
  global player
  global player
  global player
  global points
  global running
  global screen
  global screen_height
  global screen_width
  global sec_count
  global sec_count
  global time_count
  global time_count
  global time_count
  global view_range
  global view_range
  global view_range
  if not is_falling:
  if player.x1 <= view_range + 96:
  images = []
  img = images[0]
  img = None
  img = None
  index = 0
  inv = False
  is_jumping = False #only part of going up of the jump
  is_moving_left = False
  is_moving_right = False
  jump_height = 0
  lives -= 1
  lives = lives_in
  max_index = 0
  max_jump_height = 0
  mode = 0
  move_dir = 'left'
  on_ground = False
  on_ground = True
  p = Player()
  p.images = img
  p.img = img[0]
  p.speed_x = speed_x
  p.speed_y = speed_y
  p.x1 = x
  p.x2 = x + img[0].return_img().get_width() - 1
  p.y1 = y
  p.y2 = y + img[0].return_img().get_height() - 1
  player = create_player(42, 192, 0.5, 1.5, mario)
  player.move('down')
  points = points_in
  pygame.display.update()
  reset()
  return b
  return e
  return False
  return False
  return p
  return {'coins':coins, 'points':points, 'lives':lives, 'goto':'quit'}
  screen.blit(background.return_img(), (-view_range, 0))
  screen.blit(player.img.return_img(), (player.x1 - view_range, player.y1 - 8))
  screen.blit(txt_font.render("Coins", 0, (255, 255, 255)), (136, 8))
  screen.blit(txt_font.render("Lives", 0, (255, 255, 255)), (232, 8))
  screen.blit(txt_font.render("Points", 0, (255, 255, 255)), (40, 8))
  screen.blit(txt_font.render("Time", 0, (255, 255, 255)), (328, 8))
  screen.blit(txt_font.render(str(coins), 0, (255, 255, 255)), (136, 24))
  screen.blit(txt_font.render(str(lives), 0, (255, 255, 255)), (232, 24))
  screen.blit(txt_font.render(str(points), 0, (255, 255, 255)), (40, 24))
  screen.blit(txt_font.render(str(sec_count), 0, (255, 255, 255)), (328, 24))
  sec_count = 400
  slowed_jump = False
  speed_x = 0
  speed_x = 0
  speed_y = 0
  speed_y = 0
  speed_y = 0
  started_moving = False
  time_count = 0
  times = 1
  view_range = 0 #the x cordinate of the left side of the part you can see on the screen
  while not player.x1 >= castle_x:
  while player.y1 <= screen_height:
  while running:
  x1 = 0
  x1 = 0
  x1 = 0
  x2 = 0
  x2 = 0
  x2 = 0
  y1 = 0
  y1 = 0
  y1 = 0
  y2 = 0
  y2 = 0
  y2 = 0
#animated image class
#block's vars
#create block class
#create entity class
#create functions
#create player class
#function to check entity's ability to move
#function to check player's ability to move
#function to create block object
#function to create entity object
#function to create player object
#function to detect touch between 2 entities
#function to detect touch between player and entity/block
#function to kill player
#function to move entity
#function to move player
#function to print background
#function to reset the game
#function to set the part that is printed on the screen
#images
#main section
#player's vars
#set up pygame
background = img([pygame.image.load('textures\\background2.png')])
block_map = pygame.PixelArray(pygame.image.load('lvl1map.png'))
blocks = None
bricks = img([pygame.image.load('textures\\bricks.png')])
castle_x = 3266
class Block(object):
class Entity(object):
class img(object):
class Player(object):
coin = img([pygame.image.load('textures\coin\\0.png'), pygame.image.load('textures\coin\\1.png'), pygame.image.load('textures\coin\\2.png'), pygame.image.load('textures\coin\\1.png'), pygame.image.load('textures\coin\\0.png')])
coins = None
def create_block(x, y, speed_y, img, bonus, times):
def create_entity(x, y, speed_x, speed_y, img, ent_type):
def create_player(x, y, speed_x, speed_y, img):
def end_level():
def is_entity_touch(entity1, entity2):
def is_player_touch(entity):
def kill_player(is_falling):
def print_frame():
def reset():
def run_level(coins_in, points_in, lives_in):
def set_view_range():
empty_block = img([pygame.image.load('textures\empty_block.png')])
entities = None
fire_ball = img([pygame.image.load('textures\\fire_ball.png')])
fire_flower = img([pygame.image.load('textures\\fire_flower\\0.png'), pygame.image.load('textures\\fire_flower\\1.png'), pygame.image.load('textures\\fire_flower\\2.png'), pygame.image.load('textures\\fire_flower\\3.png')])
flag_x = 3168
for i in range(len(block_map)):
goomba = img([pygame.image.load('textures\goomba\\0.png'), pygame.image.load('textures\goomba\\1.png')])
import pygame
invisible = img([])
koopa = img([koopa_l, koopa_r])
koopa_l = img([pygame.image.load('textures\koopa\left\\0.png'), pygame.image.load('textures\koopa\left\\1.png')])
koopa_r = img([pygame.image.load('textures\koopa\\right\\0.png'), pygame.image.load('textures\koopa\\right\\1.png')])
koopa_shell = img([pygame.image.load('textures\green_shell.png')])
lives = None
mario = [mario_small, mario_super, mario_fire, mario_small_inv, mario_super_inv]
mario_fire = img([pygame.image.load('textures\mario\\fire_mario.png')])
mario_small = img([pygame.image.load('textures\mario\small_mario.png')])
mario_small_inv = img([pygame.image.load('textures\mario\invincible_small_mario\\0.png'), pygame.image.load('textures\mario\invincible_small_mario\\1.png'), pygame.image.load('textures\mario\invincible_small_mario\\2.png'), pygame.image.load('textures\mario\invincible_small_mario\\3.png')])
mario_super = img([pygame.image.load('textures\mario\super_mario.png')])
mario_super_inv = img([pygame.image.load('textures\mario\invincible_super_mario\\0.png'), pygame.image.load('textures\mario\invincible_super_mario\\1.png'), pygame.image.load('textures\mario\invincible_super_mario\\2.png'), pygame.image.load('textures\mario\invincible_super_mario\\3.png'), pygame.image.load('textures\mario\invincible_super_mario\\4.png')])
player = None
points = None
prize = img([pygame.image.load('textures\prize_block\\0.png'), pygame.image.load('textures\prize_block\\1.png'), pygame.image.load('textures\prize_block\\2.png'), pygame.image.load('textures\prize_block\\1.png'), pygame.image.load('textures\prize_block\\0.png')])
pygame.init()
reset()
running = True
screen = pygame.displa`123y.set_mode((screen_width, screen_height))
screen_height = background.return_img().get_height()
screen_width = 400
sec_count = None
star_man = img([pygame.image.load('textures\star_man\\0.png'), pygame.image.load('textures\star_man\\1.png'), pygame.image.load('textures\star_man\\2.png'), pygame.image.load('textures\star_man\\3.png')])
super_mushroom = img([pygame.image.load('textures\super_mushroom.png')])
time_count = None
txt_font = pygame.font.SysFont('Arial', 16, True)
up_mushroom = img([pygame.image.load('textures\\1_up_mushroom.png')])
view_range = None*