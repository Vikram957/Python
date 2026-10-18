from tkinter import*
from PIL import Image , ImageTk
import speech_to_text
import action
root = Tk()
root.title("Voice Assistant")
root.geometry("575x675")   #width
root.resizable(False,False)   #it restrict resizable window
root.config(bg = "#171923")

# ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END , "User--->"+user_val+"\n")
    if bot_val != None:
        text.insert(END, "Bot<---"+str(bot_val)+"\n")
    if bot_val == "Ok Sir":
        root.destroy()



def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "User--->"+send+"\n")
    if bot != None:
        text.insert(END, "Bot<---"+str(bot)+"\n")
    if bot == "Ok Sir":
        root.destroy()


def del_txt():
    text.delete("1.0" , "end")
# FRAME

frame = LabelFrame(root , padx = 12, pady = 7,borderwidth=3,relief="raised")
frame.config(bg = "#292D3E")
frame.grid(row = 0,column=1,padx = 122,pady=7)


# text Label
text_label = Label(frame , text="Voice Assistant", font=("comic Sans ms",14, "bold"),bg ="#356696")
text_label.grid(row=0,column=0, padx=20,pady=10)


# image
image = Image.open("python_projects/voice_assistant_project/voice_assistant_logo.jpeg")
image = image.resize((280,280))
image = ImageTk.PhotoImage(image)

image_label = Label(frame , image = image)
image_label.grid(row=1,column=0,pady=20)


# adding some text widgets

text = Text(root , font= ("courier 10 bold"),bg = "#356696")
text.grid(row = 2,column = 0)
text.place(x = 100, y = 410,width=360,height=100)


# ENTRY WIDGET
entry = Entry(root, justify=CENTER)
entry.place(x=130,y=520,width=299,height=36)


# Butoon 1
button1 = Button(root,text = "ASK",bg = "#A78BFA",pady=14,padx=30,borderwidth=3,relief="solid",command=ask)
button1.place(x = 90, y = 580)

# Butoon 2
button2 = Button(root,text = "Send",bg = "#A78BFA",pady=14,padx=30,borderwidth=3,relief="solid",command=send)
button2.place(x = 390, y = 580)


# Butoon 3
button3 = Button(root,text = "Delete",bg = "#A78BFA",pady=14,padx=30,borderwidth=3,relief="solid",command=del_txt)
button3.place(x = 232, y = 580)


root.mainloop()
