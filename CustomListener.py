from gen.fdslListener import fdslListener
from gen.fdslParser import fdslParser
from abstract_syntax_tree.ast import AST
from abstract_syntax_tree.make_ast_subtree import make_ast_subtree

class CustomListener(fdslListener):
	def __init__(self):
		#overriden rules for the changes to a rule to be manual using exit(ruleName)Rule function
		self.overridden_rules = ['program']
		#I Don't know if we have to make the rules more specific for this one
		self.binary_operator_list = ['term','arithExpr','logicExpr','cmpExpr']
		#these rules get begin and end
		self.compound_rules = []
		self.scoped_rules = []
		self.rule_names = []
		self.ast = AST()


	def exitEveryRule(self, ctx):
		rule_name = self.rule_names[ctx.getRuleIndex()]
		if rule_name in self.scoped_rules:
			ctx.compound = True
		if rule_name not in self.overridden_rules:
			if rule_name in self.binary_operator_list and ctx.getChildCount() > 1:
				make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
			else:
				make_ast_subtree(self.ast, ctx, rule_name)

	def exitProgram(self, ctx:fdslParser.ProgramContext):
		make_ast_subtree(self.ast, ctx, "program", keep_node=True)

