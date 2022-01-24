import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Arvude liitja")
label.pack()

liidetav1 = tk.Entry(fg="black", bg="gray", width=50)
liidetav1.pack()

liidetav2 = tk.Entry(fg="black", bg="gray", width=50)
liidetav2.pack()

def liida():
    summa = int(liidetav2.get()) + int(liidetav1.get())
    label = tk.Label(text=summa)
    label.pack()

button = tk.Button(
    text="Liida",
    width=25,
    height=5,
    bg="gray",
    fg="green",
    command = liida
)



button.pack()
window.mainloop()