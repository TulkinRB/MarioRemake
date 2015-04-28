import Level1
import Menu
import Inst
coins = None
points = None
lives = None
running = True

def reset():
	global coins
	global points
	global lives
	global goto
	coins = 0
	points = 0
	lives = 3
	goto = 'menu'

reset()

while running:
	if goto == 'menu':
		goto = Menu.run_level()
	elif goto == 'play':
		returned = Level1.run_level(coins, points, lives)
		coins = returned['coins']
		points = returned['points']
		lives = returned['lives']
		goto = returned['goto']
	elif goto == 'quit':
		running = False
	else:
		goto = 'menu'