import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

for i in range(10):
    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    if random_number == 1:
        print("Nice shirt!")
    elif random_number == 2:
        print("You have a great smile!")
    elif random_number == 3:
        print("Your hair is looking great today!")
    elif random_number == 4:
        print("You're really smart!")
    elif random_number == 5:
        print("Has anyone told you that you are looking great today?!")
    else:
        print("Hm")
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
