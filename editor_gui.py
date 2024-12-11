import tkinter as tk
from tkinter import messagebox
from json_manager import JSONManager
from html_generator import HTMLGenerator

class ContentEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Content Editor")

        self.json_manager = JSONManager("static/page_content.json")
        self.html_generator = HTMLGenerator("static/index.html")

        self.text_area = tk.Text(root, width=50, height=20, wrap=tk.WORD)
        self.text_area.pack(pady=10)

        self.edit_button = tk.Button(root, text="Edit", command=self.enable_editing)
        self.edit_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save", command=self.save_content, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.load_content()

    def load_content(self):
        content = self.json_manager.read_content()
        self.text_area.insert(1.0, content)
        self.text_area.configure(state=tk.DISABLED)

    def enable_editing(self):
        self.text_area.configure(state=tk.NORMAL)
        self.save_button.configure(state=tk.NORMAL)

    def save_content(self):
        updated_content = self.text_area.get(1.0, tk.END).strip()

        if not updated_content:
            messagebox.showerror("Error", "Content cannot be empty!")
            return

        # Update JSON file
        self.json_manager.write_content(updated_content)

        # Update HTML file
        self.html_generator.generate_html(updated_content)

        self.text_area.configure(state=tk.DISABLED)
        self.save_button.configure(state=tk.DISABLED)
        messagebox.showinfo("Success", "Content saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContentEditorApp(root)
    root.mainloop()
