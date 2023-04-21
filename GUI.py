import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
from main import extract_data_from_pdf, save_results

# Functions to open file dialog and get PDF file path
def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF FILES", "*.pdf")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

# Function to process PDF file and save results
def process_pdf():
    pdf_path = entry.get()
    if not pdf_path:
        messagebox.showerror(message="Please enter a file path", icon="warning")
        return

    results = extract_data_from_pdf(pdf_path)

    if file_mode.get() == "create":
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                   filetypes=[("Excel Files", ".xlsx")])
    else:
        output_file = filedialog.askopenfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel Files", ".xlsx")])

    if not output_file:
        messagebox.showwarning(message="Please enter an output file", icon="warning")
        return

    save_results(results, output_file, file_mode.get())

    # Open the output file with the default application
    os.system(f'open "{output_file}"')

# GUI setup
window = tk.Tk()
window.title("EOB Recoupment Finder")

window.geometry("600x300+10+20")
window.rowconfigure([0, 1, 2, 3, 4], weight=1)
window.columnconfigure(0, weight=1)

# Greeting
greeting = tk.Label(window, text="WELCOME TO EOB RECOUPMENT FINDER",
    font="Helvetica 18 bold", width=55)
greeting.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

# Browse PDF
label = tk.Label(window, text="PDF FILE")
entry = tk.Entry(window, width=35)
browse_button = ttk.Button(window, text="Browse", command=browse_pdf)

label.grid(row=1, column=0, sticky="w", padx=20)
entry.grid(row=1, column=0, padx=5)
browse_button.grid(row=1, column=0, sticky="e", padx=5)

# Radio buttons for file mode selection
file_mode = tk.StringVar(value="create")
select_file_mode = tk.Label(window, text="Select file mode:")
create_file_radio = tk.Radiobutton(window, text="Create new file", variable=file_mode, value="create")
update_file_radio = tk.Radiobutton(window, text="Update existing file", variable=file_mode, value="update")

select_file_mode.grid(row=3, column=0, sticky="w", padx=20)
create_file_radio.grid(row=3, column=0)
update_file_radio.grid(row=3, column=0, sticky="e", padx=5)

# Process PDF
process_button = tk.Button(window, text="Process PDF", command=process_pdf)
process_button.grid(row=4, column=0, sticky="nsew", padx=200, pady=20)

window.mainloop()

