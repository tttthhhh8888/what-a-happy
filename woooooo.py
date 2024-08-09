print ("Woo"*10)
print ("Woo"*20)

import tkinter as tk

def on_button_click():
    current_value = scale.get()
    print(f"Selected Value: {current_value}")

root = tk.Tk()
root.title("Large Range Dial Example")

scale = tk.Scale(root, from_=0, to=99999999, orient='horizontal', length=600)
scale.pack()

button = tk.Button(root, text="Select", command=on_button_click)
button.pack()

label = tk.Label(root, text="Selected Value: 0")
label.pack()

root.mainloop()
