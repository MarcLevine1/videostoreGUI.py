"""
Program: videostoreGUI.py
Author: Marc Levine 11/18/2021

*** Note: this file breezypythongui.py MUST be in the same directory as the file for the application to work.
***
"""
from breezypythongui import EasyFrame
from tkinter.font import Font

class VideoStore(EasyFrame):
	 
	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Video Store", width = 380, height = 260, background = "SteelBlue")
		self.addLabel(text = "Welcome to Five star Retro Video", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "SteelBlue", font = Font(family = "Times New Roman", size = 18))

		self.addLabel(text = "Price for Old videos: $2.00", row = 1, column = 0, background = "SteelBlue")
		self.addLabel(text = "Price for New videos: $3.00", row = 2, column = 0, background = "SteelBlue")

		self.addLabel(text = "No. of old videos:", row = 3, column = 0, background = "SteelBlue")
		self.oldRental = self.addIntegerField(value = 0, row = 3, column = 1)
		# if want to add color     self.oldRental[Red]

		self.addLabel(text = "No. of new videos:", row = 4, column = 0, background = "SteelBlue")
		self.newRental = self.addIntegerField(value = 0, row = 4, column = 1)

		#command line
		self.addButton(text = "Calculate", row = 5, column = 0, columnspan = 2, command = self.total)
		
		# Empty label to use with the program's outcome
		self.outputLabel = self.addLabel(text = "", row = 6, column = 0, columnspan = 2, sticky = "NSEW", background = "SteelBlue")

	# Event handling method	
	def total(self):
		NEW_VIDEO = 3.00
		OLD_VIDEO = 2.00

		# Grab the input values from the entry fields
		oldNum = self.oldRental.getNumber()
		newNum = self.newRental.getNumber()

		# calculate the total
		totalCost = (NEW_VIDEO * newNum) + (OLD_VIDEO * oldNum)

		# Output to the GUI window using tabular method
		self.outputLabel["text"] = "The total cost is: $%0.2f" % (totalCost) 
		self.outputLabel["background"] = "Khaki" 
		self.outputLabel["foreground"] = "red"



# definition of the main() function for program entry
def main():
	"""Instantiation and pop up the window."""
	VideoStore().mainloop()

# global call to trigger the main() function
if __name__ == "__main__":
	main()			