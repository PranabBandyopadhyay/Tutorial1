import threadsafe_tkinter as tk

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

"""def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("HANGMAN")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()"""


a = "    O  " \
    "   /|\ " \
    "   / \  "

b = "    O  " \
    "   /|\ " \
    "   /  "

c = "    O  " \
    "   /|\ "

d = "    O  " \
    "   /| "

e = "    O  " \
    "    | "

f = "    O  "

g = " DEAD"

popup = tk.Tk()
popup.wm_title("HANGMAN")


def hmdraw(count):



    if count == 0:
        popup = tk.Tk()
        popup.wm_title("HANGMAN")
        label = tk.Label(popup, text=a, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        popup.destroy()

    elif count == 1:
        popup = tk.Tk()
        popup.wm_title("HANGMAN")
        label = tk.Label(popup, text=b, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        popup.destroy()

    elif count == 2:
        popup = tk.Tk()
        popup.wm_title("HANGMAN")
        label = tk.Label(popup, text=c, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        popup.destroy()

    elif count == 3:
        popup = tk.Tk()
        popup.wm_title("HANGMAN")
        label = tk.Label(popup, text=d, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        popup.destroy()

    elif count == 4:
        popup = tk.Tk()
        popup.wm_title("HANGMAN")
        label = tk.Label(popup, text=e, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        popup.destroy()

    elif count == 5:
        popup = tk.Tk()
        popup.wm_title("HANGMAN")
        label = tk.Label(popup, text=f, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        popup.destroy()

    elif count == 6:
        popup = tk.Tk()
        popup.wm_title("HANGMAN")
        label = tk.Label(popup, text=g, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)

    popup.mainloop()

for i in range(0,6):
    hmdraw(i)

