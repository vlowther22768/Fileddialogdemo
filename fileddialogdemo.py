from breezypythongui import EasyFrame
import tkinter.filedialog

class FileDialogDemo(EasyFrame):
# definition of the __init__() method which is our class construtor
	def __init__(self):
		#call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "File Dialog Demo")
		self.outputArea = self.addTextArea(text = "", row = 0, column = 0, width = 80, height = 15)
		self.addButton(text = "Open", row = 1, column = 0, command = self.openFile)
# Event handling method 
	def openFile(self):
		"""Pops ip an open file dialog box, and if a file is selected, displays its
		text in the text are of the GUI and its pathname in the title bar."""
		fList = [("Python files", "*.py"), ("Text files", "*.txt"),("Web Documents", "*.html")]
		fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)

	#only go through the process of reading file data if the filename is NOT an empty string 
		if fileName != "":
			file = open(fileName, "r")
			text = file.read()
			file.close()
			self.outputArea.setText(text)
			self.setTitle(fileName)

def main():
	FileDialogDemo().mainloop()

main()