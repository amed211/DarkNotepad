###################################################################################
#                                                                                 #
#                                                                                 #
#                    Alternative Notepad 📄                                       #
#                                                                                 #
#I am thinking of filling the other empty lines with the support of the community.#
#                                                                                 #
#                                                                                 #
#                                                                                 #
###################################################################################
import tkinter as tk
from tkinter import filedialog, messagebox
import sys
from ctrl import bind_shortcuts

class Notepad:
    def __init__(self, root, file_path=None):
        self.root = root
        self.root.title("Not Defteri")
        self.root.geometry("800x600")
        self.root.configure(bg="black")
        self.current_file = file_path

        self.text_area = tk.Text(self.root, wrap="word", undo=True, bg="black", fg="white", insertbackground="white", font=("Consolas", 12))
        self.text_area.pack(expand=1, fill="both")

        self.scrollbar = tk.Scrollbar(self.text_area, bg="gray", troughcolor="gray", activebackground="gray")
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.create_menu()
        bind_shortcuts(self)

        if file_path:
            self.load_file(file_path)

    def create_menu(self):
        menubar = tk.Menu(self.root, bg="black", fg="white")
        file_menu = tk.Menu(menubar, tearoff=0, bg="black", fg="white")
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save differently", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.load_file(file_path)
            self.current_file = file_path
            self.root.title(f"Notepad - {file_path}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as file:
                    content = self.text_area.get("1.0", tk.END)
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the file: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    content = self.text_area.get("1.0", tk.END)
                    file.write(content)
                self.current_file = file_path
                self.root.title(f"notepad - {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

    def load_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("error", f"An error occurred while uploading the file: {e}")

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    root = tk.Tk()
    app = Notepad(root, file_path)
    root.mainloop()
