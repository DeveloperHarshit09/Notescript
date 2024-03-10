from tkinter import *
import tkinter as tk
from tkinter import messagebox, font
from tkinter.messagebox import _show
import os
from tkinter.filedialog import asksaveasfilename, askopenfilename
import win32api
import pyautogui
import json


def newFile(event=None):
    if len(TextArea.get("1.0", "end-1c")) != 0 and str(TextArea.get(1.0, END)).isspace() == False:
        MsgBox = tk.messagebox.askquestion('Notescript Version 1.2',
                                           'It will clear all your data save your work before making new '
                                           'file', icon='warning')
        if MsgBox == 'yes':
            global file
            root.title("Untitled-Notescript")
            file = None
            TextArea.delete(1.0, END)
    else:
        root.title("Untitled-Notescript")
        file = None
        TextArea.delete(1.0, END)


def openFile(event=None):
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notescript")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile(event=None):
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notescript")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitapp(event=None):
    MsgBox = tk.messagebox.askquestion('Notescript Version 1.2', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        try:
            os.remove('Temporary.txt')
        except:
            pass
        root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    _show("Notescript version 1.2", "This software is created by Technology Supporter on 6th March 2020")


def contact():
    _show("Notescript version 1.2", "For Regarding queries contact us by E-MAIL easyalgorithmsuccess@gmail.com")


def soft(event=None):
    _show("Notescript version 1.2",
          "This Software is update by Technology Supporter on 29th Feburary 2024 with some changes")


def locprinter(event=NONE):
    if len(TextArea.get("1.0", "end-1c")) == 0 or str(TextArea.get(1.0, END)).isspace():
        messagebox.showerror('Empty File', 'Empty file cannot be Print')
    else:
        MsgBox = tk.messagebox.askquestion('Notescript Version 1.2', 'Are you sure you want to print this document',
                                           icon='info')
        if MsgBox == 'yes':
            temp = open('Temporary.txt', "w")
            temp.write(TextArea.get(1.0, END))
            temp.flush()
            temp.close()
            win32api.ShellExecute(0, "print", 'Temporary.txt', None, ".", 0)


# To capture cancel event
def on_closing():
    if len(TextArea.get("1.0", "end-1c")) == 0 or str(TextArea.get(1.0, END)).isspace():
        root.destroy()
    else:
        MsgBox = tk.messagebox.askquestion('Notescript Version 1.2', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            try:
                os.remove('Temporary.txt')
            except:
                pass
            root.destroy()


def calibri():
    dictionary = {
        "Fonts": "Calibri",

    }

    with open("Fonts.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=["Calibri", Fontsize['Fontsize']])


def times():
    dictionary = {
        "Fonts": "Times New Roman",

    }

    with open("Fonts.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=["Times New Roman", Fontsize['Fontsize']])


def kruti():
    dictionary = {
        "Fonts": "Kruti dev 010",

    }

    with open("Fonts.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=["Kruti dev 010", Fontsize['Fontsize']])


def arial():
    dictionary = {
        "Fonts": "Arial",

    }

    with open("Fonts.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=["Arial", Fontsize['Fontsize']])


def gs():
    dictionary = {
        "Fonts": "Goudy Stout",

    }

    with open("Fonts.json", "w") as outfile:
        json.dump(dictionary, outfile)

    TextArea.configure(font=["Goudy Stout", Fontsize['Fontsize']])


# For Undo Redo
def undoo():
    pyautogui.hotkey('ctrl', 'z')


def redoo():
    pyautogui.hotkey('ctrl', 'y')


# For themes
def light():
    dictionary = {
        "bg": "White",
        "fg": "Black",
        "cursor": "Black",

    }

    with open("Themes.json", "w") as outfile:
        json.dump(dictionary, outfile)

    root.config(bg="White")
    TextArea.config(bg='White', fg="Black", insertbackground="Black")
    FileMenu.config(bg='White', fg='Black')
    EditMenu.config(bg='White', fg='Black')
    Format.config(bg='White', fg='Black')
    sub_menu.config(bg='White', fg='Black')
    submenu2.config(bg='White', fg='Black')
    submenu3.config(bg='White', fg='Black')
    Appearance.config(bg='White', fg='Black')
    HelpMenu.config(bg='White', fg='Black')


def dark():
    dictionary = {
        "bg": "Black",
        "fg": "White",
        "cursor": "White",

    }

    with open("Themes.json", "w") as outfile:
        json.dump(dictionary, outfile)

    root.config(bg="Black")
    TextArea.config(bg='Black', fg="White", insertbackground="White")
    FileMenu.config(bg="Black", fg="White")
    EditMenu.config(bg="Black", fg="White")
    Format.config(bg="Black", fg="White")
    sub_menu.config(bg="Black", fg="White")
    submenu2.config(bg="Black", fg="White")
    submenu3.config(bg='Black', fg='White')
    Appearance.config(bg="Black", fg="White")
    HelpMenu.config(bg="Black", fg="White")


def blue():
    dictionary = {
        "bg": "#193549",
        "fg": "White",
        "cursor": "White",

    }

    with open("Themes.json", "w") as outfile:
        json.dump(dictionary, outfile)
    root.config(bg="#193549")
    TextArea.config(bg='#193549', fg="White", insertbackground="White")

    FileMenu.config(bg="#193549", fg="White")
    EditMenu.config(bg="#193549", fg="White")
    Format.config(bg="#193549", fg="White")
    sub_menu.config(bg="#193549", fg="White")
    submenu2.config(bg="#193549", fg="White")
    submenu3.config(bg='#193549', fg='White')
    Appearance.config(bg="#193549", fg="White")
    HelpMenu.config(bg="#193549", fg="White")


def yellow():
    dictionary = {
        "bg": "Yellow",
        "fg": "Red",
        "cursor": "Red",

    }

    with open("Themes.json", "w") as outfile:
        json.dump(dictionary, outfile)
    root.config(bg="Yellow")
    TextArea.config(bg='Yellow', fg="Red", insertbackground="Red")
    FileMenu.config(bg='Yellow', fg='Red')
    EditMenu.config(bg='Yellow', fg='Red')
    Format.config(bg='Yellow', fg='Red')
    sub_menu.config(bg='Yellow', fg='Red')
    submenu2.config(bg='Yellow', fg='Red')
    submenu3.config(bg='Yellow', fg='Red')
    Appearance.config(bg='Yellow', fg='Red')
    HelpMenu.config(bg='Yellow', fg='Red')


def purple():
    dictionary = {
        "bg": "Purple",
        "fg": "White",
        "cursor": "White",

    }

    with open("Themes.json", "w") as outfile:
        json.dump(dictionary, outfile)
    root.config(bg="Purple")
    TextArea.config(bg='Purple', fg="White", insertbackground="White")
    FileMenu.config(bg='Purple', fg='White')
    EditMenu.config(bg='Purple', fg='White')
    Format.config(bg='Purple', fg='White')
    sub_menu.config(bg='Purple', fg='White')
    submenu2.config(bg='Purple', fg='White')
    submenu3.config(bg='Purple', fg='White')
    Appearance.config(bg='Purple', fg='White')
    HelpMenu.config(bg='Purple', fg='White')


def green():
    dictionary = {
        "bg": "Light Green",
        "fg": "Dark Green",
        "cursor": "White",

    }

    with open("Themes.json", "w") as outfile:
        json.dump(dictionary, outfile)
    root.config(bg="Light Green")
    TextArea.config(bg='Light Green', fg="Dark Green", insertbackground="White")
    FileMenu.config(bg='Light Green', fg='Dark Green')
    EditMenu.config(bg='Light Green', fg='Dark Green')
    Format.config(bg='Light Green', fg='Dark Green')
    sub_menu.config(bg='Light Green', fg='Dark Green')
    submenu2.config(bg='Light Green', fg='Dark Green')
    submenu3.config(bg='Light Green', fg='Dark Green')
    Appearance.config(bg='Light Green', fg='Dark Green')
    HelpMenu.config(bg='Light Green', fg='Dark Green')


def dark_yellow():
    dictionary = {
        "bg": "Black",
        "fg": "Yellow",
        "cursor": "Yellow",

    }

    with open("Themes.json", "w") as outfile:
        json.dump(dictionary, outfile)

    root.config(bg="Black")
    TextArea.config(bg='Black', fg="Yellow", insertbackground="Yellow")
    FileMenu.config(bg='Black', fg='Yellow')
    EditMenu.config(bg='Black', fg='Yellow')
    Format.config(bg='Black', fg='Yellow')
    sub_menu.config(bg='Black', fg='Yellow')
    submenu2.config(bg='Black', fg='Yellow')
    submenu3.config(bg='Black', fg='Yellow')
    Appearance.config(bg='Black', fg='Yellow')
    HelpMenu.config(bg='Black', fg='Yellow')


# For Format Menu

def bold(event=None):
    boldfont = font.Font(TextArea, TextArea.cget("font"))
    boldfont.configure(weight="bold")
    TextArea.tag_configure("bold", font=boldfont)
    try:
        current_tags = TextArea.tag_names("sel.first")
        if "bold" in current_tags:
            TextArea.tag_remove("bold", "sel.first", "sel.last")
        elif "underline" in current_tags:
            TextArea.tag_remove("underline", "sel.first", "sel.last")
            TextArea.tag_add("bold", "sel.first", "sel.last")
        elif "italic" in current_tags:
            TextArea.tag_remove("italic", "sel.first", "sel.last")
            TextArea.tag_add("bold", "sel.first", "sel.last")
        else:
            TextArea.tag_add("bold", "sel.first", "sel.last")
    except:
        pass


def italicss(event=None):
    italicfont = font.Font(TextArea, TextArea.cget("font"))
    italicfont.configure(slant="italic")
    TextArea.tag_configure("italic", font=italicfont)
    try:
        current_tags = TextArea.tag_names("sel.first")
        if "italic" in current_tags:
            TextArea.tag_remove("italic", "sel.first", "sel.last")
        elif "bold" in current_tags:
            TextArea.tag_remove("bold", "sel.first", "sel.last")
            TextArea.tag_add("italic", "sel.first", "sel.last")

        elif "underline" in current_tags:
            TextArea.tag_remove("underline", "sel.first", "sel.last")
            TextArea.tag_add("italic", "sel.first", "sel.last")
        else:
            TextArea.tag_add("italic", "sel.first", "sel.last")
    except:
        pass


def under(event=None):
    f = font.Font(TextArea, TextArea.cget("font"))
    f.configure(underline=True)
    TextArea.tag_configure("underline", font=f)
    try:
        current_tags = TextArea.tag_names("sel.first")
        if "underline" in current_tags:
            TextArea.tag_remove("underline", "sel.first", "sel.last")
        elif "bold" in current_tags:
            TextArea.tag_remove("bold", "sel.first", "sel.last")
            TextArea.tag_add("underline", "sel.first", "sel.last")
        elif "italic" in current_tags:
            TextArea.tag_remove("italic", "sel.first", "sel.last")
            TextArea.tag_add("underline", "sel.first", "sel.last")
        else:
            TextArea.tag_add("underline", "sel.first", "sel.last")
    except:
        pass


# For Font Size

def ten():
    dictionary = {
        "Fontsize": "10",

    }

    with open("Fontsize.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=[Fonts['Fonts'], '10'])


def twen():
    dictionary = {
        "Fontsize": "18",

    }

    with open("Fontsize.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=[Fonts['Fonts'], '18'])


def four():
    dictionary = {
        "Fontsize": "24",

    }

    with open("Fontsize.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=[Fonts['Fonts'], '24'])


def six():
    dictionary = {
        "Fontsize": "36",

    }

    with open("Fontsize.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=[Fonts['Fonts'], '36'])


def eight():
    dictionary = {
        "Fontsize": "48",

    }

    with open("Fontsize.json", "w") as outfile:
        json.dump(dictionary, outfile)
    TextArea.configure(font=[Fonts['Fonts'], '48'])


# To Capture User Theme From Themes.json
try:
    with open('Themes.json', 'r') as c:
        userdata = json.load(c)
except:

    dictionary = {
        "bg": "White",
        "fg": "Black",
        "cursor": "Black",

    }

    with open("Themes.json", "w") as outfile:
        json.dump(dictionary, outfile)

    with open('Themes.json', 'r') as c:
        userdata = json.load(c)

# To Capture From Fonts.json
try:
    with open('Fonts.json', 'r') as ce:
        Fonts = json.load(ce)
except:

    dictionary = {
        "Fonts": "Calibri",

    }

    with open("Fonts.json", "w") as outfile:
        json.dump(dictionary, outfile)

    with open('Fonts.json', 'r') as ce:
        Fonts = json.load(ce)

# To Capture From Fontsize.json
try:
    with open('Fontsize.json', 'r') as cee:
        Fontsize = json.load(cee)

except:
    dictionary = {
        "Fontsize": "24",

    }

    with open("Fontsize.json", "w") as outfile:
        json.dump(dictionary, outfile)

    with open('Fontsize.json', 'r') as cee:
        Fontsize = json.load(cee)


def find_text():
    search_text = entry.get()
    TextArea.tag_remove('found', '1.0', tk.END)
    if search_text:
        start_pos = '1.0'
        while True:
            start_pos = TextArea.search(search_text, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f'{start_pos}+{len(search_text)}c'
            TextArea.tag_add('found', start_pos, end_pos)
            start_pos = end_pos
        TextArea.tag_config('found', background='yellow')


def unhighlight():
    TextArea.tag_remove('found', '1.0', tk.END)
    new.destroy()


def find(event=None):
    global new
    new = tk.Tk()
    new.title("Find")
    new.wm_iconbitmap("logo.ico")
    new.geometry("300x300")
    new.resizable(False, False)
    name_label = tk.Label(new, text='Find', font=('calibre', 10, 'bold'))
    name_label.pack()
    global entry
    entry = tk.Entry(new)
    entry.pack(pady=20)
    sub_btn = tk.Button(new, text='Find', command=find_text)
    sub_btn.pack()

    new.protocol("WM_DELETE_WINDOW", unhighlight)

    new.mainloop()


def replace_text():
    search_text = entry2.get()
    replace_text = entryreplace.get()
    if replace_text == '' or search_text == '':
        pass

    else:
        content = TextArea.get('1.0', tk.END)
        updated_content = content.replace(search_text, replace_text)
        TextArea.delete('1.0', tk.END)
        TextArea.insert('1.0', updated_content)

        if replace_text:
            start_pos = '1.0'
            while True:
                start_pos = TextArea.search(replace_text, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(replace_text)}c'
                TextArea.tag_add('replaced', start_pos, end_pos)
                start_pos = end_pos
            TextArea.tag_config('replaced', background='red')


def after_replacement():
    TextArea.tag_remove('found', '1.0', tk.END)
    TextArea.tag_remove('replaced', '1.0', tk.END)
    rep.destroy()


def replace(event=None):
    global rep
    rep = tk.Tk()
    rep.title("Replace")
    rep.wm_iconbitmap("logo.ico")
    rep.geometry("300x300")
    rep.resizable(False, False)
    name_labell = tk.Label(rep, text='Replace to', font=('calibre', 10, 'bold'))
    name_labell.pack()
    global entry2
    entry2 = tk.Entry(rep)
    entry2.pack(pady=20)

    name_labell2 = tk.Label(rep, text='Repalce With', font=('calibre', 10, 'bold'))
    name_labell2.pack()

    global entryreplace
    entryreplace = tk.Entry(rep)
    entryreplace.pack(pady=20)

    btn1 = tk.Button(rep, text='Replace', command=replace_text)
    btn1.pack()

    # To Capture Close Window
    rep.protocol("WM_DELETE_WINDOW", after_replacement)
    rep.mainloop()

# Add Right Click Menu Functionality
def show_menu(event):
    RightMenu.post(event.x_root, event.y_root)

# To Protect Common Settings given in Software
l1 = ['10', '18', '24', '36']
l2 = ['Calibri', 'Times New Roman', 'Kruti dev 010', 'Goudy Stout', 'Arial']
BG = ['White', 'Black', 'Purple', 'Light Green', '#193549', 'Yellow']
FG = ['Black', 'White', 'Dark Green', 'Red', 'Yellow']
Mouse = ['White', 'Black', 'Red', 'Dark Green', 'Yellow']

if __name__ == '__main__' and userdata['bg'] in BG and userdata['fg'] in FG and userdata['cursor'] in Mouse and \
        Fonts['Fonts'] in l2 and Fontsize['Fontsize'] in l1:
    # BASIC TKINTER SETUP
    root = Tk()
    root.title("Untitled - Notescript")
    root.wm_iconbitmap("new.ico")
    root.geometry("600x530")

    # Add TextArea

    TextArea = Text(root, undo=True, bg=userdata['bg'], fg=userdata['fg'], insertbackground=userdata['cursor'])

    TextArea.configure(font=[Fonts['Fonts'], Fontsize['Fontsize']])
    TextArea.pack(expand=True, fill=BOTH)
    file = None

    # CREATE A MENUBAR
    MenuBar = Menu(root)

    # FileMenu starts
    FileMenu = Menu(MenuBar, tearoff=0)

    # open new file
    FileMenu.add_command(label="New" + "              " + "Ctrl+N", command=newFile)
    # open already existing file
    FileMenu.add_command(label="Open" + "            " + "Ctrl+O", command=openFile)
    # save file
    FileMenu.add_command(label="Save" + "              " + "Ctrl+S", command=saveFile)
    FileMenu.add_separator()


    # print
    FileMenu.add_command(label="Print" + "              " + "Ctrl+P", command=locprinter)

    # Exit
    FileMenu.add_command(label="Exit" + "                " + "Alt+F4", command=quitapp)

    MenuBar.add_cascade(label="File", menu=FileMenu)

    # FileMenu ends

    # Edit menu
    EditMenu = Menu(MenuBar, tearoff=0)

    # cut,copy,paste
    EditMenu.add_command(label="Cut" + "              " + "Ctrl+X", command=cut)
    EditMenu.add_command(label="Copy" + "           " + "Ctrl+C", command=copy)
    EditMenu.add_separator()

    EditMenu.add_command(label="Paste" + "           " + "Ctrl+V", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # EditMenu ends

    # Format Menu Starts
    Format = Menu(MenuBar, tearoff=0)
    Format.add_command(label="Bold" + "                   " + "Ctrl+B", command=bold)
    Format.add_command(label="Italic" + "                   " + "Ctrl+L", command=italicss)
    Format.add_command(label="Underline" + "          " + "Ctrl+U", command=under)
    Format.add_separator()
    Format.add_command(label="Find" + "                    " + "Ctrl+F", command=find)
    Format.add_command(label="Replace" + "              " + "Ctrl+R", command=replace)

    MenuBar.add_cascade(label="Format", menu=Format)
    # Format menu ends

    # Appearance menu
    Appearance = Menu(MenuBar, tearoff=0)

    # Font submenu
    sub_menu = Menu(Appearance, tearoff=0)
    sub_menu.add_command(label='Calibri', command=calibri)
    sub_menu.add_command(label='Times New Roman', command=times)
    sub_menu.add_command(label='Kruti Dev 010', command=kruti)
    sub_menu.add_command(label='Arial', command=arial)
    sub_menu.add_command(label='Goudy Stout', command=gs)

    Appearance.add_cascade(label="Fonts", menu=sub_menu)

    # Font Submenu ends

    # Fontsize submenu
    submenu3 = Menu(Appearance, tearoff=0)
    submenu3.add_command(label='10', command=ten)
    submenu3.add_command(label='18', command=twen)
    submenu3.add_command(label='24', command=four)
    submenu3.add_command(label='36', command=six)
    submenu3.add_command(label='48', command=eight)

    Appearance.add_cascade(label="Font-Size", menu=submenu3)

    # Font-Size Submenu ends

    # Theme submenu
    submenu2 = Menu(Appearance, tearoff=0)
    submenu2.add_command(label='Light', command=light)
    submenu2.add_command(label='Dark', command=dark)
    submenu2.add_command(label='Dark-Yellow', command=dark_yellow)
    submenu2.add_command(label='Blue', command=blue)
    submenu2.add_command(label='Yellow', command=yellow)
    submenu2.add_command(label='Purple', command=purple)
    submenu2.add_command(label='Light Green', command=green)

    Appearance.add_cascade(label="Themes", menu=submenu2)

    # Theme Submenu ends

    Appearance.add_separator()
    # Add Undo Redo
    Appearance.add_command(label="Undo" + "           " + "Ctrl+Z", command=undoo)
    Appearance.add_command(label="Redo" + "            " + "Ctrl+Y", command=redoo)

    MenuBar.add_cascade(label="Appearance", menu=Appearance)

    # Appearance menu ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notescript", command=about)
    HelpMenu.add_command(label="Contact us", command=contact)

    HelpMenu.add_separator()
    HelpMenu.add_command(label="Update History", command=soft)
    # HelpMenu.add_command(label="BC",command=bc)

    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # Help Menu Ends

    # Right Click menu
    RightMenu = Menu(MenuBar, tearoff=0)

    # cut,copy,paste
    RightMenu.add_command(label="Cut       ", command=cut)
    RightMenu.add_command(label="Copy       ", command=copy)
    RightMenu.add_command(label="Paste       ", command=paste)
    RightMenu.add_separator()
    RightMenu.add_command(label="Bold       ", command=bold)
    RightMenu.add_command(label="Italic       ", command=italicss)
    RightMenu.add_command(label="Underline       ", command=under)


    # Right Click Menu ends

    root.config(menu=MenuBar)

    # Adding Scrollbar at y-axis
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    # Menubar Theme
    FileMenu.config(bg=userdata['bg'], fg=userdata['fg'])
    EditMenu.config(bg=userdata['bg'], fg=userdata['fg'])
    Format.config(bg=userdata['bg'], fg=userdata['fg'])
    sub_menu.config(bg=userdata['bg'], fg=userdata['fg'])
    submenu2.config(bg=userdata['bg'], fg=userdata['fg'])
    submenu3.config(bg=userdata['bg'], fg=userdata['fg'])
    Appearance.config(bg=userdata['bg'], fg=userdata['fg'])
    HelpMenu.config(bg=userdata['bg'], fg=userdata['fg'])

    # Shortcuts
    root.bind('<Control-o>', openFile)
    root.bind('<Control-O>', openFile)
    root.bind('<Control-p>', locprinter)
    root.bind('<Control-P>', locprinter)
    root.bind('<Control-s>', saveFile)
    root.bind('<Control-S>', saveFile)
    root.bind('<Control-n>', newFile)
    root.bind('<Control-N>', newFile)
    root.bind('<Alt-F4>', quitapp)
    root.bind('<Alt-a>', soft)
    root.bind('<Alt-A>', soft)
    root.bind('<Control-b>', bold)
    root.bind('<Control-B>', bold)
    root.bind('<Control-L>', italicss)
    root.bind('<Control-l>', italicss)
    root.bind('<Control-U>', under)
    root.bind('<Control-u>', under)
    root.bind('<Control-F>', find)
    root.bind('<Control-f>', find)
    root.bind('<Control-R>', replace)
    root.bind('<Control-r>', replace)

    # Bind right-click event to show_menu function
    root.bind("<Button-3>", show_menu)

    # To Capture Close Window
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
