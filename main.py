import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from progi_ocen import progi

# Okno aplikacji
root = tk.Tk()
root.title("Moja aplikacja")
root.attributes('-topmost', 1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 400
window_height = 400

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(True,True)       #Można rozszerzać pionowo i poziomo
root.wm_maxsize(800, 800)       #Max rozmiar

# Configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Welcome Label
welcome_label = ttk.Label(
    root,
    text='Witaj w mojej pierwszej aplikacji!',
    background='red',
    foreground='white',
    font='Arial 15 underline bold',
    anchor='center',
    relief='ridge'
)

welcome_label.grid(column=0, row=0, columnspan=2, sticky='WE', ipady=10, padx=5)

# Image Label
photo = tk.PhotoImage(file='./pictures/images.png')
photo_label = ttk.Label(root, image=photo)
photo_label.grid(column=0, row=1, columnspan=2)

#  Points Label
points_label = ttk.Label(root, text='Podaj maksymalną liczbę punktów:')
points_label.grid(column=0, row=2, sticky='E')

# Points Entry
max_points = tk.StringVar()
points_entry = ttk.Entry(root, textvariable=max_points)
points_entry.grid(column=1, row=2, pady=1, sticky='W')
points_entry.focus()

# Checkbox
checkbox_var = tk.StringVar()

def check_changed():
    return checkbox_var == '1'

checkbox = ttk.Checkbutton(root,
                           text='Kocham mężusia',
                           command=check_changed,
                           variable=checkbox_var
                           )

checkbox.grid(column=1, row=3, sticky='NW')

# Message Info
def results():
    showinfo(
        title='Wyniki',
        message=progi(max_points.get())
    )

# 'Akceptuj' Button
akceptuj_button = ttk.Button(root, text='Akceptuj', command=results)
akceptuj_button.grid(column=0, row=4, columnspan=2, pady=20)

# Separator
separator = ttk.Separator(root, orient='horizontal')
separator.grid(column=0, row=5, columnspan=2, sticky='WE')

# 'Zamknij' Button
zamknij_button = ttk.Button(root, text='Zamknij', command=lambda: root.quit())
zamknij_button.grid(column=0, row=6, columnspan=2, pady=20, sticky='S')


root.mainloop()