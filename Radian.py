import win32gui
import win32con

def minimize_terminal():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
import pymem
import os
import customtkinter
import tkinter
import subprocess
minimize_terminal()

customtkinter.set_appearance_mode("#000000")

app = customtkinter.CTk()
app.configure(bg="black")
app.geometry("545x300")
app.resizable(False, False)
app.title("github.com/MaddoxICY | If You Paid More Than 20$ you got scammed")

label = customtkinter.CTkLabel(master=app, text="MADE BY https://github.com/MaddoxICY", text_color="#FF0000")
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="process name",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

entry1 = customtkinter.CTkEntry(master=app,
                                placeholder_text="memory address",
                                width=120,
                                height=25,
                                border_width=2,
                                corner_radius=10)
entry1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

entry2 = customtkinter.CTkEntry(master=app,
                                placeholder_text="length",
                                width=120,
                                height=25,
                                border_width=2,
                                corner_radius=10)
entry2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

def button_event():
    procname = entry.get()
    print(procname)
    address = int(entry1.get(), 0)
    print(address)
    length = int(entry2.get(), 0)
    print(length)
    value = "."
    for x in range(length):
        value = value + '.'

    # Define your process ID here
    process_id = 1234

    handle = pymem.process.open(process_id, debug=True, process_access=pymem.constants.PROCESS_ALL_ACCESS)
    rs = pymem.memory.read_string(handle, address, byte=length)
    rb = pymem.memory.read_bytes(handle, address, length)

button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 fg_color="#FF0000",
                                 hover_color="#6A6767",
                                 text="remove string",
                                 command=button_event)
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
app.mainloop()
