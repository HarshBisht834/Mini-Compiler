
# inter mediated code file created
class IntermediateCodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []
        self.temp_count = 1
        self.generate(self.ast)

    def new_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def generate(self, nodes):
        for node in nodes:
            kind = node[0]
            if kind == 'DECLARE':
                self.code.append(f"int {node[1]}")
            elif kind == 'ASSIGN':
                _, var, expr = node
                if isinstance(expr, tuple):
                    op, left, right = expr
                    temp = self.new_temp()
                    self.code.append(f"{temp} = {left} {op} {right}")
                    self.code.append(f"{var} = {temp}")
                else:
                    self.code.append(f"{var} = {expr}")
            elif kind == 'PRINTF':
                for arg in node[1]:
                    self.code.append(f"print {arg}")
            elif kind == 'SCANF':
                _, fmt, var = node
                self.code.append(f"read {var}  // {fmt}")
            elif kind == 'IF':
                cond, body, else_body = node[1], node[2], node[3]
                self.code.append(f"IF {cond[1]} {cond[0]} {cond[2]} GOTO THEN")
                if else_body:
                    self.generate(else_body)
                self.code.append("GOTO ENDIF")
                self.code.append("THEN:")
                self.generate(body)
                self.code.append("ENDIF:")
            elif kind == 'WHILE':
                cond, body = node[1], node[2]
                self.code.append("WHILE_START:")
                self.code.append(f"IF NOT {cond[1]} {cond[0]} {cond[2]} GOTO WHILE_END")
                self.generate(body)
                self.code.append("GOTO WHILE_START")
                self.code.append("WHILE_END:")
# edited again
