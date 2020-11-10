import tkinter as tk

height = 500
width = 600

def test_function (entry):
    print("Chamado enviado", entry)

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='./download.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#003AFF')
frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.1, anchor='n')

# entry
entry = tk.Entry(frame, font=40)

# button
button = tk.Button(frame, text="Enviar", bg='white', font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.35, relheight=1, relwidth=0.3)

#
lower_frame = tk.Frame(root, bg='#003AFF', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Entry(lower_frame, font=40)
label.place(relwidth=1, relheight=1)

root.mainloop()