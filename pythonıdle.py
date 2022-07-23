from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename            
from tkinter.scrolledtext import ScrolledText                               
import subprocess                                                            
#pencere yaratmaq
window = Tk()
#Basliq
window.title("Python IDLE")
#Menu yaratmaq
menu = Menu(window)
window.config(menu=menu)
#Kod yazmaq ucun redaktor penceresi
editor = ScrolledText(window, font=("haveltica 10 bold"))                        #srift,olcu,qalinliq
editor.pack(fill=BOTH, expand=1)                                                 #both-ufuqi,saquli doldurmaq
editor.focus()                                                                   #proqram dayanana qeder aktiv saxliyir
file_path = ""
#Open 
def open_file(event=None):
    global code, file_path
    open_path = askopenfilename(filetypes=[("Python File", "*.py")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)            #silmek
        editor.insert(1.0, code)           #elave etmek
window.bind("<Control-o>", open_file)
#Save
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)           #istifadeci terefinder deyer daxil edilir
        file.write(code) 
window.bind("<Control-s>", save_file)
#Save as
def save_as(event=None):
    global code, file_path
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
window.bind("<Control-S>", save_as)
#Run
def run(event=None):
    global code, file_path
    cmd = f"python {file_path}"        
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)   #popen-yeni prosese baslamaq,1-proqram,2-fayl arqumenti
    output, error =  process.communicate()
    #evvelki metni sil
    output_window.delete(1.0, END)
    #yeni cixis metni daxil etmek
    output_window.insert(1.0, output)
    #xeta metnini daxil etmek
    output_window.insert(1.0, error)
window.bind("<F5>", run)
#IDLE baglamaq
def close(event=None):
    window.destroy()    #yaddasi bosaltmaq ekrani temizlemek
window.bind("<Control-q>", close)
#cut
def cut_text(event=None):
        editor.event_generate(("<<Cut>>"))
#copy
def copy_text(event=None):
        editor.event_generate(("<<Copy>>"))
#paste
def paste_text(event=None):
        editor.event_generate(("<<Paste>>"))
     
#Menu yaratmaq
file_menu = Menu(menu, tearoff=0)   #tearoff=1 menyu qoparmaq
edit_menu = Menu(menu, tearoff=0)
run_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
#label elave et esas menyu ile elaqelendirir
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Run", menu=run_menu)
menu.add_cascade(label ="Theme", menu=theme_menu)
#file menuya emrler elave edir
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()                            
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=close)
#edit menu
edit_menu.add_command(label="Cut", command=cut_text) 
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
#run
run_menu.add_command(label="Run", accelerator="F5", command=run)
#theme
def light():
    editor.config(bg="white")
    output_window.config(bg="white")

def dark():
    editor.config(fg="#1dd604", bg="black")
    output_window.config(fg="#1dd604", bg="black")
#theme menu
theme_menu.add_command(label="light", command=light)
theme_menu.add_command(label="dark", command=dark)
#output
output_window = ScrolledText(window, height=10)
output_window.pack(fill=BOTH, expand=1)
window.mainloop()