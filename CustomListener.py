
"""
CustomListener: Constructs a precise and deeply structured Abstract Syntax Tree (AST)
for the FDSL language used in ML feature definitions.

AST Construction Strategy:
- Each rule in the grammar that contributes structurally (like logicExpr, cmpExpr, arithExpr)
  is overridden to create explicit binary operation nodes (e.g., AND, <, +, etc.).
- The `feat` rule builds an '=' assignment with the feature name on the left and the full expression AST on the right.
- Function calls like `hour(login_time)` are recognized in the `factor` rule and built accordingly.
- Terminal tokens like operators are only used in the AST when they are wrapped in parser rules (`compareOp`, `logicalOp`)
  to ensure they are not dropped from the parse tree.
"""



from gen.fdslListener import fdslListener
from gen.fdslParser import fdslParser
from abstract_syntax_tree.ast import AST
from abstract_syntax_tree.make_ast_subtree import make_ast_subtree

class CustomListener(fdslListener):
    def __init__(self):
        self.overridden_rules = ['program', 'feat']
        self.binary_operator_list = ['logicExpr', 'cmpExpr', 'arithExpr', 'term']
        self.compound_rules = ['program']
        self.scoped_rules = []
        self.rule_names = []
        self.ast = AST()
        self.features = []  # Collect feature nodes here

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name in self.scoped_rules:
            ctx.compound = True

        if rule_name not in self.overridden_rules:
            if rule_name in self.binary_operator_list and ctx.getChildCount() == 3:
                left, op, right = ctx.getChild(0), ctx.getChild(1), ctx.getChild(2)
                if hasattr(left, "ast_value") and hasattr(right, "ast_value"):
                    op_text = op.getText()
                    node = self.ast.make_node(op_text, [left.ast_value, right.ast_value])
                    ctx.ast_value = node
                    self.ast.root = node
            else:
                make_ast_subtree(self.ast, ctx, rule_name)

    def exitFeat(self, ctx: fdslParser.FeatContext):
        """
        Build subtree:
        FeatureDefinition
        ├── feature_name
        └── expression
        """
        feature_name = ctx.getChild(1).getText()  # 0='feature:', 1=ID, 2='=', 3=expr
        feature_node = self.ast.make_node("FeatureDefinition", [
            self.ast.make_node(feature_name, [])
        ])
        if hasattr(ctx.expr(), "ast_value"):
            feature_node.children.append(ctx.expr().ast_value)
        ctx.ast_value = feature_node
        self.features.append(feature_node)

    def exitProgram(self, ctx: fdslParser.ProgramContext):
        root = self.ast.make_node("Feats", self.features)
        ctx.ast_value = root
        self.ast.root = root


