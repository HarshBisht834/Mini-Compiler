class Parser:
    def _init_(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.ast = self.parse_statements()

    def current_token(self):
        return self.tokens[self.position] if self.position < len(self.tokens) else ('EOF', '')

    def eat(self, expected_type=None):
        token = self.current_token()
        if expected_type is None or token[0] == expected_type:
            self.position += 1
            return token
        else:
            raise Exception(f"Expected {expected_type}, got {token}")

    def parse_statements(self):
        stmts = []
        while self.position < len(self.tokens):
            if self.current_token()[0] == 'RBRACE':
                break
            stmts.append(self.parse_statement())
        return stmts

    def parse_statement(self):
        token = self.current_token()
        if token[0] == 'INT':
            self.eat('INT')
            var = self.eat('ID')[1]
            self.eat('END')
            return ('DECLARE', var)
        
        elif token[0] == 'ID':
            var = self.eat('ID')[1]
            if self.current_token()[0] == 'OP' and self.current_token()[1] == '=':
                self.eat('OP')
                expr = self.parse_expression()
                self.eat('END')
                return ('ASSIGN', var, expr)
        elif token[0] == 'PRINTF':
            self.eat('PRINTF')
            self.eat('LPAREN')
            args = self.parse_arguments()
            self.eat('RPAREN')
            self.eat('END')
            return ('PRINTF', args)
        elif token[0] == 'SCANF':
            self.eat('SCANF')
            self.eat('LPAREN')
            fmt = self.eat('STRING')[1]
            self.eat('COMMA')
            self.eat('ADDRESS')  
            var = self.eat('ID')[1]
            self.eat('RPAREN')
            self.eat('END')
            return ('SCANF', fmt, var)
        elif token[0] == 'IF':
            self.eat('IF')
            self.eat('LPAREN')
            cond = self.parse_expression()
            self.eat('RPAREN')
            self.eat('LBRACE')
            if_body = self.parse_statements()
            self.eat('RBRACE')
            else_body = []
            if self.current_token()[0] == 'ELSE':
                self.eat('ELSE')
                self.eat('LBRACE')
                else_body = self.parse_statements()
                self.eat('RBRACE')
            return ('IF', cond, if_body, else_body)
        elif token[0] == 'WHILE':
            self.eat('WHILE')
            self.eat('LPAREN')
            cond = self.parse_expression()
            self.eat('RPAREN')
            self.eat('LBRACE')
            body = self.parse_statements()
            self.eat('RBRACE')
            return ('WHILE', cond, body)
        else:
            raise Exception(f"Unexpected token: {token}")

    def parse_expression(self):
        left = self.eat(self.current_token()[0])
        if self.current_token()[0] == 'OP':
            op = self.eat('OP')[1]
            right = self.eat(self.current_token()[0])
            return (op, left[1], right[1])
        return left[1]

    def parse_arguments(self):
        args = []
        while self.current_token()[0] not in ('RPAREN', 'EOF'):
            token = self.eat(self.current_token()[0])
            if token[0] != 'COMMA':
                args.append(token[1])
        return args