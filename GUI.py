import os
import tkinter as tk
from tkinter import filedialog
from main import extract_data_from_pdf, save_results

#functions to open file dialog and get PDF file path

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF FILES", "*.pdf")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

#function to process PDF file and save results

def process_pdf():
    pdf_path = entry.get()
    results = extract_data_from_pdf(pdf_path)
    output_file = filedialog.asksaveasfilename(defaultextension=".xlsx",
                filetypes=[("Excel Files", ".xlsx")])
    save_results(results, output_file)

#GUI setup
window = tk.Tk()
window.geometry("400x200+10+20")
window.title("EOB Recoupment Finder")

greeting = tk.Label(window, text="WELCOME TO EOB RECOUPMENT FINDER",
    width=55, height=3)
greeting.pack()

label = tk.Label(text="PDF FILE")
entry = tk.Entry(width=50)
label.pack()
entry.pack()

browse_button = tk.Button(text="Browse", width=10, height=2, bg='gray20', fg='black',
    command=browse_pdf)
browse_button.pack()

process_button = tk.Button(text="Process PDF",width=10, height=2,bg='gray20', fg='black',
    command=process_pdf)
process_button.pack()

window.mainloop()