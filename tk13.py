# -*- coding: utf-8 -*-
# tk13.pyw
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
lb=tk.Label(text="this is a Lable. This is a Lable. This is a Label.")
ms=tk.Message(text="This is a Message.This is a Message.This is a Message.")
[widget.pack() for widget in(lb,ms)]
root.mainloop()