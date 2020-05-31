from tkinter import *
from tkinter import ttk

def main():
    # creates window instance
    window = Tk()
    window.geometry('320x400')

    activity_combo = ttk.Combobox(window, width=20)
    activity_combo.grid(column=0, row=0)

    clock_frame = ttk.Frame(window, width=300, height=100, relief='solid', borderwidth=1)
    clock_frame.grid(column=0, row=1, padx=10, pady=10)

    start_stop_button = ttk.Button(window, width=20, text='Start/Stop')
    start_stop_button.grid(column=0, row=2)

    reset_clock_button = ttk.Button()

    # keeps tkinter window open (last line of program)
    window.mainloop()

if __name__ == "__main__":
    main()