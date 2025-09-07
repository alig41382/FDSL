# Generated from C:/Users/Ali/Desktop/pycharm/FDSL/fdsl.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .fdslParser import fdslParser
else:
    from fdslParser import fdslParser

# This class defines a complete generic visitor for a parse tree produced by fdslParser.

class fdslVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fdslParser#program.
    def visitProgram(self, ctx:fdslParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#feats.
    def visitFeats(self, ctx:fdslParser.FeatsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#feat.
    def visitFeat(self, ctx:fdslParser.FeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#name.
    def visitName(self, ctx:fdslParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#expr.
    def visitExpr(self, ctx:fdslParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#logicExpr.
    def visitLogicExpr(self, ctx:fdslParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#cmpExpr.
    def visitCmpExpr(self, ctx:fdslParser.CmpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#arithExpr.
    def visitArithExpr(self, ctx:fdslParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#term.
    def visitTerm(self, ctx:fdslParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#factor.
    def visitFactor(self, ctx:fdslParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#compareOp.
    def visitCompareOp(self, ctx:fdslParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fdslParser#logicalOp.
    def visitLogicalOp(self, ctx:fdslParser.LogicalOpContext):
        return self.visitChildren(ctx)



del fdslParser