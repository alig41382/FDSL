# YAML features show 30 and 75 instead of feature names
# Reason: grabbing i-2 before FeatureDefinition is brittle. Use a stack like the other generators.
class YAMLGenerator:
    def __init__(self):
        self.features = []
        self.default_check = "ks_test"
        self.default_threshold = 0.05

    def _unformat(self, token: str) -> str:
        if token.startswith('df["') and token.endswith('"]'):
            return token[4:-2]
        return token

    def generate(self, traversal):
        self.features.clear()
        stack = []

        for token in traversal:
            if token == 'FeatureDefinition':
                _ = stack.pop()            # discard expression
                feature = self._unformat(stack.pop())
                self.features.append(feature)
            elif token in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
                continue
            else:
                stack.append(token)

        yaml_lines = ["features:"]
        for name in self.features:
            yaml_lines.append(f"  - name: {name}")
            yaml_lines.append(f"    drift_check: {self.default_check}")
            yaml_lines.append(f"    threshold: {self.default_threshold}")
        return '\n'.join(yaml_lines)


# class YAMLGenerator:
#     def __init__(self):
#         self.features = []
#         self.default_check = "ks_test"
#         self.default_threshold = 0.05
#
#     def generate(self, traversal):
#         self.features.clear()
#         for i in range(len(traversal)):
#             if traversal[i] == 'FeatureDefinition' and i >= 2:
#                 feature_name = traversal[i - 2]  # two tokens before FeatureDefinition is the feature name
#                 self.features.append(feature_name)
#
#         yaml_lines = ["features:"]
#         for name in self.features:
#             yaml_lines.append(f"  - name: {name}")
#             yaml_lines.append(f"    drift_check: {self.default_check}")
#             yaml_lines.append(f"    threshold: {self.default_threshold}")
#
#         return '\n'.join(yaml_lines)
