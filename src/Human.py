from GridWord import *
from word_search_generator import WordSearch
from word_search_generator.mask.shapes import *
from customtkinter import *
from pathlib import Path
from tkinter import *
from PlayAgainMenu import *
from About import *
from Alert import *
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter import filedialog
from WordList import *
import os


# Get path of image
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


'''
WINDOW
'''

# Make window
window = Tk()
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
position_right = int(window.winfo_screenwidth()/2 - window_width/2)
position_down = int(window.winfo_screenheight()/2 - window_height/2)

window.geometry("+{}+{}".format(position_right-400, position_down-300))
window.geometry("1181x708")
window.configure(bg = "#FFFFFF")

'''
CANVAS
'''

# Canvas frame
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 708,
    width = 1181,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

# Canvas image background
image_image_1 = PhotoImage(
    file=relative_to_assets("hu_image_1.png"))
image_1 = canvas.create_image(
    590.0,
    354.0,
    image=image_image_1
)
image_image_2 = PhotoImage(
    file=relative_to_assets("hu_image_2.png"))
image_2 = canvas.create_image(
    227.0,
    586.0,
    image=image_image_2
)
image_image_3 = PhotoImage(
    file=relative_to_assets("hu_image_3.png"))
image_3 = canvas.create_image(
    353.0,
    321.0,
    image=image_image_3
)
image_image_4 = PhotoImage(
    file=relative_to_assets("hu_image_4.png"))
image_4 = canvas.create_image(
    519.0,
    688.3294067382812,
    image=image_image_4
)

# Canvas BOARD
canvas.create_rectangle(
    332.0,
    37.0,
    962.0,
    667.0,
    fill="#F3F3F3",
    outline="")
canvas.create_rectangle(
    981.0,
    100.0,
    1163.0,
    667.0,
    fill="#F3F3F3",
    outline="")

# Canvas WORD SEARCH SHAPE
image_image_5 = PhotoImage(
    file=relative_to_assets("hu_image_5.png"))
image_5 = canvas.create_image(
    154.0,
    296.0,
    image=image_image_5
)
canvas.create_text(
    22.0,
    265.0,
    anchor="nw",
    text="Word search shape ",
    fill="#000000",
    font=("Nunito Regular", 20 * -1)
)

# Canvas DIFFICULTY LEVEL
image_image_7 = PhotoImage(
    file=relative_to_assets("hu_image_7.png"))
image_7 = canvas.create_image(
    154.0,
    383.0,
    image=image_image_7
)
canvas.create_text(
    22.0,
    354.0,
    anchor="nw",
    text="Difficulty Level ",
    fill="#000000",
    font=("Nunito Regular", 20 * -1)
)

# Canvas WORD SEARCH SIZE
image_image_9 = PhotoImage(
    file=relative_to_assets("hu_image_9.png"))
image_9 = canvas.create_image(
    154.0,
    470.0,
    image=image_image_9
)
canvas.create_text(
    22.0,
    435.0,
    anchor="nw",
    text="Word search size ",
    fill="#000000",
    font=("Nunito Regular", 20 * -1)
)
image_image_8 = PhotoImage(
    file=relative_to_assets("hu_image_8.png"))
image_8 = canvas.create_image(
    154.0,
    399.0,
    image=image_image_8
)
topic_image = PhotoImage(
    file=relative_to_assets("bg.png"))


'''
DEF
'''

# Canvas topic
def topic():
        topic_text = str(get_entry_data_2())
        size = 20
        if len(topic_text) > 14:
            size = int(size * 14 / len(topic_text))
        topic = Button(
            image=topic_image,
            text= topic_text,
            compound="center",  # Add this line
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Nunito Bold", size),  # Change the font size here
            fg="black",  # Change the font color here
        )
        topic.place(
            x=968.0,
            y=50.0,
            width=207.0,
            height=40.0
        )

# Draw puzzle and topic on the window
def generator():
    text1 = get_entry_data()
    text2 = get_entry_data_2()
    if text2 == "":
        alert2 = Alert(window, 2)
    elif text1 == "":
        alert1 = Alert(window, 1)
    else:
        make_puzzle()
        topic()

# Run about menu
def run_about():
    about_menu = About(window)

# Run play again menu    
def run_playagainmenu():
    again_menu = PlayAgainMenu(window, 1)

# Save pdf
def browse_directory():
    directory_path = filedialog.askdirectory()
    file_path = directory_path + "/puzzle.pdf"
    if os.path.exists(file_path):
        i = 1
        while os.path.exists(file_path):
            file_path = directory_path + "/puzzle(" + str(i) + ").pdf"
            i += 1
    puzzle.save(path= file_path)
    

# Get data from entry_1
def get_entry_data():
    text = entry_1.get("1.0", 'end-1c')
    if text == 'Type words here(Example: cat dog rat...)':
        text = ""
    words = text.split()
    size = get_radiobutton_selection()
    is_valid = True
    for wd in words:
        if len(wd) > size:
            words.remove(wd)
            is_valid = False
    if is_valid == False:
        remove_alert = Alert(window, 4)
    text = ",".join(words)
    return text

# Get data from entry_2
def get_entry_data_2():
    text = entry_2.get()
    return text

# Get hình dạng từ shape combobox 1
def get_combobox1_selection():
    selection = combobox1.get()  # Get the current selection from combobox
    return selection

# Get độ khó từ difficulty levels slider
def get_slider_value():
    value = slider.get()  # Get the current value from the slider
    return value

# Get kích thước từ word search size radiobutton
def get_radiobutton_selection():
    selection = size_var.get()  # Get the current selection from radiobutton
    if selection == "Small":
        return 15
    if selection == "Medium":
        return 17
    if selection == "Large":
        return 19

# SCRAMBLE THE PUZZLE
def make_puzzle():
    global puzzle
    level = int(get_slider_value())
    re_level = {
        1 : 1,
        2 : 2,
        3 : 8,
        4 : 7,
        5 : 4,
        6 : 5,
        7 : 3
    }.get(level)
    size = get_radiobutton_selection()
    mask = get_combobox1_selection()
    text = get_entry_data()
    puzzle = WordSearch(text, re_level, size) # Puzzle
    if mask == "Circle":
        puzzle.apply_mask(Circle())
    if mask == "Heart":
        puzzle.apply_mask(Heart())    
    if mask == "Diamond":
        puzzle.apply_mask(Diamond())
    if mask == "Hexagon":
        puzzle.apply_mask(Hexagon())
    if mask == "Octagon":
        puzzle.apply_mask(Octagon())
    if mask == "Pentagon":
        puzzle.apply_mask(Pentagon())
    words = [word.text for word in puzzle._words] # List of words
    hint = [word.position_xy for word in puzzle._words] # List of hint
    wordlist = WordList(window, words, hint) # Word list column
    grid = GridWord(window, puzzle._puzzle, words, hint, wordlist) # Grid word
    wordlist.setGrid(grid)

'''
BUTTONS
'''

# Canvas button 1: GENERATOR
button_image_1 = PhotoImage(
    file=relative_to_assets("hu_button_3.png"))
button_1 = Button(
    image=button_image_1,
    text="GENERATOR",
    compound="center",  # Add this line
    borderwidth=0,
    highlightthickness=0,
    command=generator,
    relief="flat",
    font=("Nunito Bold", 20),  # Change the font size here
    fg="white",  # Change the font color here
)
button_1.place(
    x=15.0,
    y=518.0,
    width=278.0,
    height=43.0
)

# Canvas button 2: EXPORT PDF
button_image_2 = PhotoImage(
    file=relative_to_assets("hu_button_1.png"))
button_2 = Button(
    image=button_image_2,
    text="EXPORT PDF",
    compound="center",  # Add this line
    borderwidth=0,
    highlightthickness=0,
    command= browse_directory,
    relief="flat",
    font=("Nunito Bold", 20),  # Change the font size here
    fg="white"  # Change the font color here
)
button_2.place(
    x=15.0,
    y=569.0,
    width=278.0,
    height=43.0
)

# Canvas button 3: PLAY AGAIN
button_image_3 = PhotoImage(
    file=relative_to_assets("hu_button_2.png"))
button_3 = Button(
    image=button_image_3,
    text="PLAY AGAIN",
    compound="center",  # Add this line
    borderwidth=0,
    highlightthickness=0,
    command=run_playagainmenu,
    relief="flat",
    font=("Nunito Bold", 20),  # Change the font size here
    fg="white"  # Change the font color here
)
button_3.place(
    x=15.0,
    y=620.0,
    width=278.0,
    height=43.0
)

# Canvas button 4: ABOUT
button_image_4 = PhotoImage(
    file=relative_to_assets("hu_button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=run_about,
    relief="flat"
)
button_4.place(
    x=7.0,
    y=0.0,
    width=35.0,
    height=35.0
)

# Canvas ENTRY 1: WORD LIST
entry_image_1 = PhotoImage(
    file=relative_to_assets("hu_entry_1.png"))
entry_bg_1 = canvas.create_image(
    154.5,
    165.5,
    image=entry_image_1
)
entry_1 = CTkTextbox(
    master=window,
    width=275,
    height=155,
    bg_color="#F3F3F3",
    fg_color="#F3F3F3",
    text_color="black",
    border_color="#F3F3F3",
    font=("Nunito", 14),
    scrollbar_button_color="#D18686",
    scrollbar_button_hover_color="#D18686"
)
def on_entry1_click(event):
    # function that gets called whenever entry1 is clicked
    if entry_1.get("1.0", 'end-1c') == 'Type words here(Example: cat dog rat...)':
        entry_1.delete("1.0", "end")  # delete all the text in the entry
        entry_1.insert("1.0", '')  # Insert blank for user input
def on_entry1_focusout(event):
    if entry_1.get("1.0", 'end-1c') == '':
        entry_1.insert("1.0", 'Type words here(Example: cat dog rat...)')
entry_1.bind('<FocusIn>', on_entry1_click)
entry_1.bind('<FocusOut>', on_entry1_focusout)
entry_1.insert("1.0", 'Type words here(Example: cat dog rat...)')
entry_1.place(
    x=17.0,
    y=90.0,
)

#canvas ENTRY 2: TOPIC
entry_image_2 = PhotoImage(
    file=relative_to_assets("hu_entry_2.png"))
entry_bg_2 = canvas.create_image(
    154.5,
    55.5,
    image=entry_image_2
)
entry_2 = CTkEntry(
    master=window,
    placeholder_text='Type topic here (Example: Animal)',
    placeholder_text_color="#D18686",
    width=270,
    font=("Nunito Bold", 14),
    text_color="black",
    bg_color="#F3F3F3",
    fg_color="#F3F3F3",
    border_color="#F3F3F3",
)
entry_2.place(
    x=16.0,
    y=43.0,
)

# Button List word search shape
values = ["Square", "Circle", "Heart", "Diamond", "Hexagon", "Octagon", "Pentagon"]  # Replace with your options
combobox1 = CTkComboBox(window, values=values, width=270, state="readonly", fg_color="white", dropdown_font=("Nunito", 13), dropdown_fg_color="white", dropdown_text_color="black", text_color="black", border_color="white", button_color="white", dropdown_hover_color="#D18686", button_hover_color="#D18686", bg_color="#F3F3F3", font=("Nunito", 15))
combobox1.set("Square")
x1, y1, x2, y2 = 100.0, 280.0, 205.0, 352.0
x = (x1 + x2) / 2
y = (y1 + y2) / 2
canvas.create_window(x, y, window=combobox1)

# Button Slider difficulty level
def sliding(value):
    my_label.configure(text=int(value))
slider = CTkSlider(master=window, from_=1, to=7, button_color="#D18686", progress_color="#D18686", bg_color="white", fg_color="#F3F3F3", border_color="white", width=220, number_of_steps=6, command=sliding)
x1, y1, x2, y2 = 100.0, 280.0, 205.0, 522.0
x = (x1 + x2) / 2 -10
y = (y1 + y2) / 2
canvas.create_window(x, y, window=slider)
my_label = CTkLabel(window, text=int(slider.get()), font=("Nunito", 16), text_color="#D18686", bg_color="white")
canvas.create_window(x+120, y, window=my_label)

#Button WORD SEARCH SIZE small - medium - large
size_var = StringVar()
radiobutton_small = CTkRadioButton(window, text="Small\n(15 x 15)", variable=size_var, value="Small", font=("Nunito", 14), bg_color="#F3F3F3", text_color="black", fg_color="#D18686")
radiobutton_medium = CTkRadioButton(window, text="Medium\n(17 x 17)", variable=size_var, value="Medium", font=("Nunito", 14), bg_color="#F3F3F3", text_color="black", fg_color="#D18686")
radiobutton_large = CTkRadioButton(window, text="Large\n(19 x 19)", variable=size_var, value="Large", font=("Nunito", 14), bg_color="#F3F3F3", text_color="black", fg_color="#D18686")
size_var.set("Small")
x1, y1, x2, y2 = 15.0, 394.0, 293.0, 500.0
x_small = x1 + (x2 - x1) / 6 + 15
x_medium = x1 + 3 * (x2 - x1) / 6 + 6
x_large = x1 + 4.5 * (x2 - x1) / 6 + 21
y = (y1 + y2) / 2 +40
canvas.create_window(x_small, y, window=radiobutton_small)
canvas.create_window(x_medium, y, window=radiobutton_medium)
canvas.create_window(x_large, y, window=radiobutton_large)


window.resizable(False, False)
window.mainloop()
