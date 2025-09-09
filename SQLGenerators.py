class SQLGenerator:
    def __init__(self):
        self.operators = {'+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=', 'AND', 'OR'}
        self.logical_operators = {'>', '<', '>=', '<=', '==', '!=', 'AND', 'OR'}
        self.stack = []
        self.generated_lines = []

    def is_operator(self, token):
        return token in self.operators

    def is_boolean_expr(self, expr: str) -> bool:
        return any(op in expr for op in self.logical_operators)

    def generate(self, traversal):
        self.stack.clear()
        self.generated_lines.clear()

        for token in traversal:
            if token == 'FeatureDefinition':
                self.emit_assignment()
            elif self.is_operator(token):
                self.emit_binary(token)
            elif token in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
                continue
            else:
                self.stack.append(token)

        return ',\n'.join(self.generated_lines)

    def emit_assignment(self):
        value_expr = self.stack.pop()
        feature_name = self.stack.pop()

        if self.is_boolean_expr(value_expr):
            line = f"CASE WHEN {value_expr} THEN TRUE ELSE FALSE END AS {feature_name}"
        else:
            line = f"{value_expr} AS {feature_name}"

        self.generated_lines.append(line)

    def emit_binary(self, operator):
        right = self.stack.pop()
        left = self.stack.pop()

        # Normalize operators
        if operator == '==':
            operator = '='
        elif operator == '!=':
            operator = '<>'

        # Format string and boolean literals
        if right.startswith('"') and right.endswith('"'):
            right = f"'{right[1:-1]}'"
        elif right.lower() in {'true', 'false'}:
            right = right.upper()

        # Optional: wrap division by zero
        if operator == '/':
            expr = f"CASE WHEN {right} = 0 THEN NULL ELSE {left} / {right} END"
        else:
            expr = f"{left} {operator} {right}"

        self.stack.append(expr)