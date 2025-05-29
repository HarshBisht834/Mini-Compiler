class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.keywords = {'if', 'else', 'while', 'return', 'int', 'printf', 'scanf'}
        self.current = 0
        self.tokenize()

    def tokenize(self):
        while self.current < len(self.code):
            ch = self.code[self.current]

            if ch.isspace():
                self.current += 1
            elif ch == '"':
                self.tokens.append(self.tokenize_string())
            elif ch.isalpha() or ch == '_':
                self.tokens.append(self.tokenize_identifier())
            elif ch.isdigit():
                self.tokens.append(self.tokenize_number())
            elif ch in '+-*/=<>!%':
                self.tokens.append(self.tokenize_operator())
            elif ch == ';':
                self.tokens.append(('END', ';'))
                self.current += 1
            elif ch == ',':
                self.tokens.append(('COMMA', ','))
                self.current += 1
            elif ch == '(':
                self.tokens.append(('LPAREN', '('))
                self.current += 1
            elif ch == ')':
                self.tokens.append(('RPAREN', ')'))
                self.current += 1
            elif ch == '{':
                self.tokens.append(('LBRACE', '{'))
                self.current += 1
            elif ch == '}':
                self.tokens.append(('RBRACE', '}'))
                self.current += 1
            elif ch == '&':
                self.tokens.append(('ADDRESS', '&'))
                self.current += 1
            else:
                raise Exception(f"Unknown character: {ch}")

    def tokenize_string(self):
        self.current += 1  # skip opening quote
        start = self.current
        while self.current < len(self.code) and self.code[self.current] != '"':
            self.current += 1
        value = self.code[start:self.current]
        self.current += 1  # skip closing quote
        return ('STRING', value)

    def tokenize_identifier(self):
        start = self.current
        while self.current < len(self.code) and (self.code[self.current].isalnum() or self.code[self.current] == '_'):
            self.current += 1
        text = self.code[start:self.current]
        token_type = text.upper() if text in self.keywords else 'ID'
        return (token_type, text)

    def tokenize_number(self):
        start = self.current
        while self.current < len(self.code) and self.code[self.current].isdigit():
            self.current += 1
        return ('NUMBER', self.code[start:self.current])

    def tokenize_operator(self):
        start = self.current
        next_char = self.code[self.current + 1] if self.current + 1 < len(self.code) else ''
        if next_char == '=':
            op = self.code[self.current:self.current + 2]
            self.current += 2
        else:
            op = self.code[self.current]
            self.current += 1
        return ('OP', op)
        # added
