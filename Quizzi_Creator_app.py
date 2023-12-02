#prerequisites
import random
import webbrowser
import warnings
from tkinter import *
from tkinter import filedialog

window = Tk() 
window.geometry("400x600")
window.resizable(width=False, height=False)
window.title("QUIZZI Creator")


global background
global primary_text
global secondary_text
global button_color
background, primary_text, secondary_text, button_color = "#222326","#DCDCDC","#a5a48b","#474747"
created_quizname, created_bg, created_color, created_creator, created_secondary, created_primary = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

created_quizname.set("My Quiz")
created_creator.set("Fellow Quizzer")
created_bg.set("#222326")
created_primary.set("#DCDCDC")
created_secondary.set("#a5a48b")
created_color.set("#474747")

global created_questions
created_questions = [['Get started by typing a question here.', '','','',''],['Add your second question here.', '','','','']]
created_question, created_correct,created_dummy1,created_dummy2,created_dummy3 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

window.configure(bg=background) 

def openGen():
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

    created_quizname.set(metadata[0])
    created_creator.set(metadata[1])
    created_bg.set(metadata[2])
    created_primary.set(metadata[3])
    created_secondary.set(metadata[4])
    created_color.set(metadata[5])

    global background
    global primary_text
    global secondary_text
    global button_color
    background, primary_text, secondary_text, button_color = created_bg.get(),created_primary.get(),created_secondary.get(),created_color.get()
    window.configure(bg=background) 


    #change background
    window.configure(bg=metadata[2]) 
    del split_config[0]
    questions_list = split_config

    global created_questions
    created_questions = []
    for i in range(len(questions_list)):
        a = questions_list[i].split(",")
        print(a)
        created_questions += [a]
    Menu()

#function to clear the screen off widgets
#to be used when switching EG: menu --> edit questions.
def clear():
    list = window.place_slaves()
    for n in list:  
        n.destroy()

class Menu:
    def __init__(self):
        clear()
        #define the widgets styles and attributes

        quiz_loaded_text = "Editing Quiz: " + created_quizname.get()
        self.title = Label(window, font=('Arial', 12), text=quiz_loaded_text, bg=background, fg=secondary_text, wraplength=375)
        self.title.place(relx=0.5, rely=0, anchor=N)

        #name label
        self.label = Label(window, font=('Comic Sans MS', 35), text="Quizzi Creator", bg=background, fg=primary_text)
        self.label.place(relx=0.5, rely=0.3, anchor=CENTER)

        #edit button
        self.btn_edit = Button(window, text="Edit Questions", font=("Arial", 13), command=editQuizGen, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn_edit.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.btn = Button(window, text="Edit Quiz Metadata", font=("Arial", 13), command=metadataGen, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.btn_save = Button(window, text="Save as", font=("Arial", 13), command=saveGen, width=10, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn_save.place(relx=0.9, rely=0.8, anchor=E)

        self.btn_open = Button(window, text="Open file", font=("Arial", 13), width=10, command =openGen, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn_open.place(relx=0.5, rely=0.8, anchor=CENTER)  

        self.btn_reset = Button(window, text="Reset ALL", font=("Arial", 13), width=10, command =reset_all, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn_reset.place(relx=0.1, rely=0.8, anchor=W)
 




global page
global lastPage
page = 1
lastPage = -1
class EditQuiz: 
    def __init__(self):


        global page
        if page < 1:
            page = 1
            print("ERROR")
            self.loadPage(page)

        self.loadPage(page)



    def prev(self):
        # define global variables so we can modify them!
        global page
        global lastPage

        # if on last page (eg: 18/18 or 25/25), and nothing was entered, remove from array.
        if page == len(created_questions):
            index = len(created_questions) - 1
            if (created_question.get() == "" and created_correct.get() == "" and created_dummy1.get() == "" and created_dummy2.get() == "" and created_dummy3.get() == ""):
                del created_questions[index]
                # making lastPage equal to "-1" doesn't save anything to the array,
                # otherwise it would save something that doesn't exist.
                lastPage = -1

        # this guarantees the page number won't go negative.
        if page > 1:
            # load the previous page.
            page -= 1
            self.loadPage(page)

    def ford(self):
        # define global variables so we can modify them.
        global page
        global lastPage

        totalPages = len(created_questions)

        # since the user wants to go ford, if we are on the last page add another question.
        if page == totalPages:
            empty_question = ['', '', '', '', '']
            created_questions.append(empty_question)
        
        page += 1

        # failsafe. just incase the array is completely empty, shouldn't happen.
        if totalPages == 0:
            page,lastPage = 1,1
            empty_question = ['This was a error, but i fixed it', '', '', '', '']   
            created_questions.append(empty_question)


        
        self.loadPage(page)
        
    def loadPage(self, page):
        clear()
        global lastPage

                

        if not (lastPage == -1):
            # save question
            self.questionToAdd_array = [created_question.get(),created_dummy1.get(),created_dummy2.get(),created_dummy3.get(),created_correct.get()]
            created_questions.pop(lastPage-1)
            created_questions.insert(lastPage-1, self.questionToAdd_array)

        # update all text fields. fetching from question array
        created_question.set(created_questions[page-1][0])
        created_correct.set(created_questions[page-1][4])
        created_dummy1.set(created_questions[page-1][1])    
        created_dummy2.set(created_questions[page-1][2])
        created_dummy3.set(created_questions[page-1][3])

        lastPage = page

        self.btn = Button(window, text="Main Menu", font=("Arial", 13), command=menuGenSaveQuestions, width=10, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn.place(relx=0.1, rely=0.9, anchor=W)

        self.btn_back = Button(window, text="⟵", font=("Arial", 13), width=10, command = self.prev, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn_ford = Button(window, text="⟶", font=("Arial", 13), width=10, command = self.ford, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        
        self.btn_ford.place(relx=0.9, rely=0.9, anchor=E)
        self.btn_back.place(relx=0.5, rely=0.9, anchor=CENTER)  

        self.page = page
        self.length = len(created_questions)
        self.page_text = str(self.page) + "/" + str(self.length)

        self.label = Label(window, font=("Arial", 16), text=self.page_text, bg=background, fg=primary_text)
        self.label.place(relx=0.5, rely=0.01, anchor=N)

        self.quiz_question_label = Label(window, font=("Arial", 12), text="Question:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_question_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.quiz_question = Entry(window, width=35,textvariable=created_question, font=("Helvetica", 13))
        self.quiz_question.place(relx=0.5, rely=0.15, anchor=CENTER)
        
        self.quiz_correct_label = Label(window, font=("Arial", 12), text="Correct Answer:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_correct_label.place(relx=0.02, rely=0.4, anchor=W)
        self.quiz_correct = Entry(window, width=24,textvariable=created_correct, font=("Helvetica", 13))
        self.quiz_correct.place(relx=0.98, rely=0.4, anchor=E)

        self.quiz_dummy1_label = Label(window, font=("Arial", 12), text="Dummy Answer:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_dummy1_label.place(relx=0.02, rely=0.45, anchor=W)
        self.quiz_dummy1 = Entry(window, width=24,textvariable=created_dummy1, font=("Helvetica", 13))
        self.quiz_dummy1.place(relx=0.98, rely=0.45, anchor=E)

        self.quiz_dummy2_label = Label(window, font=("Arial", 12), text="Dummy Answer:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_dummy2_label.place(relx=0.02, rely=0.5, anchor=W)
        self.quiz_dummy2 = Entry(window, width=24,textvariable=created_dummy2, font=("Helvetica", 13))
        self.quiz_dummy2.place(relx=0.98, rely=0.5, anchor=E)

        self.quiz_dummy3_label = Label(window, font=("Arial", 12), text="Dummy Answer:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_dummy3_label.place(relx=0.02, rely=0.55, anchor=W)
        self.quiz_dummy3 = Entry(window, width=24,textvariable=created_dummy3, font=("Helvetica", 13))
        self.quiz_dummy3.place(relx=0.98, rely=0.55, anchor=E)

class Metadata:
    def __init__(self):
        clear()
        #define the widgets styles and attributes

        self.label = Label(window, font=("Arial", 16), text="Edit Metadata", bg=background, fg=primary_text)
        self.label.place(relx=0.5, rely=0.01, anchor=N)

        self.quiz_nameLabel = Label(window, font=("Arial", 12), text="Quiz Name:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_nameLabel.place(relx=0.02, rely=0.3, anchor=W)
        self.quiz_name = Entry(window, textvariable=created_quizname, width=24, font=("Helvetica", 13))
        self.quiz_name.place(relx=0.98, rely=0.3, anchor=E)
        
 
        self.quiz_creatorLabel = Label(window, font=("Arial", 12), text="Creator Name:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_creatorLabel.place(relx=0.02, rely=0.35, anchor=W)
        self.quiz_creator = Entry(window, width=24,textvariable=created_creator, font=("Helvetica", 13))
        self.quiz_creator.place(relx=0.98, rely=0.35, anchor=E)

        self.quiz_bgLabel = Label(window, font=("Arial", 12), text="Background Color:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_bgLabel.place(relx=0.02, rely=0.4, anchor=W)
        self.quiz_bg = Entry(window, width=24,textvariable=created_bg, font=("Helvetica", 13))
        self.quiz_bg.place(relx=0.98, rely=0.4, anchor=E)

        self.quiz_primary_text_label = Label(window, font=("Arial", 12), text="Primary Text Color:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_primary_text_label.place(relx=0.02, rely=0.45, anchor=W)
        self.quiz_primary_text = Entry(window, width=24,textvariable=created_primary, font=("Helvetica", 13))
        self.quiz_primary_text.place(relx=0.98, rely=0.45, anchor=E)

        self.quiz_second_text_label = Label(window, font=("Arial", 12), text="Secondary Text Color:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_second_text_label.place(relx=0.02, rely=0.5, anchor=W)
        self.quiz_second_text = Entry(window, width=24,textvariable=created_secondary, font=("Helvetica", 13))
        self.quiz_second_text.place(relx=0.98, rely=0.5, anchor=E)

        self.quiz_btn_color_label = Label(window, font=("Arial", 12), text="Button Color:", bg=background, fg=primary_text, wraplength=375)
        self.quiz_btn_color_label.place(relx=0.02, rely=0.55, anchor=W)
        self.quiz_btn_color= Entry(window, width=24,textvariable=created_color, font=("Helvetica", 13))
        self.quiz_btn_color.place(relx=0.98, rely=0.55, anchor=E)


        self.preset_label = Label(window, font=("Arial", 12), text="Theme presets:", bg=background, fg=secondary_text, wraplength=375)
        self.preset_label.place(relx=0.5, rely=0.7, anchor=CENTER)

        
        self.preset_old = Button(window, text="Default", font=("Arial", 13), command=preset_oringal, width=8, height=1, bd=0, bg="#474747", activebackground="#696969", fg="#DCDCDC", activeforeground="white")
        self.preset_old.place(relx=0.2, rely=0.76, anchor=CENTER)

        self.preset_light = Button(window, text="Light", font=("Arial", 13), command=preset_light, width=8, height=1, bd=0, bg="#8C8C8C", activebackground="#696969", fg="white", activeforeground="grey")
        self.preset_light.place(relx=0.4, rely=0.76, anchor=CENTER)

        self.preset_dark = Button(window, text="Dark", font=("Arial", 13), command=preset_dark, width=8, height=1, bd=0, bg="#111111", activebackground="#696969", fg="#BDBDBD", activeforeground="white")
        self.preset_dark.place(relx=0.6, rely=0.76, anchor=CENTER)

        self.preset_army = Button(window, text="Army", font=("Arial", 13), command=preset_army, width=8, height=1, bd=0, bg="#226544", activebackground="#696969", fg="#a5a48b", activeforeground="white")
        self.preset_army.place(relx=0.8, rely=0.76, anchor=CENTER)

        self.preset_gold = Button(window, text="Golden", font=("Arial", 13), command=preset_gold, width=8, height=1, bd=0, bg="gold", activebackground="#696969", fg="black", activeforeground="white")
        self.preset_gold.place(relx=0.2, rely=0.813, anchor=CENTER)

        self.preset_random = Button(window, text="Random", font=("Arial", 13), command=preset_random, width=8, height=1, bd=0, bg="lightblue", activebackground="#696969", fg="red", activeforeground="green")
        self.preset_random.place(relx=0.4, rely=0.813, anchor=CENTER)

        # self.btn_back = Button(window, text="⟵", font=("Arial", 13), width=10, command = self.prev, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        # self.btn_ford = Button(window, text="⟶", font=("Arial", 13), width=10, command = self.ford, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        

        self.btn = Button(window, text="Back and Save Changes", font=("Arial", 13), command=menuGenSavedata, width=35, height=1, bd=0, bg=button_color, activebackground="#696969", fg=primary_text, activeforeground="white")
        self.btn.place(relx=0.5, rely=0.9, anchor=CENTER)

#functions.
#ask name

#Gen Menu
def menuGen():
    #If they didnt choose a name, Set there name to Quizzer
    Menu()

#Help screen
def metadataGen():
    Metadata()  

def menuGenSaveQuestions():
    global lastPage
    global created_questions
    global page

    print(lastPage)
    if not (lastPage == -1):
        question_array = [created_question.get(),created_dummy1.get(),created_dummy2.get(),created_dummy3.get(),created_correct.get()]
        if question_array != ['','','','','']:
            # insert the last question into array.
            created_questions.pop(lastPage-1)
            created_questions.insert(lastPage-1, question_array)
            print("INSERTING: "+ str(question_array))
        else:
            # excutes when the question is completely empty.
            # created_questions.pop(page-1)
            # print("Popping->>" + str(page-1))
            # lastPage == -1
            # print("was on page "+ str(page) +"chaning to")
            # page -= 2
            print(page)

    

    lastPage_array = created_questions[lastPage-1]
    # cleanize array of blanks.
    created_questions = [i for i in created_questions if i != ['','','','','']]

    # if completely empty, refresh array with content
    if created_questions == []:
        created_questions = [['Get started by typing a question here.', '','','',''],['Add your second question here.', '','','','']]

    # methodically check every page for the last page the user was on. then store this page index as the page variable.

    for i in range(len(created_questions)):
        print("checking "+str(i)+" -> "+str(created_questions[i]))
        if created_questions[i] == lastPage_array:
            page = i+1
            lastPage = -1

    if lastPage > len(created_questions):
        page = len(created_questions)
        lastPage = -1
        print("last page was to high so setting to Highest option." + str(page))
        print(created_questions[page-1])

        
    Menu()


def menuGenSavedata():
    #import appropriate StringVars
    global background
    global primary_text
    global secondary_text
    global button_color
    background, primary_text, secondary_text, button_color = created_bg.get(),created_primary.get(),created_secondary.get(),created_color.get()
    window.configure(bg=background) 
    Menu()
#Start Quiz function
def editQuizGen():
    EditQuiz()

def preset_oringal():
    created_bg.set("#222326")
    created_primary.set("#DCDCDC")
    created_secondary.set("#a5a48b")
    created_color.set("#474747")

def preset_light():
    created_bg.set("#D6D6D6")
    created_primary.set("Black")
    created_secondary.set("#727272")
    created_color.set("#8C8C8C")

def preset_dark():
    created_bg.set("#111111")
    created_primary.set("#BDBDBD")
    created_secondary.set("#7B7B7B")
    created_color.set("#232323")

def preset_army():
    created_bg.set("#2A4923")
    created_primary.set("#ACCFA5")
    created_secondary.set("#a5a48b")
    created_color.set("#23381F")

def preset_gold():
    created_bg.set("#FEFFA6")
    created_primary.set("Black")
    created_secondary.set("#4F4F4F")
    created_color.set("Gold")


def reset_all():
    global background
    global primary_text
    global secondary_text
    global button_color
    created_quizname.set("My Quiz")
    created_creator.set("Fellow Quizzer")
    created_bg.set("#222326")
    created_primary.set("#DCDCDC")
    created_secondary.set("#a5a48b")
    created_color.set("#474747")
    global lastPage
    global created_questions
    created_questions = [['Get started by typing a question here.', '','','',''],['Add your second question here.', '','','','']]
    lastPage = -1
    background, primary_text, secondary_text, button_color = created_bg.get(),created_primary.get(),created_secondary.get(),created_color.get()
    window.configure(bg=background)
    Menu()

def preset_random():

    def random_Hex():
        random_number = random.randint(1118481,16777215)
        hex_number = str(hex(random_number))
        hex_number ='#'+ hex_number[2:]

        if not (len(hex_number) < 7):
            return hex_number
        else:
            #I think this is impossiable but its a
            return "red"
        
    created_bg.set(random_Hex())
    created_primary.set(random_Hex())
    created_secondary.set(random_Hex())
    created_color.set(random_Hex())


def saveGen():
    questions = ""
    for i in range(len(created_questions)):
        questions += ','.join(map(str, created_questions[i]))
        questions += '/'
        #this always adds another / char towards the end to it will be removed below since this will not complile properly.
    
    metadata = created_quizname.get() + "," + created_creator.get() + "," + created_bg.get() + "," + created_primary.get() + "," + created_secondary.get() + "," + created_color.get() + "/"
    config_string = metadata + questions
    config_string = config_string[:-1]

    f = open(filedialog.asksaveasfilename(title = "Save as",defaultextension=".txt",filetypes=[("Text files", ".txt")]),'w')
    with f as text_file:
        text_file.write(config_string)


#close
def close_window(): 
    window.destroy()

#Share
url = "https://www.twitter.com"
def shareRes(): 
    webbrowser.open(url,new=1)

#First screen to be ask name.
menuGen()
window.mainloop()
    
    