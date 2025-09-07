#handling type
class SQLGenerator:
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
                self.stack.append(token)

        return ',\n'.join(self.generated_lines)

    def emit_assignment(self):
        value_expr = self.stack.pop()
        feature_name = self.stack.pop()
        line = f"CASE WHEN ({value_expr}) THEN TRUE ELSE FALSE END AS {feature_name}"
        self.generated_lines.append(line)

    def emit_binary(self, operator):
        right = self.stack.pop()
        left = self.stack.pop()

        if operator == '==':
            operator = '='
        elif operator == '!=':
            operator = '<>'

        if right.startswith('"') and right.endswith('"'):
            right = f"'{right[1:-1]}'"
        elif right in {'true', 'false'}:
            right = right.upper()

        expr = f"{left} {operator} {right}"
        self.stack.append(expr)



# class SQLGenerator:
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
#                 continue
#             else:
#                 self.stack.append(token)
#
#         return ',\n'.join(self.generated_lines)
#
#     def emit_assignment(self):
#         value_expr = self.stack.pop()
#         feature_name = self.stack.pop()
#         condition = f"({value_expr})"
#         line = f"CASE WHEN {condition} THEN TRUE ELSE FALSE END AS {feature_name}"
#         self.generated_lines.append(line)
#
#     def emit_binary(self, operator):
#         right = self.stack.pop()
#         left = self.stack.pop()
#
#         if operator == '==':
#             operator = '='
#         elif operator == '!=':
#             operator = '<>'
#
#         if right.startswith('"') and right.endswith('"'):
#             right = f"'{right[1:-1]}'"  # Convert to single-quoted string for SQL
#
#         expr = f"{left} {operator} {right}"
#         self.stack.append(expr)
