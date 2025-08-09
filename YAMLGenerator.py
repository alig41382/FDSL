class YAMLGenerator:
    def __init__(self):
        self.features = []
        self.default_check = "ks_test"
        self.default_threshold = 0.05

    def generate(self, traversal):
        self.features.clear()
        for i in range(len(traversal)):
            if traversal[i] == 'FeatureDefinition' and i >= 2:
                feature_name = traversal[i - 2]  # two tokens before FeatureDefinition is the feature name
                self.features.append(feature_name)

        yaml_lines = ["features:"]
        for name in self.features:
            yaml_lines.append(f"  - name: {name}")
            yaml_lines.append(f"    drift_check: {self.default_check}")
            yaml_lines.append(f"    threshold: {self.default_threshold}")

        return '\n'.join(yaml_lines)
