# importing required module
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from gtts import gTTS
 
# this module helps to
# play the converted audio 
import os

def quitter_function():
    answer = askquestion(title='Quit?', message='Do you really want to quit?')
    if answer=='yes':
        root.destroy()

def openfile():
    filename=askopenfilename(initialdir='Documents',
                             filetypes=[('Text files', '.text'),
                                        ('All files', '*')])
    s = open(filename).read()
    textbox.insert(1.0, s)

# create tkinter window
root = Tk()
 
# styling the frame which helps to 
# make our background stylish
frame1 = Frame(root,
               bg = "black",
               height = "150")
 
# place the widget in gui window
frame1.pack(fill = X)
 
 
frame2 = Frame(root,
               bg = "black",
               height = "450")
frame2.pack(fill=X)
 
 
 
# styling the label which show the text 
# in our tkinter window
label = Label(frame1, text = "Text to Speech 📄👉📢",
              font = ('Courier New', 20, 'bold'),
              bg = "brown")
 
label.place(x = 180, y = 110)
 
 
 
# entry is used to enter the text 
textbox = ScrolledText(frame2, height=6, width = 45,
              bd = 8, font =('Courier New', 14))
 
textbox.place(x = 80, y = 52)
textbox.insert(END, "")


 
# define a function which can
# get text and convert into audio
def play():
 
    # Language in which you want to convert 
    language = "en"
 
 
 
   # Passing the text  and language, 
   # here we have  slow=False. Which tells 
   # the module that the converted audio should 
   # have a high speed 
 
    myobj = gTTS(text = textbox.get(1.0,END),
                lang = language,
                slow = False)
 
 
 
    # give the name as you want to 
    # save the audio
    myobj.save("convert.wav")
    os.system("convert.wav")
 
# create a button which holds
# our play function using command = play
btn = Button(frame2, text = "Convert 🔊",
             width = "15", pady = 10,
             font =('Courier New', 15),
             command = play, bg='brown')

btn1 = Button(frame2, text = "Quit ⏱",
             width = "15", pady = 10,
             font =('Courier New', 15),
             command = quitter_function, bg='brown')

btn2 = Button(frame2, text = "Open file 📄",
             width = "15", pady = 10,
             font =('Courier New', 15),
             command = openfile, bg='brown')
 
btn.place(x = 150,
          y = 230)

btn1.place(x = 250,
          y = 300)

btn2.place(x = 350,
          y = 230)
 
# give a title 
root.title("text to speech converter")
 
 
 
# we can not change the size
# if you want you can change
root.geometry("650x550+350+200")

# start the gui
root.mainloop()
