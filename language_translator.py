import tkinter as tk
import googletrans
from PIL import ImageTk, Image      
from googletrans import Translator  
from tkinter import messagebox,ttk
import os
from gtts import gTTS
root = tk.Tk()
root.title('Langauge Translator')
C = tk.Canvas(root,height=10,width=10)
filename = ImageTk.PhotoImage(Image.open('new.jpg'))
background_label = tk.Label(root,image=filename )
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack(side="bottom",)
root.iconbitmap("favicon.ico")
photo=ImageTk.PhotoImage(Image.open("play.jpg"))
photo1=ImageTk.PhotoImage(Image.open("speaker.jpg"))
tk.Label(root,text="TRANSLATOR",font=("Forte", 25),foreground='blue').place(x=570,y=30)
a = tk.StringVar() 
auto_detect = ttk.Combobox(root, width = 20, textvariable = a, state='readonly',font=('verdana',12,'bold')) 
auto_detect['values'] = (
                          'Auto Detect', 
                          ) 
  
auto_detect.place(x=50,y=70)
auto_detect.current(0) 
l = tk.StringVar() 
choose_langauge = ttk.Combobox(root, width = 20, textvariable = l,font=('verdana',12,'bold')) 
choose_langauge['values'] = ('Afrikaans',
                        'Albanian',
                        'Arabic',
                        'Armenian',
                        'Basque',
                        'Belarusian',
                        'Bengali',
                        'Bosnian',
                        'Bulgarian',
                       'Catalan',
                        'Cebuano',
                        'Chichewa',
                        'Chinese (simplified)',
                        'Chinese (traditional)',
                             
                        'Corsican',
                        'Croatian',
                       ' Czech',
                        'Danish',
                        'Dutch',
                        'English',
                        'Esperanto',
                        'Estonian',
                        'Filipino',
                        'Finnish',
                        'French',
                        'Frisian',
                        'Galician',
                        'Georgian',
                        'German',
                        'Greek',
                        'Gujarati',
                        'Haitian Creole',
                        'Hausa',
                        'Hawaiian',
                        'Hebrew',
                        'Hindi',
                        'Hmong',
                        'Hungarian',
                        'Icelandic',
                        'Igbo',
                        'Indonesian',
                        'Irish',
                        'Italian',
                        'Japanese',
                        'Javanese',
                        'Kannada',
                        'Kazakh',
                        'Khmer',
                        'Kinyarwanda',
                        'Korean',
                        'Kurdish (kurmanji)',
                        'Kyrgyz',
                        'Lao',
                        'Latin',
                        'Latvian',
                        'Lithuanian',
                        'Luxembourgish',
                        'Macedonian',
                        'Malagasy',
                        'Malay',
                        'Malayalam',
                        'Maltese',
                        'Maori',
                        'Marathi',
                        'Mongolian',
                        'Myanmar (burmese)',
                        'Nepali',
                        'Norwegian'
                        'Odia',
                        'Pashto',
                        'Persian',
                        'Polish',
                        'Portuguese',
                        'Punjabi',
                        'Romanian',
                        'Russian',
                        'Samoan',
                        'Scots Gaelic',
                        'Serbian',
                        'Sesotho',
                        'Shona',
                        'Sindhi',
                        'Sinhala',
                        'Slovak',
                        'Slovenian',
                        'Somali',
                        'Spanish',
                        'Sundanese',
                        'Swahili',
                        'Swedish',
                        'Tajik',
                        'Tamil',
                        'Tatar',
                        'Telugu',
                        'Thai',
                        'Turkish',
                        'Turkmen',
                        'Ukrainian',
                        'Urdu',
                        'Uyghur',
                        'Uzbek',
                        'Vietnamese',
                        'Welsh',
                        'Xhosa'
                        'Yiddish',
                        'Yoruba',
                        'Zulu',
                          ) 
  
choose_langauge.place(x=930,y=70)
choose_langauge.current(0) 
def convert():
    play = tk.Button(root,image=photo,command=sound,relief="ridge",borderwidth=3,font=('verdana',15,'bold'),cursor="hand2")
    play.place(x=1750,y=170)
    
    language_1 = t1.get("1.0","end-1c")
    cl = choose_langauge.get()
    if language_1 == '':
        messagebox.showerror('Language Translator','please fill the box')
    else:
        d=googletrans.LANGUAGES
        t2.configure(state='normal')
        t2.delete(1.0,'end')
        translator = Translator()
        a=translator.detect(language_1)
        try:
            for i in d.keys():
                if cl.lower()==d[i]:
                    t2.configure(state="normal")
                    output = translator.translate(language_1, dest=str(i))
                    t2.insert('end',output.text)
                    t2.configure(state="disabled")
                    speak = gTTS(text=output.text, lang=str(i), slow= False)
                    speak.save("captured_voice.mp3")
                if i==str(a.lang):
                    auto_detect['values'] = (d[i].capitalize(),)
                    auto_detect.place(x=50,y=70)
                    auto_detect.current(0)
        except:
            play1 = tk.Button(root,image=photo1,relief="ridge",borderwidth=3,font=('verdana',15,'bold'),cursor="hand2")
            play1.place(x=1750,y=170)
def sound():
    os.system("start captured_voice.mp3")
def clear():
        t2.configure(state='normal')
        t1.delete(1.0,'end')
        t2.delete(1.0,'end')
        scrollbar =tk.Scrollbar(root)
def multiple(*args):
    t1.yview(*args)
    t2.yview(*args)
t1 = tk.Text(root,width=60,height=27,borderwidth=5,relief="ridge",font=('arial',14))
t1.place(x=30,y=130)
scrollbar=tk.Scrollbar(root)
scrollbar.pack(side="right",fill="y",ipadx=5)
scrollbar.config(command=multiple)
t2 = tk.Text(root,width=60,height=27,borderwidth=5,relief="ridge",font=('arial',14))
t2.place(x=900,y=130)
t2.configure(state="disabled")
button = tk.Button(root,text="Translate",command=convert,background="pink",relief="ridge",borderwidth=3,font=('verdana',15,'bold'),cursor="hand2")
button.place(x=700,y=870)
clear = tk.Button(root,text="Clear",command=clear,background="pink",relief="ridge",borderwidth=3,font=('verdana',15,'bold'),cursor="hand2")
clear.place(x=930,y=870)
play = tk.Button(root,image=photo,command=sound,relief="ridge",borderwidth=3,font=('verdana',15,'bold'),cursor="hand2")
play.place(x=1750,y=170)
root.mainloop()
 

 


 



 

 