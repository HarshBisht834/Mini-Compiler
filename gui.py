import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class CompilerGUI:
    def __init__(self, root, compile_callback, load_samples_callback):
        self.root = root
        self.root.title("Mini Compiler")
        self.compile_callback = compile_callback
        self.load_samples_callback = load_samples_callback

        # Fonts and Colors
        self.font = ("Courier New", 12)
        self.bg_color = "#f4f4f4"
        self.text_color = "#000000"

        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("1000x700")
        self.root.configure(bg=self.bg_color)

        # Frame for code editor and line numbers
        editor_frame = tk.Frame(self.root, bg=self.bg_color)
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Line number display
        self.line_numbers = tk.Text(editor_frame, width=4, padx=5, bg="#eaeaea", fg="gray", font=self.font, state='disabled')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Code editor
        self.code_editor = tk.Text(editor_frame, font=self.font, bg="white", fg=self.text_color, undo=True, wrap="none")
        self.code_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.code_editor.bind("<KeyRelease>", self.update_line_numbers)

        # Buttons Frame
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(fill=tk.X, padx=10)

        compile_btn = tk.Button(button_frame, text="Compile", font=self.font, command=self.on_compile)
        compile_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = tk.Button(button_frame, text="Clear Output", font=self.font, command=self.clear_output)
        clear_btn.pack(side=tk.LEFT, padx=5)

        sample_btn = tk.Button(button_frame, text="Load Sample Code", font=self.font, command=self.load_samples_callback)
        sample_btn.pack(side=tk.LEFT, padx=5)

        # Output Box
        self.output_box = scrolledtext.ScrolledText(self.root, height=15, font=("Courier New", 11), bg="black", fg="lime", wrap="word")
        self.output_box.pack(fill=tk.BOTH, expand=False, padx=10, pady=(0, 10))

        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        code = self.code_editor.get("1.0", "end-1c")
        lines = code.split("\n")
        self.line_numbers.config(state='normal')
        self.line_numbers.delete("1.0", tk.END)
        for i in range(1, len(lines)+1):
            self.line_numbers.insert(tk.END, f"{i}\n")
        self.line_numbers.config(state='disabled')

    def on_compile(self):
        source_code = self.code_editor.get("1.0", tk.END)
        self.compile_callback(source_code)

    def display_output(self, output_text):
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, output_text)

    def clear_output(self):
        self.output_box.delete("1.0", tk.END)

    def insert_sample_code(self, code):
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, code)
        self.update_line_numbers()




