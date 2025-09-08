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
                expr = stack.pop()        # e.g. (x < 30)
                left = stack.pop()        # e.g. x
                right = stack.pop()       # e.g. 30
                feature_name = stack.pop()  # finally get: 'is_active'
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
