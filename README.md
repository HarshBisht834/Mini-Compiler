# Mini Compiler with GUI for Procedural Language

This is a Python-based Mini Compiler for a procedural programming language with an interactive GUI built using Tkinter. It performs all major compilation phases, including:

- Lexical Analysis
- Syntax Analysis
- Semantic Analysis
- Intermediate Code Generation (ICG)

## 💻 Features

- Compile C-style code with variables, control structures (`if`, `else`, `while`), and function calls (`printf`, `scanf`).
- Real-time compilation with visual output for each phase: Tokens (Lexical), Abstract Syntax Tree (AST), Semantic Errors, and Intermediate Code Generation (ICG).
- Graphical interface for easy code editing and output viewing.
- Pure Python implementation — no external libraries or APIs used.

## 📁 Project Structure


MiniCompiler/

├── lexer.py # Lexical Analyzer
├── parser.py # Syntax Analyzer (Parser)
├── semantic.py # Semantic Analyzer
├── icg.py # Intermediate Code Generator
├── gui.py # GUI with Tkinter
├── main.py # Entry point to run the compiler
└── README.md # Project documentation

