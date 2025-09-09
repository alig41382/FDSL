# Generated from C:/Users/Ali/Desktop/pycharm/FDSL/fdsl.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,4,
        1,29,8,1,11,1,12,1,30,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,
        5,1,5,1,5,5,5,46,8,5,10,5,12,5,49,9,5,1,6,1,6,1,6,1,6,3,6,55,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,5,7,63,8,7,10,7,12,7,66,9,7,1,8,1,8,1,8,
        1,8,1,8,1,8,5,8,74,8,8,10,8,12,8,77,9,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,92,8,9,10,9,12,9,95,9,9,1,9,1,9,
        3,9,99,8,9,1,10,1,10,1,11,1,11,1,11,0,2,14,16,12,0,2,4,6,8,10,12,
        14,16,18,20,22,0,2,1,0,3,4,1,0,5,6,103,0,24,1,0,0,0,2,28,1,0,0,0,
        4,32,1,0,0,0,6,37,1,0,0,0,8,39,1,0,0,0,10,41,1,0,0,0,12,50,1,0,0,
        0,14,56,1,0,0,0,16,67,1,0,0,0,18,98,1,0,0,0,20,100,1,0,0,0,22,102,
        1,0,0,0,24,25,3,2,1,0,25,26,5,0,0,1,26,1,1,0,0,0,27,29,3,4,2,0,28,
        27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,3,1,0,0,
        0,32,33,5,1,0,0,33,34,3,6,3,0,34,35,5,2,0,0,35,36,3,8,4,0,36,5,1,
        0,0,0,37,38,5,13,0,0,38,7,1,0,0,0,39,40,3,10,5,0,40,9,1,0,0,0,41,
        47,3,12,6,0,42,43,3,22,11,0,43,44,3,12,6,0,44,46,1,0,0,0,45,42,1,
        0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,11,1,0,0,0,49,
        47,1,0,0,0,50,54,3,14,7,0,51,52,3,20,10,0,52,53,3,14,7,0,53,55,1,
        0,0,0,54,51,1,0,0,0,54,55,1,0,0,0,55,13,1,0,0,0,56,57,6,7,-1,0,57,
        58,3,16,8,0,58,64,1,0,0,0,59,60,10,2,0,0,60,61,7,0,0,0,61,63,3,16,
        8,0,62,59,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,15,
        1,0,0,0,66,64,1,0,0,0,67,68,6,8,-1,0,68,69,3,18,9,0,69,75,1,0,0,
        0,70,71,10,2,0,0,71,72,7,1,0,0,72,74,3,18,9,0,73,70,1,0,0,0,74,77,
        1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,17,1,0,0,0,77,75,1,0,0,0,
        78,99,5,12,0,0,79,99,5,14,0,0,80,99,5,15,0,0,81,99,5,13,0,0,82,83,
        5,7,0,0,83,84,3,8,4,0,84,85,5,8,0,0,85,99,1,0,0,0,86,87,5,13,0,0,
        87,88,5,7,0,0,88,93,3,8,4,0,89,90,5,9,0,0,90,92,3,8,4,0,91,89,1,
        0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,
        93,1,0,0,0,96,97,5,8,0,0,97,99,1,0,0,0,98,78,1,0,0,0,98,79,1,0,0,
        0,98,80,1,0,0,0,98,81,1,0,0,0,98,82,1,0,0,0,98,86,1,0,0,0,99,19,
        1,0,0,0,100,101,5,10,0,0,101,21,1,0,0,0,102,103,5,11,0,0,103,23,
        1,0,0,0,7,30,47,54,64,75,93,98
    ]

class fdslParser ( Parser ):

    grammarFileName = "fdsl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'feature:'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "COMPARE_OP", "LOGICAL_OP", 
                      "NUMBER", "IDENTIFIER", "STRING", "BOOL", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_feats = 1
    RULE_feat = 2
    RULE_name = 3
    RULE_expr = 4
    RULE_logicExpr = 5
    RULE_cmpExpr = 6
    RULE_arithExpr = 7
    RULE_term = 8
    RULE_factor = 9
    RULE_compareOp = 10
    RULE_logicalOp = 11

    ruleNames =  [ "program", "feats", "feat", "name", "expr", "logicExpr", 
                   "cmpExpr", "arithExpr", "term", "factor", "compareOp", 
                   "logicalOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    COMPARE_OP=10
    LOGICAL_OP=11
    NUMBER=12
    IDENTIFIER=13
    STRING=14
    BOOL=15
    WS=16
    LINE_COMMENT=17
    BLOCK_COMMENT=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def feats(self):
            return self.getTypedRuleContext(fdslParser.FeatsContext,0)


        def EOF(self):
            return self.getToken(fdslParser.EOF, 0)

        def getRuleIndex(self):
            return fdslParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = fdslParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.feats()
            self.state = 25
            self.match(fdslParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def feat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fdslParser.FeatContext)
            else:
                return self.getTypedRuleContext(fdslParser.FeatContext,i)


        def getRuleIndex(self):
            return fdslParser.RULE_feats

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeats" ):
                listener.enterFeats(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeats" ):
                listener.exitFeats(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeats" ):
                return visitor.visitFeats(self)
            else:
                return visitor.visitChildren(self)




    def feats(self):

        localctx = fdslParser.FeatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_feats)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.feat()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(fdslParser.NameContext,0)


        def expr(self):
            return self.getTypedRuleContext(fdslParser.ExprContext,0)


        def getRuleIndex(self):
            return fdslParser.RULE_feat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeat" ):
                listener.enterFeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeat" ):
                listener.exitFeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeat" ):
                return visitor.visitFeat(self)
            else:
                return visitor.visitChildren(self)




    def feat(self):

        localctx = fdslParser.FeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(fdslParser.T__0)
            self.state = 33
            self.name()
            self.state = 34
            self.match(fdslParser.T__1)
            self.state = 35
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(fdslParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return fdslParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = fdslParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(fdslParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicExpr(self):
            return self.getTypedRuleContext(fdslParser.LogicExprContext,0)


        def getRuleIndex(self):
            return fdslParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = fdslParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.logicExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmpExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fdslParser.CmpExprContext)
            else:
                return self.getTypedRuleContext(fdslParser.CmpExprContext,i)


        def logicalOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fdslParser.LogicalOpContext)
            else:
                return self.getTypedRuleContext(fdslParser.LogicalOpContext,i)


        def getRuleIndex(self):
            return fdslParser.RULE_logicExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicExpr(self):

        localctx = fdslParser.LogicExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_logicExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.cmpExpr()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 42
                self.logicalOp()
                self.state = 43
                self.cmpExpr()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fdslParser.ArithExprContext)
            else:
                return self.getTypedRuleContext(fdslParser.ArithExprContext,i)


        def compareOp(self):
            return self.getTypedRuleContext(fdslParser.CompareOpContext,0)


        def getRuleIndex(self):
            return fdslParser.RULE_cmpExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmpExpr" ):
                listener.enterCmpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmpExpr" ):
                listener.exitCmpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmpExpr" ):
                return visitor.visitCmpExpr(self)
            else:
                return visitor.visitChildren(self)




    def cmpExpr(self):

        localctx = fdslParser.CmpExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmpExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.arithExpr(0)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 51
                self.compareOp()
                self.state = 52
                self.arithExpr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(fdslParser.TermContext,0)


        def arithExpr(self):
            return self.getTypedRuleContext(fdslParser.ArithExprContext,0)


        def getRuleIndex(self):
            return fdslParser.RULE_arithExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithExpr" ):
                listener.enterArithExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithExpr" ):
                listener.exitArithExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr" ):
                return visitor.visitArithExpr(self)
            else:
                return visitor.visitChildren(self)



    def arithExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = fdslParser.ArithExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_arithExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = fdslParser.ArithExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                    self.state = 59
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 60
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 61
                    self.term(0) 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(fdslParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(fdslParser.TermContext,0)


        def getRuleIndex(self):
            return fdslParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = fdslParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = fdslParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 70
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 71
                    _la = self._input.LA(1)
                    if not(_la==5 or _la==6):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 72
                    self.factor() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(fdslParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(fdslParser.STRING, 0)

        def BOOL(self):
            return self.getToken(fdslParser.BOOL, 0)

        def IDENTIFIER(self):
            return self.getToken(fdslParser.IDENTIFIER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fdslParser.ExprContext)
            else:
                return self.getTypedRuleContext(fdslParser.ExprContext,i)


        def getRuleIndex(self):
            return fdslParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = fdslParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(fdslParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(fdslParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(fdslParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.match(fdslParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.match(fdslParser.T__6)
                self.state = 83
                self.expr()
                self.state = 84
                self.match(fdslParser.T__7)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.match(fdslParser.IDENTIFIER)
                self.state = 87
                self.match(fdslParser.T__6)
                self.state = 88
                self.expr()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 89
                    self.match(fdslParser.T__8)
                    self.state = 90
                    self.expr()
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 96
                self.match(fdslParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARE_OP(self):
            return self.getToken(fdslParser.COMPARE_OP, 0)

        def getRuleIndex(self):
            return fdslParser.RULE_compareOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareOp" ):
                listener.enterCompareOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareOp" ):
                listener.exitCompareOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOp" ):
                return visitor.visitCompareOp(self)
            else:
                return visitor.visitChildren(self)




    def compareOp(self):

        localctx = fdslParser.CompareOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_compareOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(fdslParser.COMPARE_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICAL_OP(self):
            return self.getToken(fdslParser.LOGICAL_OP, 0)

        def getRuleIndex(self):
            return fdslParser.RULE_logicalOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOp" ):
                listener.enterLogicalOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOp" ):
                listener.exitLogicalOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOp" ):
                return visitor.visitLogicalOp(self)
            else:
                return visitor.visitChildren(self)




    def logicalOp(self):

        localctx = fdslParser.LogicalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logicalOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(fdslParser.LOGICAL_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.arithExpr_sempred
        self._predicates[8] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithExpr_sempred(self, localctx:ArithExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




