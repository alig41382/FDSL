import json
from collections import OrderedDict

class JSONGenerator:
    def __init__(self):
        self.features = []
        self.types = OrderedDict()
        self.operators = {'<', '>', '==', '<=', '>=', '!=', '+', '-', '*', '/', 'AND', 'OR'}

    def generate(self, traversal):
        self.features.clear()
        self.types.clear()
        stack = []

        def infer_type(value):
            if value in {'true', 'false'}:
                return "boolean"
            elif value.startswith('"') and value.endswith('"'):
                return "string"
            try:
                float(value)
                return "number"
            except (ValueError, TypeError):
                return None

        def infer_result_type(left, right, operator):
            left_type = self.types.get(left, infer_type(left))
            right_type = self.types.get(right, infer_type(right))

            # Handle logical operators (AND, OR)
            if operator in {'AND', 'OR'}:
                if (left_type == "boolean" or left_type is None) and (right_type == "boolean" or right_type is None):
                    return "boolean"
                return None  # Invalid or unknown types

            # Handle comparison operators (<, >, ==, <=, >=, !=)
            if operator in {'<', '>', '<=', '>='}:
                if (left_type == "number" or left_type is None) and (right_type == "number" or right_type is None):
                    return "boolean"
                return None  # Comparison only valid for numbers
            if operator == '==':
                if left_type == right_type or left_type is None or right_type is None:
                    return "boolean"
                return None  # Types must match or be unknown

            # Handle arithmetic operators (+, -, *, /)
            if operator in {'+', '-', '*', '/'}:
                if operator == '+' and (left_type == "string" or right_type == "string"):
                    return "string"  # String concatenation
                if (left_type == "number" or left_type is None) and (right_type == "number" or right_type is None):
                    return "number"
                return None  # Invalid or unknown types

            return None

        for token in traversal:
            if token == 'FeatureDefinition':
                if stack:
                    _ = stack.pop()  # Pop operator or scope
                    feature = stack.pop()
                    self.features.append(feature)
            elif token in self.operators:
                if len(stack) < 2:
                    continue
                right = stack.pop()
                left = stack.pop()

                for var, other in [(left, right), (right, left)]:
                    if var.isidentifier() and var not in self.features and var not in self.types:
                        inferred_type = infer_type(other)
                        if inferred_type:
                            self.types[var] = inferred_type

                result_type = infer_result_type(left, right, token)
                if result_type:
                    # Store the expression with its inferred type
                    expression = f"({left} {token} {right})"
                    if expression not in self.types:
                        self.types[expression] = result_type
                    stack.append(expression)
                else:
                    stack.append(f"({left} {token} {right})")
            elif token not in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
                stack.append(token)

        input_schema = {
            name: self.types[name] for name in self.types
            if name.isidentifier() and name not in self.features
        }

        input_schema = {k: v for k, v in input_schema.items() if v is not None}

        return json.dumps({
            "input": input_schema,
            "features": self.features
        }, indent=2)