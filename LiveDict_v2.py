from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PyDictionary import PyDictionary
import mtranslate
class LiveDict():
   
    def __init__(self, master=None):
        self.root=Tk()
        self.root.title("Live Dictionary (Yagnesh Vakharia)")
        self.root.config(bg='light blue')
        self.root.resizable(width=False, height=False)
        self.langList={'Afrikaans':'af','Albanian':'sq','Amharic':'am','Arabic':'ar','Armenian':'hy','Azerbaijani':'az','Basque':'eu','Belarusian':'be','Bengali':'bn','Bosnian':'bs','Bulgarian':'bg','Catalan':'ca','Cebuano':'ceb','Chichewa':'ny','Chinese (Simplified)':'zh-CN','Chinese (Taditional)':'zh-TW','Corsican':'co','Croatian':'hr','Czech':'cs','Danish':'da','Dutch':'nl','English':'en','Esperanto':'eo','Estonian':'et','Filipino':'tl','Finnish':'fi','French':'fr','Frisian':'fy','Galician':'gl','Georgian':'ka','German':'de','Greek':'el','Gujarati':'gu','Haitian Creole':'ht','Hausa':'ha','Hawaiian':'haw','Hebrew':'iw','Hindi':'hi','Hmong':'hmn','Hungarian':'hu','Icelandic':'is','Igbo':'ig','Indonesian':'id','Irish':'ga','Italian':'it','Japanese':'ja','Javanese':'jw','Kannada':'kn','Kazakh':'kk','Khmer':'km','Korean':'ko','Kurdish (Kurmanji)':'ku','Kyrgyz':'ky','Lao':'lo','Latin':'la','Latvian':'lv','Lithuanian':'lt','Luxembourgish':'lb','Macedonian':'mk','Malagasy':'mg','Malay':'ms','Malayalam':'ml','Maltese':'mt','Maori':'mi','Marathi':'mr','Mongolian':'mn','Myanmar (Burmese)':'my','Nepali':'ne','Norwegian':'no','Pashto':'ps','Persian':'fa','Polish':'pl','Portuguese':'pt','Punjabi':'pa','Romanian':'ro','Russian':'ru','Samoan':'sm','Scots Gaelic':'gd','Serbian':'sr','Sesotho':'st','Shona':'sn','Sindhi':'sd','Sinhala':'si','Slovak':'sk','Slovenian':'sl','Somali':'so','Spanish':'es','Sundanese':'su','Swahili':'sw','Swedish':'sv','Tajik':'tg','Tamil':'ta','Telugu':'te','Thai':'th','Turkish':'tr','Ukrainian':'uk','Urdu':'ur','Uzbek':'uz','Vietnamese':'vi','Welsh':'cy','Xhosa':'xh','Yiddish':'yi','Yoruba':'yo','Zulu':'zu'}
    
        self.layout()
        
    def layout(self):
        global pyDict
        pyDict=PyDictionary()
        global radioVar
        radioVar=IntVar()
        radioVar.set(1)
        global usrInput
        usrInput=StringVar()
        
        
        #Menu bar for File cascade and About command... 
        self.menuBar=Menu(self.root)
        self.fileMenu=Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label="Save",command=self.save)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit",command=lambda:self.root.destroy())
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        #About command
        self.menuBar.add_command(label="About",command=self.about)
        
        
        #radio buttons
        self.dictRadio=Radiobutton(self.root,text="Dictionary",variable=radioVar,value=1)
        self.antoRadio=Radiobutton(self.root,text="Antonyms",variable=radioVar,value=2)
        self.synoRadio=Radiobutton(self.root,text="Synonyms",variable=radioVar,value=3)
        self.tranRadio=Radiobutton(self.root,text="Translate",variable=radioVar,value=4,command=self.tranSearch)

        #Search box & bar
        self.searchBox=Entry(self.root,width=50,textvariable=usrInput,bg="#f9e0e8")
        self.searchBar=Button(self.root,text="Search",width=20,command=self.search,bg="white")
        self.root.bind('<Return>',self.search)
        
        #results
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.grid(sticky=N+S+W,column=4,row=3,rowspan=3)

        global results
        self.results=Text(self.root,height=7,width=50,wrap=WORD,yscrollcommand=self.scrollbar.set,bg="#f9e0e8")
        
        
        #positions
        self.dictRadio.grid(row=0,column=0,padx=5,pady=5)
        self.antoRadio.grid(row=0,column=1,padx=5,pady=5)
        self.synoRadio.grid(row=0,column=2,padx=5,pady=5)
        self.tranRadio.grid(row=0,column=3,padx=5,pady=5)
        self.searchBox.grid(row=1,columnspan=4,ipady=5,pady=10,sticky=S)
        self.searchBar.grid(row=2,columnspan=4,sticky=N)
        self.results.grid(row=3,columnspan=4,pady=10,padx=5)
        self.scrollbar.config(command=self.results.yview)

        #end
        self.root.config(menu=self.menuBar)
        self.root.mainloop()

    #conditional function calling
    def search(self,*args):
        if radioVar.get()==1:
            self.dictSearch()
        elif radioVar.get()==2:
            self.antoSearch()
        elif radioVar.get()==3:
            self.synoSearch()
        else:
            self.tranSearch()

    #dictionary search function
    def dictSearch(self):
        if pyDict.meaning(usrInput.get())==None:
            self.results.delete(1.0,END)
            self.results.insert(END,"Sorry the word has no such meanings")
        else:
            self.results.delete(1.0,END)
            for i in pyDict.meaning(usrInput.get()):
                self.results.insert(END,i)
                self.results.insert(END,"\n"+pyDict.meaning(usrInput.get())[i][0]+"\n"+"-"*30+"\n")


    #antonym search function                
    def antoSearch(self):
        if pyDict.antonym(usrInput.get())==None:
            self.results.delete(1.0,END)
            self.results.insert(END,"Sorry the word has no such antonyms")
        else:
            self.num=1
            self.results.delete(1.0,END)
            for i in pyDict.antonym(usrInput.get()):
                self.results.insert(END,"\n"+str(self.num)+") "+i+"\n")
                self.num=int(self.num)+1


    #synonym search function
    def synoSearch(self):
        if pyDict.synonym(usrInput.get())==None:
            self.results.delete(1.0,END)
            self.results.insert(END,"Sorry the word has no such synonyms")
        else:
            self.num=1
            self.results.delete(1.0,END)
            for i in pyDict.synonym(usrInput.get()):
                self.results.insert(END,"\n"+str(self.num)+") "+i+"\n")
                self.num=int(self.num)+1

    #tranSearch_Layout
    def tranSearch(self):

        self.root.destroy()
        
        #initializing and configuring frame
        
        self.root2=Tk()
        global tranVar
        global tranVar2
        tranVar=StringVar()
        tranVar2=StringVar()

        self.root2.title("Live Dictionary-Translate (Yagnesh Vakharia)")
        self.root2.config(bg='light blue')
        self.root2.resizable(width=False, height=False)

        self.scrollbar2 = Scrollbar(self.root2)
        self.scrollbar3 = Scrollbar(self.root2)

        #menu cascade for root2
        self.menuBar2=Menu(self.root2)
        self.menuBar2.add_command(label="Save",command=self.tran_save)
        self.root2.config(menu=self.menuBar2)
        
        #Labels and Textbox
        self.usrLang=Label(self.root2, text="Input Language",width=20)
        self.tranLang=Label(self.root2, text="Translated Language",width=20)
        self.usrTextbox=Text(self.root2,width=35,height=15,wrap=WORD,yscrollcommand=self.scrollbar2.set)
        self.tranTextbox=Text(self.root2,width=35,height=15,wrap=WORD,yscrollcommand=self.scrollbar3.set)
        
        self.backButton=Button(self.root2,text="Back",width=10, command=lambda:(self.root2.destroy(),self.__init__()))
        self.exitButton=Button(self.root2,text="Exit",width=10, command=lambda:(self.root2.destroy()))
        
        #Option Menu Layout
        
        self.cb=ttk.Combobox(self.root2,values=sorted(self.langList.keys()),state='readonly',textvariable=tranVar)
        self.cb2=ttk.Combobox(self.root2,values=sorted(self.langList.keys()),state='readonly',textvariable=tranVar2)
        self.cb.bind('<<ComboboxSelected>>',self.call)
        self.cb2.bind('<<ComboboxSelected>>',self.call2)
        
        self.cb.current(21)
        self.cb2.current(0)

        #positions
        self.usrLang.grid(row=0,column=0,padx=5,pady=5)
        self.tranLang.grid(row=0,column=2,padx=5,pady=5)
        self.cb.grid(row=1,column=0,padx=5,pady=5)
        self.cb2.grid(row=1,column=2,padx=5,pady=5)
        self.usrTextbox.grid(row=2,column=0,padx=5,pady=15)
        self.scrollbar2.grid(sticky=N+S,row=2,column=1)
        self.tranTextbox.grid(row=2,column=2,pady=15)
        self.scrollbar3.grid(sticky=N+S,row=2,column=3,padx=5)

        self.scrollbar2.config(command=self.usrTextbox.yview)
        self.scrollbar3.config(command=self.tranTextbox.yview)

        self.backButton.grid(row=3,column=0,columnspan=2,sticky=W,pady=5,padx=5)
        self.exitButton.grid(row=3,column=2,columnspan=2,sticky=E,pady=5,padx=5)

        
        self.root2.mainloop()
        
    def call(self,event):
        self.usrTextbox.delete(1.0,END)
        self.gs=mtranslate
        self.usrTextbox.insert(END,self.gs.translate(self.tranTextbox.get(1.0,END),self.langList[tranVar.get()]))

    def call2(self,event):
        self.tranTextbox.delete(1.0,END)
        self.gs=mtranslate
        self.tranTextbox.insert(END,self.gs.translate(self.usrTextbox.get(1.0,END),self.langList[tranVar2.get()]))

    #save function
    def save(self):
        try:
            if radioVar.get()==1:
                self.f=open("dict_"+usrInput.get()+".txt","w")
                self.f.write(self.results.get(1.0,END))
                self.f.close()
            elif radioVar.get()==2:
                self.f=open("anto_"+usrInput.get()+".txt","w")
                self.f.write(self.results.get(1.0,END))
                self.f.close()
            elif radioVar.get()==3:
                self.f=open("syno_"+usrInput.get()+".txt","w")
                self.f.write(self.results.get(1.0,END))
                self.f.close()

        except Exception:
            self.messagebox.showerror("Error","Something went wrong. Please try again!")

    def tran_save(self):
        self.num=1
        self.x=True
        while self.x:
            try:
                self.f2=open("translate_"+str(self.num)+".txt","r")
                
            except Exception:
                self.f2=open("translate_"+str(self.num)+".txt","w",encoding="utf-8")
                self.f2.write("Input:\n"+self.usrTextbox.get(1.0,END)+"\n\nTranslated:\n"+self.tranTextbox.get(1.0,END))
                self.f2.close()
                self.x=False
            finally:
                self.num=self.num+1
            
    #about function
    def about(self):
        messagebox.showinfo("About","This program is created by Yagnesh Vakharia.\nContact: yagneshvakharia97@gmail.com")




if __name__ == '__main__':
    LiveDict()
