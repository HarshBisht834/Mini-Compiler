import tkinter as tk
from gui import CompilerGUI
from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from icg import IntermediateCodeGenerator

def compile_code(source_code):
    try:
        lexer = Lexer(source_code)
        parser = Parser(lexer.tokens)
        semantic = SemanticAnalyzer(parser.ast)
        icg = IntermediateCodeGenerator(parser.ast)

        output = "Tokens:\n" + "\n".join(str(t) for t in lexer.tokens) + "\n\n"
        output += "AST:\n" + "\n".join(str(n) for n in parser.ast) + "\n\n"
        output += "Semantic Analysis:\n"
        output += "\n".join(semantic.errors) if semantic.errors else "No errors\n\n"
        output += "Intermediate Code:\n" + "\n".join(icg.code)

        gui.display_output(output)

    except Exception as e:
        gui.display_output(f"Error: {e}")

def load_sample():
    sample_code = (
        "x = 2;\n"
        "y = 5;\n"
        "while (x < y) {\n"
        "    if (x != 3) {\n"
        "        x = x + 1;\n"
        "    }\n"
        "}"
    )
    gui.insert_sample_code(sample_code)

root = tk.Tk()
gui = CompilerGUI(root, compile_callback=compile_code, load_samples_callback=load_sample)
root.mainloop()


