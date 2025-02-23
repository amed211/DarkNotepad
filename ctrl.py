# ctrl.py
# You can add your own shortcut keys to the shortcut file :)
import tkinter as tk
from tkinter import filedialog

def bind_shortcuts(notepad):
    notepad.root.bind("<Control-o>", lambda event: notepad.open_file())
    notepad.root.bind("<Control-s>", lambda event: save_file(notepad))
    notepad.root.bind("<Control-S>", lambda event: save_file(notepad))
    notepad.root.bind("<Control-Shift-S>", lambda event: save_as_file(notepad))
    notepad.root.bind("<Control-+>", lambda event: zoom_in(notepad))
    notepad.root.bind("<Control-minus>", lambda event: zoom_out(notepad))

def save_file(notepad):
    if hasattr(notepad, 'current_file') and notepad.current_file:
        with open(notepad.current_file, 'w', encoding='utf-8') as file:
            file.write(notepad.text_area.get("1.0", "end-1c"))
    else:
        save_as_file(notepad)

def save_as_file(notepad):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(notepad.text_area.get("1.0", "end-1c"))
        notepad.current_file = file_path
        notepad.root.title(f"Notparhe - {file_path}")

def zoom_in(notepad):
    current_font_size = int(notepad.text_area.cget("font").split()[-1])
    notepad.text_area.config(font=("Consolas", current_font_size + 2))

def zoom_out(notepad):
    current_font_size = int(notepad.text_area.cget("font").split()[-1])
    if current_font_size > 8:
        notepad.text_area.config(font=("Consolas", current_font_size - 2))
