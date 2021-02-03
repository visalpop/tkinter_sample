import tkinter as tk

def btn_press():
    st_id = en1.get()
    st_name =en2.get()
    print('STUDENT ID=>',st_id)
    print('STUDENT NAME=>',st_name)

root= tk.Tk()
lb1 = tk.Label(text='STUDENT ID')
en1 = tk.Entry()
lb2 = tk.Label(text='NAME')
en2 = tk.Entry()
btn = tk.Button(text='SET',command=btn_press)

[w.pack()for w in (lb1,en1,lb2,en2,btn)]
root.mainloop()