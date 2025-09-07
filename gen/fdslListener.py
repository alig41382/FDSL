# Generated from /Users/saman/Desktop/Compiler/FDSL/fdsl.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .fdslParser import fdslParser
else:
    from fdslParser import fdslParser

# This class defines a complete listener for a parse tree produced by fdslParser.
class fdslListener(ParseTreeListener):

    # Enter a parse tree produced by fdslParser#program.
    def enterProgram(self, ctx:fdslParser.ProgramContext):
        pass

    # Exit a parse tree produced by fdslParser#program.
    def exitProgram(self, ctx:fdslParser.ProgramContext):
        pass


    # Enter a parse tree produced by fdslParser#feats.
    def enterFeats(self, ctx:fdslParser.FeatsContext):
        pass

    # Exit a parse tree produced by fdslParser#feats.
    def exitFeats(self, ctx:fdslParser.FeatsContext):
        pass


    # Enter a parse tree produced by fdslParser#feat.
    def enterFeat(self, ctx:fdslParser.FeatContext):
        pass

    # Exit a parse tree produced by fdslParser#feat.
    def exitFeat(self, ctx:fdslParser.FeatContext):
        pass


    # Enter a parse tree produced by fdslParser#name.
    def enterName(self, ctx:fdslParser.NameContext):
        pass

    # Exit a parse tree produced by fdslParser#name.
    def exitName(self, ctx:fdslParser.NameContext):
        pass


    # Enter a parse tree produced by fdslParser#expr.
    def enterExpr(self, ctx:fdslParser.ExprContext):
        pass

    # Exit a parse tree produced by fdslParser#expr.
    def exitExpr(self, ctx:fdslParser.ExprContext):
        pass


    # Enter a parse tree produced by fdslParser#logicExpr.
    def enterLogicExpr(self, ctx:fdslParser.LogicExprContext):
        pass

    # Exit a parse tree produced by fdslParser#logicExpr.
    def exitLogicExpr(self, ctx:fdslParser.LogicExprContext):
        pass


    # Enter a parse tree produced by fdslParser#cmpExpr.
    def enterCmpExpr(self, ctx:fdslParser.CmpExprContext):
        pass

    # Exit a parse tree produced by fdslParser#cmpExpr.
    def exitCmpExpr(self, ctx:fdslParser.CmpExprContext):
        pass


    # Enter a parse tree produced by fdslParser#arithExpr.
    def enterArithExpr(self, ctx:fdslParser.ArithExprContext):
        pass

    # Exit a parse tree produced by fdslParser#arithExpr.
    def exitArithExpr(self, ctx:fdslParser.ArithExprContext):
        pass


    # Enter a parse tree produced by fdslParser#term.
    def enterTerm(self, ctx:fdslParser.TermContext):
        pass

    # Exit a parse tree produced by fdslParser#term.
    def exitTerm(self, ctx:fdslParser.TermContext):
        pass


    # Enter a parse tree produced by fdslParser#factor.
    def enterFactor(self, ctx:fdslParser.FactorContext):
        pass

    # Exit a parse tree produced by fdslParser#factor.
    def exitFactor(self, ctx:fdslParser.FactorContext):
        pass


    # Enter a parse tree produced by fdslParser#compareOp.
    def enterCompareOp(self, ctx:fdslParser.CompareOpContext):
        pass

    # Exit a parse tree produced by fdslParser#compareOp.
    def exitCompareOp(self, ctx:fdslParser.CompareOpContext):
        pass


    # Enter a parse tree produced by fdslParser#logicalOp.
    def enterLogicalOp(self, ctx:fdslParser.LogicalOpContext):
        pass

    # Exit a parse tree produced by fdslParser#logicalOp.
    def exitLogicalOp(self, ctx:fdslParser.LogicalOpContext):
        pass



del fdslParser