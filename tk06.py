import tkinter as tk

def action_btn_press():
    print('VISAL was HERE!')

root = tk.Tk()
root.title('Widget+Action')
root.geometry('350x150')
lb = tk.Label(text='Label-1')
bt = tk.Button(text='Button-1', command=action_btn_press)
lb.pack()
bt.pack()
root.mainloop()