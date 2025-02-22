import tkinter as tk
from tkinter import filedialog, messagebox

def open_file(event=None):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, file.read())
            root.title(f"ANote Pathe - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"File could not be openedFile could not be opened: {e}")

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get("1.0", tk.END))
            root.title(f"ANote Pathe - {file_path}")
        except Exception as e:
            messagebox.showerror("Eror", f"File could not be savedFile could not be saved: {e}")

def new_file(event=None):
    text_area.delete("1.0", tk.END)
    root.title(Notepad - New File)

def exit_app(event=None):
    if messagebox.askokcancel("Exit", "Are you sure you want to exit the programAre you sure you want to exit the program?"):
        root.destroy()

def zoom_in(event=None):
    global font_size
    font_size += 2
    text_area.config(font=("Consolas", font_size))

def zoom_out(event=None):
    global font_size
    if font_size > 6:
        font_size -= 2
        text_area.config(font=("Consolas", font_size))

def reset_zoom(event=None):
    global font_size
    font_size = default_font_size
    text_area.config(font=("Consolas", font_size))

root = tk.Tk()
root.title("Not Defteri")
root.geometry("900x500")
root.configure(bg="gray20")

default_font_size = 14
font_size = default_font_size

menu_bar = tk.Menu(root, bg="black", fg="white", activebackground="gray", activeforeground="black", bd=0)
file_menu = tk.Menu(menu_bar, tearoff=0, bg="black", fg="white", activebackground="gray", activeforeground="black")
file_menu.add_command(label="New (Ctrl+N)", command=new_file)
file_menu.add_command(label="Open (Ctrl+O)", command=open_file)
file_menu.add_command(label="Save (Ctrl+S)", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit (Ctrl+Q)", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

frame = tk.Frame(root, bg="gray20")
frame.pack(fill="both", expand=True)

text_area = tk.Text(frame, bg="black", fg="white", insertbackground="white", undo=True, wrap="word", bd=0, relief="flat", font=("Consolas", font_size))
text_area.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, bg="black", troughcolor="gray20", activebackground="gray", bd=0)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=text_area.yview, troughcolor="gray20", bg="gray")
text_area.config(yscrollcommand=scrollbar.set)

root.bind("<Control-s>", save_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-n>", new_file)
root.bind("<Control-q>", exit_app)
root.bind("<Control-plus>", zoom_in)   # Ctrl + +
root.bind("<Control-minus>", zoom_out) # Ctrl + -
root.bind("<Control-0>", reset_zoom)   # Ctrl + 0
text_area.bind("<Control-x>", lambda e: text_area.event_generate("<<Cut>>"))
text_area.bind("<Control-c>", lambda e: text_area.event_generate("<<Copy>>"))
text_area.bind("<Control-v>", lambda e: text_area.event_generate("<<Paste>>"))

root.mainloop()
