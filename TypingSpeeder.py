from tkinter import *
from tkinter import messagebox
import os
import random
import time
# pyinstaller --icon=icon.ico  --windowed TypingSpeeder.py



# Creating a new window and configurations
window = Tk()
window.iconbitmap("icon.ico")

window.title("Typing Speeder")
window.state('zoomed')
window.config(padx=80, pady=80, bg='#604CC3')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

start_time = time.time()

def text_open():
    # Specify the file name
    file_name = 'results.txt'

    # Check if the file exists
    if not os.path.isfile(file_name):
        # Create the file
        with open(file_name, 'w') as file:
            file.write("")

        print(f"File '{file_name}' created.")
    else:
        print(f"File '{file_name}' already exists.")

def rand_text():
    length = 35
    song = random.randint(1, 8)
    title = str(song)
    print(title)
    # Reading file with words
    file_path = f'piosenki/{title}.txt'
    with open(file_path, 'r', encoding='utf8', errors='ignore') as file:
        words_list = file.read().splitlines()
    words = []

    for line in words_list:
        for word in line.split(' '):
            words.append(word)

    words[:] = [x for x in words if x]
    lyrics = random.randint(0, len(words) - length - 1)

    words = ' '.join(words[lyrics:lyrics + length])
    words = ' ' + words
    return words





# Container frame for text_label
text_frame = Frame(window)


# Entry
entry = Entry(window, fg='white', bg="#FF7F3E", font=("Arial", 25, "normal"), width=50, borderwidth=0,
              justify='center')
entry.grid(column=1, columnspan=2, row=1)
entry.focus_set()



# Create labels once
label_grid = []



won_shown = False


def display_text():
    global text_frame
    global label_grid
    label_grid = []  # Reset label_grid
    text_frame.grid_forget()  # Remove previous text_frame
    text_frame = Frame(window, bg='#FFF6E9' )
    text_frame.grid(column=1, columnspan=2, row=0)


    row = 0
    col = 0

    for i, char in enumerate(random_string):
        if char == ' ' and col > 30:
            row += 1
            col = 0

        char_label = Label(text_frame, text=char, fg='blue', font=("Arial", 25, "normal"), bg='#FFF6E9', borderwidth=0)
        char_label.grid(row=row, column=col)

        label_grid.append(char_label)
        col+=1


def check_spelling(entry_text,
                   reference_text):
    result = []
    for index, sign in enumerate(entry_text):
        if index < len(reference_text) and sign == reference_text[index]:
            result.append(1)
        else:
            result.append(0)

    return result

def restart():

    global random_string
    global won_shown
    global start_time
    random_string = rand_text()
    won_shown = False

    display_text()
    entry.delete(0, 'end')
    #entry.insert(0, string='')
    start_time = time.time()
def on_key_release(event=None):

    entry_text = ' ' + entry.get()
    reference_text = random_string

    spelling_result = check_spelling(entry_text, reference_text)

    for i, char in enumerate(reference_text):
        if i < len(spelling_result):
            if spelling_result[i] == 1:
                color = 'green'

            else:
                color = 'red'

                if char == ' ':
                    char = '.'


        else:
            color = 'blue'


        label_grid[i].config(text=char, fg=color)

        if_won(entry_text, reference_text)



def if_won(entry_text, reference_text):
    global won_shown

    wynik = round(float(time.time() - start_time),2)
    print(wynik)
    if not won_shown and len(entry_text) == len(reference_text)  and 0 not in check_spelling(entry_text,
                                                                                             reference_text):
        won_shown = True

        with open('results.txt', 'r') as file:
            content = file.read().strip()
            if content:
                data = [float(num) for num in content.split()]
            else:
                data = []


        print(data)
        data.append(wynik)
        data.sort()
        klasyfikacja = data.index(wynik)
        data = data[:5]

        print(data)

        print(klasyfikacja)

        with open('results.txt', 'w') as file:
            file.write(' '.join(map(str, data)))

        text = ""
        for i, value in enumerate(data, start=1):
            text += f"{i}. {value}s\n"

        awans = False
        if klasyfikacja < 5:
            awans = True
            print('awans')
        if awans: text = text + f"\nWłaśnie zająłęś {klasyfikacja+1} miejsce."

        messagebox.showinfo("Info", f"Tekst przepisany!\nTwój czas to: {wynik} sekund.\n\n{text}\n")

        window.after(0, restart)


# Calls action() when pressed
button = Button(text="Start", activebackground="#FF7F3E", command=restart, bg='#3AA6B9')
button.grid(column=1, row=2,  columnspan=2)
button.config(padx=100, pady=50)

print(rand_text())
random_string = rand_text()
display_text()
text_open()


entry.bind("<KeyRelease>", on_key_release)

window.mainloop()
