import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("🔐 Password Generator")
        self.geometry("600x350")
        # self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # ---- Title ----
        header = ttk.Label(self, text="Password Generator", font=("Segoe UI", 18, "bold"))
        header.pack(pady=15)

        # ---- Options Frame ----
        options_frame = ttk.LabelFrame(self, text="Options", padding=10)
        options_frame.pack(fill="x", padx=20, pady=10)

        # Password Length
        ttk.Label(options_frame, text="Password Length:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.length_var = tk.IntVar(value=12)
        ttk.Spinbox(options_frame, from_=4, to=50, textvariable=self.length_var, width=5).grid(row=0, column=1, padx=5, pady=5)

        # Character Options
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        ttk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.use_upper).grid(row=1, column=0, sticky="w", padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.use_lower).grid(row=1, column=1, sticky="w", padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Digits (0-9)", variable=self.use_digits).grid(row=2, column=0, sticky="w", padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Symbols (!@#$)", variable=self.use_symbols).grid(row=2, column=1, sticky="w", padx=5, pady=2)

        # ---- Output Frame ----
        output_frame = ttk.LabelFrame(self, text="Generated Password", padding=10)
        output_frame.pack(fill="x", padx=20, pady=10)

        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(output_frame, textvariable=self.password_var, width=45, font=("Consolas", 12))
        self.password_entry.pack(side="left", padx=5, pady=5, fill="x", expand=True)

        ttk.Button(output_frame, text="Copy", command=self.copy_password).pack(side="right", padx=5)

        # ---- Strength Indicator ----
        strength_frame = ttk.Frame(self)
        strength_frame.pack(fill="x", padx=20, pady=5)

        ttk.Label(strength_frame, text="Strength:").pack(side="left", padx=5)
        self.strength_label = ttk.Label(strength_frame, text="N/A", font=("Segoe UI", 10, "bold"))
        self.strength_label.pack(side="left", padx=5)

        # ---- Big Buttons ----
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        self.generate_btn = ttk.Button(button_frame, text="🚀 Generate Password", command=self.generate_password)
        self.generate_btn.grid(row=0, column=0, padx=15, ipadx=10, ipady=5)

        self.clear_btn = ttk.Button(button_frame, text="❌ Clear", command=self.clear_password)
        self.clear_btn.grid(row=0, column=1, padx=15, ipadx=10, ipady=5)

    def generate_password(self):
        length = self.length_var.get()
        characters = ""

        if self.use_upper.get():
            characters += string.ascii_uppercase
        if self.use_lower.get():
            characters += string.ascii_lowercase
        if self.use_digits.get():
            characters += string.digits
        if self.use_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character set!")
            return

        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4!")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

        # Update strength meter
        self.check_strength(password)

    def check_strength(self, password):
        length = len(password)
        categories = sum([
            any(c.islower() for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            any(c in string.punctuation for c in password)
        ])

        if length >= 12 and categories >= 3:
            self.strength_label.config(text="Strong", foreground="green")
        elif length >= 8 and categories >= 2:
            self.strength_label.config(text="Medium", foreground="orange")
        else:
            self.strength_label.config(text="Weak", foreground="red")

    def copy_password(self):
        password = self.password_var.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

    def clear_password(self):
        self.password_var.set("")
        self.strength_label.config(text="N/A", foreground="black")


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
