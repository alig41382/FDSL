class YAMLGenerator:
    def __init__(self):
        self.features = []

    def _mock_drift_check(self, name):
        if "active" in name:
            return "ks_test", 0.05
        elif "spender" in name:
            return "js_divergence", 0.1
        elif "support" in name:
            return "psi", 0.07
        else:
            return "kl_divergence", 0.08

    def generate(self, traversal):
        self.features.clear()
        stack = []

        for token in traversal:
            if token == 'FeatureDefinition':
                # Pop everything until only the feature name remains
                expr_items = []
                while stack:
                    item = stack.pop()
                    if stack and stack[-1] == 'FeatureDefinition':
                        break
                    expr_items.append(item)
                if stack:
                    feature_name = stack.pop()
                    self.features.append(feature_name)
            elif token in {'begin_scope_operator', 'end_scope_operator', 'program', 'feats'}:
                continue
            else:
                stack.append(token)

        yaml_lines = ["features:"]
        for name in self.features:
            check, threshold = self._mock_drift_check(name)
            yaml_lines.append(f"  - name: {name}")
            yaml_lines.append(f"    drift_check: {check}")
            yaml_lines.append(f"    threshold: {threshold}")

        return '\n'.join(yaml_lines)
