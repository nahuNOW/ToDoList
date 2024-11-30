import tkinter as tk
from tkinter import messagebox
import datetime
import csv

def addToList():
    with open('ToDo.txt', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        currentTime = datetime.datetime.now()
        formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
        task = e.get()
        
        if task == "":
            messagebox.showwarning("Input Error", "Please enter a task.")
        else:
            writer.writerow([formattedTime + " : " + task])
            messagebox.showinfo("Done", "Your task was added to the list")

def createWindow():
    global e
    m = tk.Tk()
    m.title("To Do List")
    
    e = tk.Entry(m, width=40)
    e.pack(pady=10)
    
    addButton = tk.Button(m, text="Enter to List", width=25, command=addToList)
    addButton.pack(pady=10)
    
    m.mainloop()

createWindow()
