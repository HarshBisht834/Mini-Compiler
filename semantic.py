
class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbols = set()
        self.errors = []
        self.analyze(self.ast)

    def analyze(self, nodes):
        for node in nodes:
            kind = node[0]
            if kind == 'DECLARE':
                self.symbols.add(node[1])
            elif kind == 'ASSIGN':
                _, var, expr = node
                self.symbols.add(var)
                if isinstance(expr, tuple):
                    _, left, right = expr
                    for v in (left, right):
                        if not v.isdigit() and v not in self.symbols:
                            self.errors.append(f"Undeclared variable: {v}")
                elif expr not in self.symbols and not expr.isdigit():
                    self.errors.append(f"Undeclared variable: {expr}")
            elif kind == 'IF':
                cond, body, else_body = node[1], node[2], node[3]
                if isinstance(cond, tuple):
                    _, left, right = cond
                    for v in (left, right):
                        if not v.isdigit() and v not in self.symbols:
                            self.errors.append(f"Undeclared variable in condition: {v}")
                self.analyze(body)
                self.analyze(else_body)
            elif kind == 'WHILE':
                cond, body = node[1], node[2]
                if isinstance(cond, tuple):
                    _, left, right = cond
                    for v in (left, right):
                        if not v.isdigit() and v not in self.symbols:
                            self.errors.append(f"Undeclared variable in loop: {v}")
                self.analyze(body)
            elif kind in ('PRINTF', 'SCANF'):
                for arg in node[1:] if isinstance(node[1], list) else [node[2]]:
                    if isinstance(arg, str) and arg not in self.symbols and not arg.startswith('"') and not arg.isdigit():
                        self.errors.append(f"Undeclared variable in {kind}: {arg}")
