import random
import sys
from tkinter import messagebox, Tk
#from playsound import playsound


def crack_the_safe():
    guess = input("Guess what is the passcode to the safe: ")
    pass
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations


# ======================= DO NOT EDIT THE CODE BELOW =========================

random = random.randint(0, 1)


def try_code(guess):
    print("trying " + str(guess))

    secret_code = 8

    if int(guess) == secret_code:
        messagebox.showinfo(None, "Congratulations! You cracked the safe with " + str(guess))
        #play_the_sound_of_success()


#def play_the_sound_of_success():
    #playsound('me-gusta.wav')


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    crack_the_safe()
