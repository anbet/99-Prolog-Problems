class Scene(object):
	def enter(self):
		pass

class Engine(object):
	def __init__(self, scene_map):
		pass

	def play(self):
		pass

class Death(Scene):
	
	def enter(self):
		pass

class Centralcorridor(Scene):

	def enter(self):
		pass

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass


class Map(object):

	def __int__(self, start_scene): 
		self.strat_scene = strat_scene 
		
	

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		print self.start_scene



a_map= Map("Central_corridor")
var=a_map.opening_scene()
print var


a_game= Engine(a_map)
a_game.play()
