# -*- coding: utf-8 -*-
# tk10.pyw
import tkinter as tk

root = tk.Tk()
root.title(".config()")

lb = tk.Label(text="MS ゴシック, サイズ２０, 太字でない, 斜体, 河川なし, 取消線あり", font=("MS ゴシック", 20, "normal", "italic", "normal","overstrike"))
lb.pack()
root.mainloop()