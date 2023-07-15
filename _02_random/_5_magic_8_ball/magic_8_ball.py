import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    #question = simpledialog.askstring(title='8ball', prompt="Should I trust this magic 8ball")
    question = input("What would you like to ask the magic 8ball?")

    # Make a variable and initialize it to a random number between 0 and 3
    random_number = random.randint(0,3)

    # If the random number is 0
    if random_number == 0:
        # tell the user "Yes"
        message = messagebox.showinfo(title= '8 ball answer', message= "Yes")

    # If the random number is 1
    elif random_number == 1:
        # tell the user "No"
        message = messagebox.showinfo(title= '8 ball answer', message= "No")

    # If the random number is 2
    elif random_number == 2:
        # tell the user "Maybe you should ask Google?"
        message = messagebox.showinfo(title= '8 ball answer', message= "Maybe you should ask Google?")

    # If the random number is 3
    elif random_number == 3:
        # write your own answer
        message = messagebox.showinfo(title= '8 ball answer', message= "Good luck with finding the answer to that")


