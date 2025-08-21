# JSONGenerator.py
# Reason: you’re collecting all stack operands. Only keep identifiers (real column names).
import json

class JSONGenerator:
    def __init__(self):
        self.features = []
        self.inputs = set()
        self.operators = {'<', '>', '==', '<=', '>=', '!=', '+', '-', '*', '/', 'AND', 'OR'}

    def generate(self, traversal):
        self.features.clear()
        self.inputs.clear()
        stack = []

        for token in traversal:
            if token == 'FeatureDefinition':
                _ = stack.pop()          # expression (ignored)
                feature = stack.pop()
                # strip df["..."] if it appears
                if feature.startswith('df["') and feature.endswith('"]'):
                    feature = feature[4:-2]
                self.features.append(feature)

            elif token in self.operators:
                right = stack.pop()
                left = stack.pop()
                # collect only identifiers as inputs
                for t in (left, right):
                    # strip df["..."] if needed
                    if t.startswith('df["') and t.endswith('"]'):
                        t = t[4:-2]
                    if t.isidentifier():
                        self.inputs.add(t)
                stack.append(f"({left} {token} {right})")

            elif token not in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
                stack.append(token)

        input_schema = {name: "number" for name in self.inputs if name not in self.features}
        output = {"input": input_schema, "features": self.features}
        return json.dumps(output, indent=2)


# import json
#
# class JSONGenerator:
#     def __init__(self):
#         self.features = []
#         self.inputs = set()
#
#     def generate(self, traversal):
#         self.features.clear()
#         self.inputs.clear()
#
#         stack = []
#
#         for token in traversal:
#             if token == 'FeatureDefinition':
#                 _ = stack.pop()          # Discard expression (we don’t use it here)
#                 feature = stack.pop()    # Get feature name
#                 self.features.append(feature)
#             elif token in {'<', '>', '==', '<=', '>=', '!=', '+', '-', '*', '/', 'AND', 'OR'}:
#                 right = stack.pop()
#                 left = stack.pop()
#                 self.inputs.update([left, right])
#                 stack.append(f"({left} {token} {right})")  # placeholder
#             elif token not in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
#                 if token.isnumeric():
#                     stack.append(token)
#                 else:
#                     stack.append(token)
#
#         input_schema = {name: "number" for name in self.inputs if name not in self.features}
#         output = {
#             "input": input_schema,
#             "features": self.features
#         }
#         return json.dumps(output, indent=2)
