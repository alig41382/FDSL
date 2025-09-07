#typehandling by chatgpt
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

        for token in traversal:
            if token == 'FeatureDefinition':
                _ = stack.pop()          # expression (ignored here)
                feature = stack.pop()
                if feature.startswith('df["') and feature.endswith('"]'):
                    feature = feature[4:-2]
                self.features.append(feature)

            elif token in self.operators:
                right = stack.pop()
                left = stack.pop()

                # Check if any side is a string literal
                def is_string_literal(x): return x.startswith('"') and x.endswith('"')

                # Check if any side is a boolean literal
                def is_boolean_literal(x): return x.lower() in ('true', 'false')

                # Check if any side is a float literal
                def is_float_literal(x):
                    try:
                        float(x)
                        return True
                    except ValueError:
                        return False

                # Check if any side is an integer literal
                def is_int_literal(x):
                    try:
                        int(x)
                        return True
                    except ValueError:
                        return False

                # Clean token
                def normalize(x):
                    if x.startswith('df["') and x.endswith('"]'):
                        return x[4:-2]
                    return x

                l = normalize(left)
                r = normalize(right)

                # Infer type for left if it's an identifier
                if l.isidentifier() and l not in self.features:
                    if is_string_literal(right):
                        self.types[l] = "string"
                    elif is_boolean_literal(right):
                        self.types[l] = "boolean"
                    elif is_int_literal(right):
                        self.types[l] = "integer"
                    elif is_float_literal(right):
                        self.types[l] = "float"
                    else:
                        self.types[l] = self.types.get(l, "number")

                # Infer type for right if it's an identifier
                if r.isidentifier() and r not in self.features:
                    if is_string_literal(left):
                        self.types[r] = "string"
                    elif is_boolean_literal(left):
                        self.types[r] = "boolean"
                    elif is_int_literal(left):
                        self.types[r] = "integer"
                    elif is_float_literal(left):
                        self.types[r] = "float"
                    else:
                        self.types[r] = self.types.get(r, "number")

                stack.append(f"({left} {token} {right})")

            elif token not in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
                stack.append(token)

        input_schema = {name: self.types.get(name, "number") for name in self.types if name not in self.features}
        output = {
            "input": input_schema,
            "features": self.features
        }
        return json.dumps(output, indent=2)







# import json
# from collections import OrderedDict
#
# class JSONGenerator:
#     def __init__(self):
#         self.features = []
#         self.types = OrderedDict()
#         self.operators = {'<', '>', '==', '<=', '>=', '!=', '+', '-', '*', '/', 'AND', 'OR'}
#
#     def generate(self, traversal):
#         self.features.clear()
#         self.types.clear()
#         stack = []
#
#         for token in traversal:
#             if token == 'FeatureDefinition':
#                 _ = stack.pop()          # expression (ignored here)
#                 feature = stack.pop()
#                 if feature.startswith('df["') and feature.endswith('"]'):
#                     feature = feature[4:-2]
#                 self.features.append(feature)
#
#             elif token in self.operators:
#                 right = stack.pop()
#                 left = stack.pop()
#
#                 # Check if any side is a string literal
#                 def is_string_literal(x): return x.startswith('"') and x.endswith('"')
#
#                 # Clean token
#                 def normalize(x):
#                     if x.startswith('df["') and x.endswith('"]'):
#                         return x[4:-2]
#                     return x
#
#                 l = normalize(left)
#                 r = normalize(right)
#
#                 if l.isidentifier() and l not in self.features:
#                     self.types[l] = "string" if is_string_literal(right) else self.types.get(l, "number")
#                 if r.isidentifier() and r not in self.features:
#                     self.types[r] = "string" if is_string_literal(left) else self.types.get(r, "number")
#
#                 stack.append(f"({left} {token} {right})")
#
#             elif token not in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
#                 stack.append(token)
#
#         input_schema = {name: self.types.get(name, "number") for name in self.types if name not in self.features}
#         output = {
#             "input": input_schema,
#             "features": self.features
#         }
#         return json.dumps(output, indent=2)
