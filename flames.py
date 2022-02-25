from tkinter import *
from tkinter import messagebox


# ---------------------------------- clear button function -------------------------------------------------------------
def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    canvas.delete("all")


# -------------------------------- quit button function ----------------------------------------------------------------

def quit_window():
    window.destroy()


# ----------------------------------check button function --------------------------------------------------------------

def check():
    canvas.delete("all")
    name1 = str(entry1.get())
    name2 = str(entry2.get())
    n_list1 = list(name1.lower())
    n_list2 = list(name2.lower())
    if ' ' in n_list1:
        n_list1.remove(' ')
    if ' ' in n_list2:
        n_list2.remove(' ')

    calculate(n_list1, n_list2)


# ------------------------------- function for finding flames ----------------------------------------------------------


def calculate(name1, name2):
    temp1 = []
    temp2 = []
    f = ['f',
         'l',
         'a',
         'm',
         'e',
         's']

    for i in name1:
        if i not in name2:
            temp1.append(i)

    for i in name2:
        if i not in name1:
            temp2.append(i)
    remaining_no = len(temp1 + temp2)

    count = remaining_no

    while len(f) > 1:
        flag = (count % len(f) - 1)
        if flag >= 0:
            right = f[flag + 1:]
            left = f[: flag]
            f = right + left
        else:
            f = f[:len(f) - 1]

    switch = {'f': 'FRIENDSHIP',
              'l': 'LOVE',
              'a': 'AFFECTION',
              'm': 'MARRY',
              'e': 'ENEMY',
              's': 'SIBLINGS'}

    if (entry1.get() == "") or (entry2.get() == ""):
        messagebox.showerror("error", "Fields can't be empty ")
    else:
        store = open("names.txt", "a")
        if switch[f[0]] == 'MARRY':
            canvas.create_text(200, 50, fill="green", font="times 16 italic bold", text=(
                    str(entry1.get()) + " " + "and" + " " +
                    str(entry2.get()) + " are going to " + switch[f[0]]))

            store.write(str(entry1.get()) + " " + "and" + " " +
                        str(entry2.get()) + " are going to " + switch[f[0]]+"\n")

        elif switch[f[0]] == 'SIBLINGS' or switch[f[0]] == 'ENEMY':
            if switch[f[0]] == 'ENEMY':
                canvas.create_text(200, 50, fill="red", font="roman 16 bold", text=(
                        str(entry1.get()) + " " + "and" + " " +
                        str(entry2.get()) + " are " + switch[f[0]]))

                store.write(str(entry1.get()) + " " + "and" + " " +
                            str(entry2.get()) + " are " + switch[f[0]]+"\n")

            else:
                canvas.create_text(200, 50, font="times 16 italic bold", fill="green", text=(
                        str(entry1.get()) + " " + "and" + " " +
                        str(entry2.get()) + " are " + switch[f[0]]))

                store.write(str(entry1.get()) + " " + "and" + " " +
                            str(entry2.get()) + " are " + switch[f[0]]+"\n")

        else:
            canvas.create_text(200, 50, font="times 16 bold", fill="green", text=(
                    str(entry1.get()) + " " + "and" + " " +
                    str(entry2.get()) + " are in " + switch[f[0]]))

            store.write(str(entry1.get()) + " " + "and" + " " +
                        str(entry2.get()) + " are in " + switch[f[0]]+"\n")
            store.close()

# ---------------------------------- UI Design -------------------------------------------------------------------------

# setting window screen


window = Tk()
window.geometry('500x300')
window.title("flames app @amalraj")
title = Label(text="FLAMES", bg="pink", fg="white", border=2, relief="ridge", font='bold')
title.pack(side=TOP, fill=X)

# frame for enclosing entry

frame1 = Frame(window, height=200, width=500)
frame1.configure(bg="sky blue")

your_name = Label(frame1, text="YOUR NAME", bg="sky blue")
crush_name = Label(frame1, text="YOUR CRUSH NAME", bg="sky blue")

dot1 = Label(frame1, text=":", bg="sky blue")
dot2 = Label(frame1, text=":", bg="sky blue")

entry1 = Entry(frame1, width=52)
entry2 = Entry(frame1, width=52)

check_button = Button(frame1, text="CHECK", width=5, command=check)

check_button.grid(row=2, column=2, padx=5, pady=5)

your_name.grid(row=0, column=0, padx=5, pady=5)
crush_name.grid(row=1, column=0, padx=5, pady=5)
dot1.grid(row=0, column=1, padx=5, pady=5)
dot2.grid(row=1, column=1, padx=5, pady=5)
entry1.grid(row=0, column=2, padx=5, pady=5)
entry2.grid(row=1, column=2, padx=5, pady=5)
entry1.focus()

frame1.pack(fill="both", expand=True)

# frame for enclosing output display

frame2 = LabelFrame(window, text="RESULT", height=100, width=420)
frame2.configure(bg="pink")

canvas = Canvas(frame2, height=1, )
canvas.configure(bg='white')
canvas.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True, side=LEFT)

# frame for enclosing clear and quit button

frame3 = Frame(window, height=100, width=45)
frame3.configure(bg="sky blue")

clear_button = Button(frame3, text="CLEAR", width=5, command=clear)
quit_button = Button(frame3, text="QUIT", width=5, command=quit_window)

clear_button.grid(row=0, column=0, padx=20, pady=25)
quit_button.grid(row=1, column=0, padx=20)

frame3.pack(fill="both", expand=True)

window.bind('<Down>', lambda entry: entry2.focus_set())  # binds down key for going to lower entry
window.bind('<Up>', lambda entry: entry1.focus_set())  # binds up key for going to upper entry

window.bind('<Return>', lambda entry: check())  # binds return key for going to check button
window.mainloop()
