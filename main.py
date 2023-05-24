from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background="white")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text= c)
    label2.configure(text=c1)
    root.after(1000,label_change)



def translate_now():
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)


#icon

image_icon = PhotoImage(file="g.png")
root.iconphoto(False,image_icon)

#arrow

arrow_image = PhotoImage(file="a.png")
image_label = Label(root,image=arrow_image,width=260)
image_label.place(x=420,y=110)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1=language.keys()


# first combobox


combo1 = ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1 = Label(root,text="ENGLISH",font="Segoe 30 bold",bg="white",width = 15,bd=5,relief=GROOVE)
label1.place(x=18,y=60)


# second combobox


# combo2 = ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")


combo2.place(x=750,y=20)
combo2.set("Select Language")

label2 = Label(root,text="ENGLISH",font="Segoe 30 bold",bg="white",width = 15,bd=5,relief=GROOVE)
label2.place(x=700,y=60)

#first frame
f = Frame(root,bg="Black",bd=5)
f.place(x=19,y=118,width=370,height=210)

text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=350,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



#second frame
f1= Frame(root,bg="Black",bd=5)
f1.place(x=700,y=118,width=370,height=210)

text2=Text(f1,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=350,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#translate button

translate = Button(root,text="Translate",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=10,height=2,bg="black",fg="white",command=translate_now)

translate.place(x=486,y=320)





label_change()


root.mainloop()

