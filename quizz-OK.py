#dev Hamdy Abou El Anein
from tkinter import *
from tkinter import messagebox 

class Problem(object):
  def __init__(self, question = "", a = "", b = "", c = "", correct = ""):
    object.__init__(self)
    self.question = question
    self.a = a
    self.b = b
    self.c = c
    self.correct = correct
    
class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    self.problems = []
    self.counter = 0

    self.addComponents()
    self.loadProblems()
    
    self.showProblem(0)
    
    self.mainloop()
    
  def addComponents(self):


    self.title("Quiz Scrum Master")

    self.grid()
    self.columnconfigure(0, minsize = 100)
    self.columnconfigure(1, minsize = 200)
    self.columnconfigure(2, minsize = 100)

    self.lblQuestion = Label(self, text = "Question")
    self.lblQuestion.grid(columnspan = 3, sticky = "we")
    
    self.btnA = Button(self, text = "A", command = self.checkA)
    self.btnA.grid(columnspan = 3, sticky = "we")
    
    self.btnB = Button(self, text = "B", command = self.checkB)
    self.btnB.grid(columnspan = 3, sticky = "we")
    
    self.btnC = Button(self, text = "C", command = self.checkC)
    self.btnC.grid(columnspan = 3, sticky = "we")
    
    self.btnPrev = Button(self, text = "prev", command = self.prev)
    self.btnPrev.grid(row = 4, column = 0)
    
    self.lblCounter = Label(self, text = "0")
    self.lblCounter.grid(row = 4, column = 1)
    
    self.btnNext = Button(self, text = "next", command = self.next)
    self.btnNext.grid(row = 4, column = 2)
    
  def checkA(self):
    self.check("A")

  def checkB(self):
    self.check("B")

  def checkC(self):
    self.check("C")
    
  def check(self, guess):

    correct = self.problems[self.counter].correct
    if guess == correct:
      messagebox.showinfo("Quiz", "Good Answer")
    else:
      messagebox.showinfo("Quiz", "Wrong answer.")
      
  def prev(self):
    self.counter -= 1
    if self.counter < 0:
      self.counter = 0
    self.showProblem(self.counter)
    
  def next(self):
    self.counter += 1
    if self.counter >= len(self.problems):
      self.counter = len(self.problems) - 1
    self.showProblem(self.counter)

  def showProblem(self, counter):
    self.lblQuestion["text"] = self.problems[counter].question
    self.btnA["text"] = self.problems[counter].a
    self.btnB["text"] = self.problems[counter].b
    self.btnC["text"] = self.problems[counter].c
    self.lblCounter["text"] = self.counter

  def loadProblems(self):
    self.problems.append(Problem(
      "When is a Sprint over ?",
      "When all the tasks are completed.",
      "When all Product Backlog items meet their definition of done.",
      "When the time-box expires.",
      "C"))
  
    self.problems.append(Problem(
      "What is the main reason for the Scrum Master to be at the Daily Scrum?",
      "To make sure every team member answers the three questions.",
      "He or she does not have to be there; he or she only has to ensure the Development Team has a Daily Scrum.",
      "To write down any changes to the Sprint Backlog, including adding new items, and tracking  progress on the burn-down.",
      "B"))
  
    self.problems.append(Problem(
      "It is mandatory that the product increment be released to production at the end of each Sprint.",
      "True",
      "False",
      "",
      "B"))
  
    self.problems.append(Problem(
      "When might a Sprint be abnormally terminated?",
      "When it becomes clear that not everything will be finished by the end of the Sprint.",
      "When the sales department has an important new opportunity.",
      "When the Sprint Goal becomes obsolete.",
      "C"))
  
    self.problems.append(Problem(
      "Which statement best describes a Product Owner's responsibility?",
      "Optimizing the value of the work the Development Team does.",
      "Managing the project and ensuring that the work meets the commitments to the stakeholders.",
      "Directing the Development Team.",
      "A"))
  
    
def main():
  a = App()
  
if __name__ == "__main__":
  main()
  
