import tkinter as tk
from tkinter import messagebox
import json
from html_generator import HTMLGenerator

class EditorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Wix 2.0")
        self.master.geometry("500x600")
        self.master.configure(bg='#FFD700') 

        self.html_generator = HTMLGenerator()

        # Load initial content
        self.load_content()

        # Title Label
        self.title_label = tk.Label(master, text="Title:", font=("Arial", 14), bg='#FFD700', fg='#111111')
        self.title_label.pack(pady=5)

        self.title_entry = tk.Entry(master, font=("Arial", 14), width=40)
        self.title_entry.insert(0, self.content['title'])
        self.title_entry.pack(pady=5)

        # Description Label
        self.description_label = tk.Label(master, text="Description:", font=("Arial", 14), bg='#FFD700', fg='#111111')
        self.description_label.pack(pady=5)

        self.description_entry = tk.Entry(master, font=("Arial", 14), width=40)
        self.description_entry.insert(0, self.content['description'])
        self.description_entry.pack(pady=5)

        # Body Label
        self.body_label = tk.Label(master, text="Body:", font=("Arial", 14), bg='#FFD700', fg='#111111')
        self.body_label.pack(pady=5)

        self.body_text = tk.Text(master, font=("Arial", 14), width=40, height=10)
        self.body_text.insert(1.0, self.content['body'])
        self.body_text.pack(pady=5)

        # Buttons
        self.save_button = tk.Button(master, text="Save", font=("Arial", 12), bg='#FFFFFF', fg='#111111', width=40,
                                     activebackground='#FFC107', activeforeground='#111111', 
                                     command=self.save_content, relief='flat', borderwidth=5)
        self.save_button.pack(pady=10)

        self.edit_button = tk.Button(master, text="Edit", font=("Arial", 12), bg='#FFFFFF', fg='#111111', width=40, 
                                     activebackground='#FFC107', activeforeground='#111111', 
                                     command=self.enable_editing, relief='flat', borderwidth=5)
        self.edit_button.pack(pady=5)

        self.disable_editing()

    def load_content(self):
        try:
            with open('page_content.json', 'r') as file:
                self.content = json.load(file)
        except FileNotFoundError:
            self.content = {"title": "Default Title", "description": "Default Description", "body": "Default Body"}

    def save_content(self):
        self.content['title'] = self.title_entry.get()
        self.content['description'] = self.description_entry.get()
        self.content['body'] = self.body_text.get(1.0, tk.END).strip()

        with open('page_content.json', 'w') as file:
            json.dump(self.content, file, indent=4)

        self.html_generator.generate_html(self.content)
        messagebox.showinfo("Success", "Content saved successfully!")
        self.disable_editing()

    def enable_editing(self):
        self.title_entry.config(state='normal')
        self.description_entry.config(state='normal')
        self.body_text.config(state='normal')

    def disable_editing(self):
        self.title_entry.config(state='disabled')
        self.description_entry.config(state='disabled')
        self.body_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = EditorGUI(root)
    root.mainloop()
