from tkinter import *
import random
import csv

score = 0
words_list = []
showed_words = []
user_words = []
secs_left = 61
display = ' '

with open("words.txt", encoding="utf-8-sig") as data_file:
    data = csv.reader(data_file)
    for row in data:
        words_list.append(''.join(row))

win = Tk()
win.title('Typing Speed Test')
win.config(padx=50, pady=50, width=100)
win.after_id = None

canvas = Canvas(win, width=800, height=300, highlightthickness=0)
word_show = canvas.create_text(400, 150, text="Press the space bar after each word. \nPress start to begin.",
                               font=("Courier", 20, "bold"), fill='black', justify="left")
canvas.grid(row=2, column=0, columnspan=6)


def random_words():
    display = ' '
    display2 = ' '
    for i in range(6):
        display_word = random.choice(words_list)
        display_word2 = random.choice(words_list)
        showed_words.append(display_word)
        showed_words.append(display_word2)
        display += (display_word + ' ')
        display2 += (display_word2 + ' ')
        canvas.itemconfig(word_show, text=f'{display} \n{display2}')


def start():
    start_btn.destroy()
    timer.after(1000, count_down(secs_left))
    random_words()


def count_down(secs_left):
    timer.config(text=f'{secs_left}')
    if secs_left > 0:
        timer.after(1000, count_down, secs_left - 1)
    if secs_left == 0:
        messagewindow()


def user_type(event):
    user_words.append(input_box.get().lower().strip())
    input_box.delete(0, "end")
    if len(user_words) % 12 == 0:
        random_words()
    get_score()
    print(user_words)
    print(showed_words)


def get_score():
    global score
    correct_words = [word for word in user_words if word in words_list]
    score = len(correct_words)
    words_right.config(text=f'{score}')


def messagewindow():
    window = Toplevel()
    window.geometry('600x400')
    window.title('Times Up!')
    message = f'You typed {score} words.'
    socre_label = Label(window, text=message).pack()
    try_again = Button(window, text='Try again', command=win.destroy).pack()
    quit = Button(window, text='Quit', command=win.destroy).pack()


welcome = Label(font=('arial', 28),
                text="Welcome to the typing speed test! \n The average person can type 39 word per minute. Let's "
                     "see what you can do!")
welcome.grid(row=0, column=1)

explanation = Label(font=('arial', 28),
                    text="You will have 60 seconds to type as many of the words given as possible. \n You can "
                         "push the space bar to move to the next word quickly.")
explanation.grid(row=1, column=1)

words_right = Label(font=('arial', 24), text=f'{score}')
words_right.grid(row=2, column=0, padx=20)

timer = Label(font=('arial', 24), text=f'{secs_left}')

timer.grid(row=2, column=2, padx=20)

start_btn = Button(font=('arial', 24), text="Start", command=start)
start_btn.grid(row=3, column=2)

input_box = Entry(width=130)
input_box.grid(row=8, column=0, columnspan=3, pady=20)
input_box.focus()
win.bind('<space>', user_type)

quit_btn = Button(font=('arial', 24), text="Quit", command=quit)
quit_btn.grid(row=4, column=2)

win.mainloop()
