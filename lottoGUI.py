''' program: lottoGUI.py
    Author: Jami Seid
    Date: 4/26/21
    *** 
    Practice Python Final 4/26/2021: Lotto Number Generator Create a
    GUI-based application using breezypythongui.  This application should
    allow the user to click a command button and have the application
    display a series of random numbers that they could conceivably to make
    their Powerball Lotto number picks. The app should generate and
    display FIVE random numbers for the main number as well as one
    PowerBall number. The FIVE "main" numbers are in a range of 1 to 69
    and the PowerBall range is from 1 *** '''

from breezypythongui import EasyFrame
import random

class LottoGUI(EasyFrame):
  """Display greeting in widgets."""
  def __init__(self):
    """sets up window and the widgets."""
    EasyFrame.__init__(self, title = "lotto Number Generator", resizable = False, background = "lightblue")
    self.addLabel(text = "lotto Number Generator", row = 0, column = 0, columnspan = 5, sticky = "NSEW", background = "lightyellow")
    self.addLabel(text = "Here are your 5 standard numbers:", row = 1, column = 0, columnspan = 5, sticky = "NSEW", background = "lightblue")
    self.numPanel = self.addPanel(row = 2, column = 0, background = "lightblue")
    self.field1 = self.addIntegerField(value = 0, row = 2, column = 0, width = 3)
    self.field2 = self.addIntegerField(value = 0, row = 2, column = 1, width = 3)
    self.field3 = self.addIntegerField(value = 0, row = 2, column = 2, width = 3)
    self.field4 = self.addIntegerField(value = 0, row = 2, column = 3, width = 3)
    self.field5 = self.addIntegerField(value = 0, row = 2, column = 4, width = 3)
    self.addLabel(text = "Your Powerball number is:", row = 3, column = 0,  columnspan = 3, sticky = "NSEW", background = "lightblue")
    self.pBall = self.addIntegerField(value = 0, row = 3, column = 1, columnspan = 5, width = 3)
    self.addButton(text = "Pick numbers", row = 4,  column = 0, columnspan = 5, command = self.pickNumbers)


  def pickNumbers(self):
    num1 = random.randint(1, 69)    
    num2 = random.randint(1, 69)
    num3 = random.randint(1, 69)
    num4 = random.randint(1, 69)
    num5 = random.randint(1, 69)
    power = random.randint(1, 26)

    # now take those random number variables and update the fields of the GUI
    self.field1.setNumber(num1)
    self.field2.setNumber(num2)
    self.field3.setNumber(num3)
    self.field4.setNumber(num4)
    self.field5.setNumber(num5)
    self.pBall.setNumber(power)

# definition of the main() function for program entry
def main():
	""" instantiates and pops up the window."""
	LottoGUI().mainloop()


#globel call to the main() function
main()