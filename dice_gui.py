import random
import tkinter
root = tkinter.Tk()

root.geometry("900x500")

root.iconbitmap(r'C:\\Users\\Kartikey\\Desktop')
text_1 = tkinter.Label(root, text = ' ', font = ("arial", 400), bg='pink')

def roll_the_dice():
    num_code = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    text_1.config(text = f'{random.choice(num_code)}{random.choice(num_code)}')
    text_1.pack()

button_1 = tkinter.Button(root, text = "Roll the Dice", command = roll_the_dice, bg='purple' )
button_1.place(x = 400,y = 0)


root.mainloop()