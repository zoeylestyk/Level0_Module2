import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    random1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    r4 = random.randint(1,6)
    r5 = random.randint(1,6)
    r6 = random.randint(1,6)

    # TODO 2) Display the selected numbers to the user in a pop-up
    message = messagebox.showinfo(title= 'Lottery Ticket', message = "Your lottery ticket numbers are: " + str(random1) + str(r2) + str(r3) + str(r4) + str(r5) + str(r6) + "!")
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
