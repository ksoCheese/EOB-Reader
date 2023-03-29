import os
import tkinter as tk
from tkinter import filedialog, messagebox
from main import extract_data_from_pdf, save_results

#functions to open file dialog and get PDF file path

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF FILES", "*.pdf")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

#function to process PDF file and save results

def process_pdf():
    pdf_path = entry.get()
    if not pdf_path:
        messagebox.showerror(message="Please enter a file path", icon="warning")
        return

    results = extract_data_from_pdf(pdf_path)
    output_file = filedialog.asksaveasfilename(defaultextension=".xlsx",
                filetypes=[("Excel Files", ".xlsx")])

    if not output_file:
        messagebox.showwarning(message="Please enter an output file", icon="warning")
        return

    save_results(results, output_file)

#GUI setup
window = tk.Tk()
window.title("EOB Recoupment Finder")

window.geometry("600x300+10+20")
window.rowconfigure([0, 1, 2], weight=1)
window.columnconfigure(0, weight=1)

#Greeting
greeting = tk.Label(window, text="WELCOME TO EOB RECOUPMENT FINDER",
    font="Helvetica 18 bold", width=55, height=3)
greeting.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

#Browse PDF
label = tk.Label(window, text="PDF FILE")
entry = tk.Entry(window, width=35)
browse_button = tk.Button(window, text="Browse", width=10, height=2, bg='gray20', fg='black',
    command=browse_pdf)

label.grid(row=1, column=0, sticky="w", padx=5)
entry.grid(row=1, column=0, padx=5)
browse_button.grid(row=1, column=0, sticky="e", padx=5)

#Process PDF
process_button = tk.Button(window, text="Process PDF",fg='black',
    command=process_pdf)
process_button.grid(row=2, column=0, sticky="nsew", padx=150, pady=10)

window.mainloop()

