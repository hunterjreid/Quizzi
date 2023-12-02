#prerequisites
import random
import webbrowser
import warnings
from tkinter import *
from tkinter import filedialog

window = Tk() 
window.geometry("400x600")
window.resizable(width=False, height=False)
window.configure(bg="white") 
window.title("QUIZZI")

name = StringVar()

background = "white"
primary_text = "black"
secondary_text = "grey"
button_color = "red"





#function to clear the screen off widgets
#to be used when switching EG: menu --> help
def clear():
    list = window.place_slaves()
    for n in list:  
        n.destroy()

#function for the Quiz
class Quiz:
    def  __init__(self,quest):
        clear()
        #define necessary variables.
        self.questions = []
        for n in quest:
            self.questions.append(n)
        self.a1 = ""
        self.a2 = ""
        self.a3 = ""
        self.a4 = ""
        self.Ra = ""
        #defining vars. 
        self.RaBtn = Button(window, text="", font=("Arial", 13))
        self.antw1 = Button(window, text="", font=("Arial", 13))
        self.antw2 = Button(window, text="", font=("Arial", 13))
        self.antw3 = Button(window, text="", font=("Arial", 13))
        self.antw4 = Button(window, text="", font=("Arial", 13))
        self.lock = False
        self.right = 0
        #next button
        self.next = Button(window, text="Next", font=("Arial", 13), width=15, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white", command=self.QuestionQuery)
        self.number = 0
        self.max = len(self.questions)
        self.QuestionQuery()
    def QuestionQuery(self):
        #place the Next button
        self.next.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        #for the length of questions
        if len(self.questions) > 0 and self.number < self.max:
            self.number += 1
            self.lock = False
            randNum = random.randint(0,len(self.questions)-1)
            questionText = self.questions[randNum][0]
            self.Ra = self.questions[randNum][-1]
            answers = []
            for i in range(1,5):
                answers.append(self.questions[randNum][i])
            random.shuffle(answers)

            self.a1 = answers[0]
            self.a2 = answers[1]
            self.a3 = answers[2]
            self.a4 = answers[3]

            #Place the question in the question Box.
            QuestionQuery = Text(window, font=("Arial", 16), width=27, height=2, bd=0, fg=primary_text, bg=button_color)
            QuestionQuery.insert(END, questionText)
            QuestionQuery.place(relx=0.5, rely=0.2, anchor=CENTER)


            self.page_text = str(self.number) + "/" + str(self.max)

            self.label = Label(window, font=("Arial", 16), text=self.page_text, bg=background, fg=primary_text,wraplength=375)
            self.label.place(relx=0.5, rely=0.01, anchor=N)



            #Define buttons for the options.
            self.antw1 = Button(window, text=self.a1, font=("Arial", 13), width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white", command = self.control1)
            self.antw2 = Button(window, text=self.a2, font=("Arial", 13), width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white", command = self.control2)
            self.antw3 = Button(window, text=self.a3, font=("Arial", 13), width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white", command = self.control3)
            self.antw4 = Button(window, text=self.a4, font=("Arial", 13), width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white", command = self.control4)
            #Place buttons for the options.
            self.antw1.place(relx=0.5, rely=0.60, anchor=CENTER)
            self.antw2.place(relx=0.5, rely=0.67, anchor=CENTER)
            self.antw3.place(relx=0.5, rely=0.74, anchor=CENTER)
            self.antw4.place(relx=0.5, rely=0.81, anchor=CENTER)


            #cycle though which option is correct.
            if self.a1 == self.Ra:
                self.RaBtn = self.antw1
            elif self.a2 == self.Ra:
                self.RaBtn = self.antw2
            elif self.a3 == self.Ra:
                self.RaBtn = self.antw3
            elif self.a4 == self.Ra:
                self.RaBtn = self.antw4
            self.questions.pop(randNum)
        else:
            clear()
            #Runs when quiz has finished. All questions have been awnsered.
            lb = Label(window, font=("Arial", 25), text=str(self.right) + " / " + str(self.max), bg=background, fg=primary_text)
            self.middleText = ""

            if ((self.max*1)==self.right):
                #if they get everything correct.
                self.middleText = "100%, impressive " + name.get()
            elif (self.right > (self.max*0.70)):
                #if they get more than 70% correct.
                self.middleText = "Congratulations " + name.get() + " you did very good, better than I thought."
            elif (self.right > (self.max*0.40)):
                #if they get more than 40% correct.
                self.middleText = "Well, " + name.get() + " that was an OK attempt."
            else:
                #if they get less than 40% correct.
                self.middleText = name.get()+", that was a poor effort"
            
            self.label = Label(window, font=("Arial", 13), text=self.middleText, bg=background, fg=secondary_text, wraplength=375)
            self.label.place(relx=0.5, rely=0.45, anchor=CENTER)

            lb.place(relx=0.5, rely=0.15, anchor=CENTER)

            goMenu = Button(window, text="Menu", font=("Arial", 13), command=menuGen, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
            goMenu.place(relx=0.5, rely=0.77, anchor=CENTER)
            share = Button(window, text="Share your score", font=("Arial", 13), command=shareRes, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=secondary_text, activeforeground="white")
            share.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    #Change color if right or wrong.
    def control1(self):
        if self.lock == False:
            if self.Ra != self.a1:
                self.antw1.configure(bg="red")
            else:
                self.antw1.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True

    #Change color if right or wrong.
    def control2(self):
        if self.lock == False:
            if self.Ra != self.a2:
                self.antw2.configure(bg="red")
            else:
                self.antw2.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True
    #Change color if right or wrong.
    def control3(self):
        if self.lock == False:
            if self.Ra != self.a3:
                self.antw3.configure(bg="red")
            else:
                self.antw3.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True
    #Change color if right or wrong.
    def control4(self):
        if self.lock == False:
            if self.Ra != self.a4:
                self.antw4.configure(bg="red")
            else:
                self.antw4.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True

class Menu:
    def __init__(self):
        clear()
        #define the widgets styles and attributes
        
        quiz_loaded_text = "Quiz Loaded: " + quiz_name + " created by " + creator_name
        quiz_text = "Loaded Quiz: " + quiz_name

        self.title = Label(window, font=('Arial', 9), text=quiz_loaded_text, bg=background, fg=secondary_text, wraplength=375)
        self.title.place(relx=0.5, rely=0, anchor=N)
        
        #name label
        self.label = Label(window, font=('Comic Sans MS', 45), text="Quizzi", bg=background, fg=primary_text)
        self.label.place(relx=0.5, rely=0.3, anchor=CENTER)

        #name footer label
        self.quizLabel = Label(window, font=("Arial", 12), text=quiz_text, bg=background, fg=primary_text, wraplength=375)
        self.quizLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

        #start button
        self.btn = Button(window, text="Play Game", font=("Arial", 13), command=quizGen, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn.place(relx=0.5, rely=0.6, anchor=CENTER)

        #help button
        self.btn = Button(window, text="Help", font=("Arial", 13), command=helpGen, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn.place(relx=0.5, rely=0.7, anchor=CENTER)

        #exit button
        self.btn = Button(window, text="Exit", font=("Arial", 13), command=close_window, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn.place(relx=0.5, rely=0.8, anchor=CENTER)

        #self.lb.grid(column=0,row=0,padx=150,pady=0)
        #self.QuizBtn.grid(column=0,row=2)

class AskName:
    def __init__(self):
        clear()
        #define the widgets styles and attributes
        #welcome label
        self.label = Label(window, font=("Arial", 20), text="Welcome to Quizzi, fellow Quizzer!", bg=background, fg=primary_text, wraplength=375)
        self.label.place(relx=0.5, rely=0.15, anchor=CENTER)

        #welcome text
        self.helpText = "So, what can we call you today?"
        self.label = Label(window, font=("Arial", 13), text=self.helpText, bg=background, fg=secondary_text, wraplength=375)
        self.label.place(relx=0.5, rely=0.45, anchor=CENTER)

        #input text
        self.text_getName = Entry(window, font=("Arial", 14), textvariable=name, width=20, bd=0, bg=button_color, fg=primary_text)
        self.text_getName.place(relx=0.5, rely=0.5, anchor=CENTER)  

        #next btn
        self.btn = Button(window, text="Next", font=("Arial", 13), command=menuGen, width=30, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn.place(relx=0.5, rely=0.9, anchor=CENTER)

class Help:
    def __init__(self):
        clear()
        #define the widgets styles and attributes
        #help label
        self.label = Label(window, font=("Arial", 16), text="Helpful Menu", bg=background, fg=primary_text)
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)

        #help text
        self.helpText = "Welcome to Quizzi, the premise of Quizzi is really quite simple.\n Answer as many questions as you can correctly. That's it!\n\n Start by trying our default '50 Locations' quiz or try your luck with "
        self.helpText += "some harder quizes created by other quizzers.\n\n TIP: Download the 'config' file from https://quiz-let.com/quiz/browse\n and replace to activate the new quiz\n\nHappy quizzing everyone :)"
        self.label = Label(window, font=("Arial", 13), text=self.helpText, bg=background, fg=secondary_text, wraplength=375)
        self.label.place(relx=0.5, rely=0.45, anchor=CENTER)

        #back button
        self.btn = Button(window, text="Back", font=("Arial", 13), command=menuGen, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn.place(relx=0.5, rely=0.9, anchor=CENTER)



#functions.
#ask name
def askNameGen():
    AskName()

#Gen Menu
def menuGen():
    #If they didnt choose a name, Set there name to Quizzer
    if name.get()=="":
        name.set("Fellow Quizzer")
    Menu()

#Help screen
def helpGen():
    Help()  


#Start Quiz function
def quizGen():
    Quiz(questions)

#close
def close_window(): 
    window.destroy()

#Share
url = "https://www.twitter.com"
def shareRes(): 
    webbrowser.open(url,new=1)

def test(): 
    print(quiz_name)



#First screen to be ask name.


# Open config file
f = open(filedialog.askopenfilename(title = "Select Config file",filetypes=[("Text files", ".txt")]),'r')
raw_config = ""
#READ config file
while 1:
    line = f.readline()
    if not line:break
    raw_config += line
#close config file after reading, not nessary but a good programming habit.
f.close()
#split config file
split_config = raw_config.split("/")
#grab metadata 
metadata = split_config[0].split(",")
#set metadata
quiz_name, creator_name, background, primary_text, secondary_text, button_color = metadata[0], metadata[1], metadata[2], metadata[3], metadata[4], metadata[5]
#change background
window.configure(bg=metadata[2]) 
del split_config[0]
questions_list = split_config
questions = []
for i in range(len(questions_list)):
    a = questions_list[i].split(",")
    print(a)
    questions += [a]


askNameGen()
window.mainloop()
    
    