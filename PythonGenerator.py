class PythonGenerator:
    def __init__(self):
        self.operators = {'+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=', 'AND', 'OR'}
        self.stack = []
        self.generated_lines = []

    def is_operator(self, token):
        return token in self.operators

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
                self.stack.append(self.format_token(token))

        return '\n'.join(self.generated_lines)

    def emit_assignment(self):
        value = self.stack.pop()
        feature = self.stack.pop()
        if feature.startswith('df["') and feature.endswith('"]'):
            feature = feature[4:-2]
        self.generated_lines.append(f'df["{feature}"] = {value}')

    def emit_binary(self, operator):
        right = self.stack.pop()
        left = self.stack.pop()

        if operator in {'AND', 'OR'}:
            py_op = '&' if operator == 'AND' else '|'
            expr = f"({left}) {py_op} ({right})"
        else:
            expr = f"({left} {operator} {right})"

        self.stack.append(expr)

    def format_token(self, token):
        if token in {'true', 'false'}:
            return token.capitalize()  # True / False
        elif token.startswith('"') and token.endswith('"'):
            return token  # e.g., "female"
        elif token.replace('.', '', 1).isdigit():
            return token
        elif token.isidentifier():
            return f'df["{token}"]'
        else:
            return token




# class PythonGenerator:
#     def __init__(self):
#         self.operators = {'+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=', 'AND', 'OR'}
#         self.stack = []
#         self.generated_lines = []
#
#     def is_operator(self, token):
#         return token in self.operators
#
#     def generate(self, traversal):
#         self.stack.clear()
#         self.generated_lines.clear()
#
#         for token in traversal:
#             if token == 'FeatureDefinition':
#                 self.emit_assignment()
#             elif self.is_operator(token):
#                 self.emit_binary(token)
#             elif token in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
#                 continue  # Structural only
#             else:
#                 self.stack.append(self.format_token(token))
#
#         return '\n'.join(self.generated_lines)
#
#     def unformat_feature(self, token: str) -> str:
#         # turn df["is_active"] -> is_active
#         if token.startswith('df["') and token.endswith('"]'):
#             return token[4:-2]
#         return token
#
#     def emit_assignment(self):
#         value = self.stack.pop()
#         feature = self.unformat_feature(self.stack.pop())
#         line = f'df["{feature}"] = {value}'
#         self.generated_lines.append(line)
#
#     def emit_binary(self, operator):
#         right = self.stack.pop()
#         left = self.stack.pop()
#
#         if operator in {'AND', 'OR'}:
#             py_op = '&' if operator == 'AND' else '|'
#             expr = f"({left}) {py_op} ({right})"
#         else:
#             expr = f"({left} {operator} {right})"
#
#         self.stack.append(expr)
#
#     def format_token(self, token):
#         if token.isnumeric():
#             return token
#         elif token.isidentifier():
#             return f'df["{token}"]'
#         else:
#             return token
