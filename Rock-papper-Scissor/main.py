from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import random

Builder.load_file("main.kv")


class Game(Widget):
	
	check = ObjectProperty(None)
	pcimage = ObjectProperty(None)
	userimage = ObjectProperty(None)
	
	def rock(self):
		Rock = "img/rock.jpg"
		Papper = "img/papper.png"
		Scissor = "img/scissor.jpg"
		images = [Rock ,Papper ,Scissor]
		self.userimage.source = Rock
		self.pcimage.source = random.choice(images)
		# Check who won
		if self.pcimage.source == Papper:
			self.check.text = "You lose!"
		elif self.pcimage.source == Scissor:
			self.check.text = "You win!"
		else:
			self.check.text = "Draw!"
	
	def papper(self):
		Rock = "img/rock.jpg"
		Papper = "img/papper.png"
		Scissor = "img/scissor.jpg"
		images = [Rock ,Papper ,Scissor]
		self.userimage.source = Papper
		self.pcimage.source = random.choice(images)
		# Check who won
		if self.pcimage.source == Scissor:
			self.check.text = "You lose!"
		elif self.pcimage.source == Rock:
			self.check.text = "You win!"
		else:
			self.check.text = "Draw!"

	def scissor(self):
		Rock = "img/rock.jpg"
		Papper = "img/papper.png"
		Scissor = "img/scissor.jpg"
		images = [Rock ,Papper ,Scissor]
		self.userimage.source = Scissor
		self.pcimage.source = random.choice(images)
		# Check who won
		if self.pcimage.source == Rock:
			self.check.text = "You lose!"
		elif self.pcimage.source == Papper:
			self.check.text = "You win!"
		else:
			self.check.text = "Draw!"

class MainApp(App):
	def build(self):
		return Game()

if __name__ == '__main__':
	MainApp().run()