class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bd= Song(["Happy birthday to you",
		"I dont want to get sued",
		"so i'll stop it rigth there"])


bulls_on_parede = Song(["There rally around the family",
			"With pockets full of shells"])


happy_bd.sing_me_a_song()
bulls_on_parede.sing_me_a_song()
