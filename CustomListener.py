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

# from gen.fdslListener import fdslListener
# from gen.fdslParser import fdslParser
# from abstract_syntax_tree.ast import AST
# from abstract_syntax_tree.make_ast_subtree import make_ast_subtree
#
#
# class CustomListener(fdslListener):
#     def __init__(self):
#         self.overridden_rules = ['program', 'feat', 'factor', 'cmpExpr', 'logicExpr', 'arithExpr', 'term']
#         self.rule_names = []
#         self.ast = AST()
#
#     def exitEveryRule(self, ctx):
#         rule_name = self.rule_names[ctx.getRuleIndex()]
#         if rule_name not in self.overridden_rules:
#             make_ast_subtree(self.ast, ctx, rule_name)
#
#     def exitProgram(self, ctx: fdslParser.ProgramContext):
#         make_ast_subtree(self.ast, ctx, "program", keep_node=True)
#
#     def exitFeat(self, ctx: fdslParser.FeatContext):
#         # Build: is_active = <expression>
#         feature_name = ctx.name().getText()
#
#         if hasattr(ctx.expr(), "ast_value"):
#             expr_node = ctx.expr().ast_value
#             assign_node = self.ast.make_node("=", [
#                 self.ast.make_node(feature_name, []),
#                 expr_node
#             ])
#         else:
#             assign_node = self.ast.make_node("=", [
#                 self.ast.make_node(feature_name, []),
#                 self.ast.make_node("UNKNOWN_EXPR", [])
#             ])
#
#         ctx.ast_value = assign_node
#         self.ast.root = assign_node
#
#     def exitLogicExpr(self, ctx: fdslParser.LogicExprContext):
#         if ctx.getChildCount() == 3:
#             left = ctx.getChild(0)
#             op = ctx.getChild(1).getText()
#             right = ctx.getChild(2)
#
#             if hasattr(left, "ast_value") and hasattr(right, "ast_value"):
#                 logic_node = self.ast.make_node(op, [left.ast_value, right.ast_value])
#                 ctx.ast_value = logic_node
#                 self.ast.root = logic_node
#         else:
#             # Single child
#             if hasattr(ctx.getChild(0), "ast_value"):
#                 ctx.ast_value = ctx.getChild(0).ast_value
#                 self.ast.root = ctx.ast_value
#
#     def exitCmpExpr(self, ctx: fdslParser.CmpExprContext):
#         if ctx.getChildCount() == 3:
#             left = ctx.getChild(0)
#             op = ctx.getChild(1).getText()
#             right = ctx.getChild(2)
#
#             if hasattr(left, "ast_value") and hasattr(right, "ast_value"):
#                 cmp_node = self.ast.make_node(op, [left.ast_value, right.ast_value])
#                 ctx.ast_value = cmp_node
#                 self.ast.root = cmp_node
#         else:
#             if hasattr(ctx.getChild(0), "ast_value"):
#                 ctx.ast_value = ctx.getChild(0).ast_value
#                 self.ast.root = ctx.ast_value
#
#     def exitArithExpr(self, ctx: fdslParser.ArithExprContext):
#         if ctx.getChildCount() == 3:
#             left = ctx.getChild(0)
#             op = ctx.getChild(1).getText()
#             right = ctx.getChild(2)
#
#             if hasattr(left, "ast_value") and hasattr(right, "ast_value"):
#                 node = self.ast.make_node(op, [left.ast_value, right.ast_value])
#                 ctx.ast_value = node
#                 self.ast.root = node
#         else:
#             if hasattr(ctx.getChild(0), "ast_value"):
#                 ctx.ast_value = ctx.getChild(0).ast_value
#                 self.ast.root = ctx.ast_value
#
#     def exitTerm(self, ctx: fdslParser.TermContext):
#         if ctx.getChildCount() == 3:
#             left = ctx.getChild(0)
#             op = ctx.getChild(1).getText()
#             right = ctx.getChild(2)
#
#             if hasattr(left, "ast_value") and hasattr(right, "ast_value"):
#                 node = self.ast.make_node(op, [left.ast_value, right.ast_value])
#                 ctx.ast_value = node
#                 self.ast.root = node
#         else:
#             if hasattr(ctx.getChild(0), "ast_value"):
#                 ctx.ast_value = ctx.getChild(0).ast_value
#                 self.ast.root = ctx.ast_value
#
#     def exitFactor(self, ctx: fdslParser.FactorContext):
#         # Handles: IDENTIFIER | NUMBER | '(' expr ')' | IDENTIFIER '(' expr ')'
#         if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '(':
#             # Function call
#             func_name = ctx.getChild(0).getText()
#             expr_ctx = ctx.getChild(2)
#
#             func_node = self.ast.make_node(func_name, [])
#             if hasattr(expr_ctx, "ast_value"):
#                 func_node.children.append(expr_ctx.ast_value)
#
#             ctx.ast_value = func_node
#             self.ast.root = func_node
#
#         elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
#             # Parentheses expression: ( expr )
#             inner_ctx = ctx.getChild(1)
#             if hasattr(inner_ctx, "ast_value"):
#                 ctx.ast_value = inner_ctx.ast_value
#                 self.ast.root = ctx.ast_value
#
#         elif ctx.getChildCount() == 1:
#             val = ctx.getChild(0).getText()
#             node = self.ast.make_node(val, [])
#             ctx.ast_value = node
#             self.ast.root = node

# class CustomListener(fdslListener):
#     def __init__(self):
#         self.overridden_rules = ['program', 'feat', 'factor']
#         self.binary_operator_list = ['logicExpr', 'cmpExpr', 'arithExpr']
#         self.compound_rules = ['program']
#         self.scoped_rules = []
#         self.rule_names = []
#         self.ast = AST()
#
#     def exitEveryRule(self, ctx):
#         rule_name = self.rule_names[ctx.getRuleIndex()]
#         if rule_name in self.scoped_rules:
#             ctx.compound = True
#         if rule_name not in self.overridden_rules:
#             if rule_name in self.binary_operator_list and ctx.getChildCount() > 1:
#                 make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
#             else:
#                 make_ast_subtree(self.ast, ctx, rule_name)
#
#     def exitProgram(self, ctx: fdslParser.ProgramContext):
#         make_ast_subtree(self.ast, ctx, "program", keep_node=True)
#
#     def exitFeat(self, ctx: fdslParser.FeatContext):
#         # structure: 'feature:' name '=' expr
#         feature_name = ctx.name().getText()
#
#         if hasattr(ctx.expr(), "ast_value"):
#             expr_node = ctx.expr().ast_value
#             assign_node = self.ast.make_node("=", [
#                 self.ast.make_node(feature_name, []),
#                 expr_node
#             ])
#         else:
#             assign_node = self.ast.make_node("=", [
#                 self.ast.make_node(feature_name, []),
#                 self.ast.make_node("UNKNOWN_EXPR", [])
#             ])
#
#         ctx.ast_value = assign_node
#         self.ast.root = assign_node
#
#     def exitFactor(self, ctx: fdslParser.FactorContext):
#         # function call pattern: IDENTIFIER '(' expr ')'
#         if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '(':
#             func_name = ctx.getChild(0).getText()
#             func_node = self.ast.make_node(func_name, [])
#
#             expr_ctx = ctx.getChild(2)
#             if hasattr(expr_ctx, "ast_value"):
#                 func_node.children.append(expr_ctx.ast_value)
#
#             ctx.ast_value = func_node
#             self.ast.root = func_node
from gen.fdslListener import fdslListener
from gen.fdslParser import fdslParser
from abstract_syntax_tree.ast import AST
from abstract_syntax_tree.make_ast_subtree import make_ast_subtree

class CustomListener(fdslListener):
    def __init__(self):
        self.overridden_rules = ['program', 'feat', 'factor']
        self.binary_operator_list = ['logicExpr', 'cmpExpr', 'arithExpr', 'term']
        self.compound_rules = ['program']
        self.scoped_rules = []
        self.rule_names = []
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name in self.scoped_rules:
            ctx.compound = True
        if rule_name not in self.overridden_rules:
            if rule_name in self.binary_operator_list and ctx.getChildCount() == 3:
                # Binary operator rule: left op right
                operator = ctx.getChild(1).getText()
                make_ast_subtree(self.ast, ctx, operator)
            else:
                # Default: use rule name
                make_ast_subtree(self.ast, ctx, rule_name)

    def exitProgram(self, ctx: fdslParser.ProgramContext):
        make_ast_subtree(self.ast, ctx, "program", keep_node=True)

    def exitFeat(self, ctx: fdslParser.FeatContext):
        # Build: is_active = <expression>
        feature_name = ctx.name().getText()

        if hasattr(ctx.expr(), "ast_value"):
            expr_node = ctx.expr().ast_value
            assign_node = self.ast.make_node("=", [
                self.ast.make_node(feature_name, []),
                expr_node
            ])
        else:
            assign_node = self.ast.make_node("=", [
                self.ast.make_node(feature_name, []),
                self.ast.make_node("UNKNOWN_EXPR", [])
            ])

        ctx.ast_value = assign_node
        self.ast.root = assign_node

    def exitFactor(self, ctx: fdslParser.FactorContext):
        # Handles: IDENTIFIER | NUMBER | '(' expr ')' | IDENTIFIER '(' expr ')'
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '(':
            # Function call
            func_name = ctx.getChild(0).getText()
            expr_ctx = ctx.getChild(2)

            func_node = self.ast.make_node(func_name, [])
            if hasattr(expr_ctx, "ast_value"):
                func_node.children.append(expr_ctx.ast_value)

            ctx.ast_value = func_node
            self.ast.root = func_node

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            # Parentheses expression: ( expr )
            inner_ctx = ctx.getChild(1)
            if hasattr(inner_ctx, "ast_value"):
                ctx.ast_value = inner_ctx.ast_value
                self.ast.root = ctx.ast_value

        elif ctx.getChildCount() == 1:
            val = ctx.getChild(0).getText()
            node = self.ast.make_node(val, [])
            ctx.ast_value = node
            self.ast.root = node