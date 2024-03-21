# Generated from D:/Programming/Projects/DSL/DSL_Data_Formulas_Visualization/Grammar/DSL_Data_Formulas_Visualization_Grammar.g4 by ANTLR 4.13.1
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
        4,1,51,203,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,1,1,1,1,1,1,1,4,1,49,8,1,11,1,12,1,50,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,62,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,91,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        9,1,9,3,9,120,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,3,10,145,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,3,12,159,8,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,4,
        16,168,8,16,11,16,12,16,169,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,3,17,184,8,17,1,17,1,17,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,0,
        0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,
        8,1,0,27,28,1,0,38,40,1,0,14,17,1,0,20,23,1,0,18,19,4,0,25,25,32,
        33,37,40,42,42,2,0,25,25,38,40,1,0,43,48,194,0,42,1,0,0,0,2,48,1,
        0,0,0,4,61,1,0,0,0,6,63,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,90,
        1,0,0,0,14,92,1,0,0,0,16,105,1,0,0,0,18,119,1,0,0,0,20,144,1,0,0,
        0,22,146,1,0,0,0,24,158,1,0,0,0,26,160,1,0,0,0,28,162,1,0,0,0,30,
        164,1,0,0,0,32,167,1,0,0,0,34,171,1,0,0,0,36,187,1,0,0,0,38,196,
        1,0,0,0,40,200,1,0,0,0,42,43,3,2,1,0,43,1,1,0,0,0,44,49,3,4,2,0,
        45,49,3,34,17,0,46,49,3,36,18,0,47,49,3,6,3,0,48,44,1,0,0,0,48,45,
        1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,
        50,51,1,0,0,0,51,3,1,0,0,0,52,53,3,8,4,0,53,54,5,29,0,0,54,62,1,
        0,0,0,55,56,3,12,6,0,56,57,5,29,0,0,57,62,1,0,0,0,58,59,3,18,9,0,
        59,60,5,29,0,0,60,62,1,0,0,0,61,52,1,0,0,0,61,55,1,0,0,0,61,58,1,
        0,0,0,62,5,1,0,0,0,63,64,7,0,0,0,64,7,1,0,0,0,65,66,5,1,0,0,66,67,
        5,25,0,0,67,68,5,34,0,0,68,74,3,10,5,0,69,70,5,8,0,0,70,71,5,25,
        0,0,71,72,5,34,0,0,72,74,3,32,16,0,73,65,1,0,0,0,73,69,1,0,0,0,74,
        9,1,0,0,0,75,76,5,9,0,0,76,77,5,32,0,0,77,78,5,26,0,0,78,79,5,33,
        0,0,79,11,1,0,0,0,80,81,5,10,0,0,81,82,5,32,0,0,82,83,5,26,0,0,83,
        84,5,33,0,0,84,91,3,14,7,0,85,86,5,11,0,0,86,87,5,32,0,0,87,88,5,
        26,0,0,88,89,5,33,0,0,89,91,3,16,8,0,90,80,1,0,0,0,90,85,1,0,0,0,
        91,13,1,0,0,0,92,93,5,2,0,0,93,94,5,34,0,0,94,95,5,32,0,0,95,96,
        5,25,0,0,96,97,5,33,0,0,97,98,5,3,0,0,98,99,5,34,0,0,99,100,5,32,
        0,0,100,101,5,25,0,0,101,102,5,41,0,0,102,103,3,28,14,0,103,104,
        5,33,0,0,104,15,1,0,0,0,105,106,3,26,13,0,106,107,5,32,0,0,107,108,
        5,25,0,0,108,109,5,33,0,0,109,110,5,3,0,0,110,111,5,34,0,0,111,112,
        5,32,0,0,112,113,5,25,0,0,113,114,5,41,0,0,114,115,3,30,15,0,115,
        116,5,33,0,0,116,17,1,0,0,0,117,120,3,20,10,0,118,120,3,22,11,0,
        119,117,1,0,0,0,119,118,1,0,0,0,120,19,1,0,0,0,121,122,5,12,0,0,
        122,123,5,32,0,0,123,124,3,32,16,0,124,125,5,33,0,0,125,126,5,6,
        0,0,126,127,5,34,0,0,127,128,5,32,0,0,128,129,7,1,0,0,129,130,5,
        31,0,0,130,131,7,1,0,0,131,132,5,33,0,0,132,145,1,0,0,0,133,134,
        5,12,0,0,134,135,5,32,0,0,135,136,5,25,0,0,136,137,5,33,0,0,137,
        138,5,6,0,0,138,139,5,34,0,0,139,140,5,32,0,0,140,141,7,1,0,0,141,
        142,5,31,0,0,142,143,7,1,0,0,143,145,5,33,0,0,144,121,1,0,0,0,144,
        133,1,0,0,0,145,21,1,0,0,0,146,147,5,13,0,0,147,148,5,32,0,0,148,
        149,3,24,12,0,149,150,5,33,0,0,150,151,5,2,0,0,151,152,5,34,0,0,
        152,153,5,32,0,0,153,154,5,25,0,0,154,155,5,33,0,0,155,23,1,0,0,
        0,156,159,5,24,0,0,157,159,3,26,13,0,158,156,1,0,0,0,158,157,1,0,
        0,0,159,25,1,0,0,0,160,161,7,2,0,0,161,27,1,0,0,0,162,163,7,3,0,
        0,163,29,1,0,0,0,164,165,7,4,0,0,165,31,1,0,0,0,166,168,7,5,0,0,
        167,166,1,0,0,0,168,169,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,
        170,33,1,0,0,0,171,172,5,4,0,0,172,173,5,32,0,0,173,174,3,38,19,
        0,174,175,5,33,0,0,175,176,5,49,0,0,176,177,3,2,1,0,177,183,5,50,
        0,0,178,179,5,5,0,0,179,180,5,49,0,0,180,181,3,2,1,0,181,182,5,50,
        0,0,182,184,1,0,0,0,183,178,1,0,0,0,183,184,1,0,0,0,184,185,1,0,
        0,0,185,186,5,29,0,0,186,35,1,0,0,0,187,188,5,7,0,0,188,189,5,32,
        0,0,189,190,3,38,19,0,190,191,5,33,0,0,191,192,5,49,0,0,192,193,
        3,2,1,0,193,194,5,50,0,0,194,195,5,29,0,0,195,37,1,0,0,0,196,197,
        5,25,0,0,197,198,3,40,20,0,198,199,7,6,0,0,199,39,1,0,0,0,200,201,
        7,7,0,0,201,41,1,0,0,0,10,48,50,61,73,90,119,144,158,169,183
    ]

class DSL_Data_Formulas_Visualization_GrammarParser ( Parser ):

    grammarFileName = "DSL_Data_Formulas_Visualization_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Data'", "'dataset'", "'name'", "'if'", 
                     "'else'", "'range'", "'while'", "'Formula'", "'ReadFrom'", 
                     "'ExportToFile'", "'ExportToImage'", "'VisualFormula'", 
                     "'VisualData'", "'graph'", "'bar'", "'pie'", "'hist'", 
                     "'png'", "'jpg'", "'csv'", "'txt'", "'json'", "'excel'", 
                     "'console'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "':'", "','", "'('", "')'", "'='", 
                     "'['", "']'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "<INVALID>", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='", "'{'", "'}'", "'<EOF>'" ]

    symbolicNames = [ "<INVALID>", "DATA", "DATASET", "NAME", "IF", "ELSE", 
                      "RANGE", "WHILE", "FORMULA_T", "READ_FROM", "EXPORT_TO_FILE", 
                      "EXPORT_TO_IMAGE", "VISUAL_FORMULA", "VISUAL_DATA", 
                      "GRAPH", "BAR", "PIE", "HIST", "PNG", "JPG", "CSV", 
                      "TEXT", "JSON", "EXCEL", "CONSOLE", "ID", "PATH", 
                      "COMMENT_BLOCK", "COMMENT_LINE", "SEMICOLON", "COLON", 
                      "COMMA", "LPAREN", "RPAREN", "ASSIGN", "LBRACKET", 
                      "RBRACKET", "OPERATORS", "DIGIT", "INTEGER", "FLOAT", 
                      "DOT", "WS", "EQUAL", "NOT_EQUAL", "GREATER", "LESS", 
                      "GREATER_EQUAL", "LESS_EQUAL", "LBRACE", "RBRACE", 
                      "EOF_TOKEN" ]

    RULE_program = 0
    RULE_commandsList = 1
    RULE_command = 2
    RULE_comment = 3
    RULE_readCommand = 4
    RULE_readFromFile = 5
    RULE_exportCommand = 6
    RULE_exportToFile = 7
    RULE_exportToImage = 8
    RULE_visualizeCommand = 9
    RULE_visualizeFormula = 10
    RULE_visualizeData = 11
    RULE_visualizationType = 12
    RULE_plotType = 13
    RULE_fileType = 14
    RULE_imageType = 15
    RULE_formulaContent = 16
    RULE_ifStatement = 17
    RULE_whileStatement = 18
    RULE_condition = 19
    RULE_expression = 20

    ruleNames =  [ "program", "commandsList", "command", "comment", "readCommand", 
                   "readFromFile", "exportCommand", "exportToFile", "exportToImage", 
                   "visualizeCommand", "visualizeFormula", "visualizeData", 
                   "visualizationType", "plotType", "fileType", "imageType", 
                   "formulaContent", "ifStatement", "whileStatement", "condition", 
                   "expression" ]

    EOF = Token.EOF
    DATA=1
    DATASET=2
    NAME=3
    IF=4
    ELSE=5
    RANGE=6
    WHILE=7
    FORMULA_T=8
    READ_FROM=9
    EXPORT_TO_FILE=10
    EXPORT_TO_IMAGE=11
    VISUAL_FORMULA=12
    VISUAL_DATA=13
    GRAPH=14
    BAR=15
    PIE=16
    HIST=17
    PNG=18
    JPG=19
    CSV=20
    TEXT=21
    JSON=22
    EXCEL=23
    CONSOLE=24
    ID=25
    PATH=26
    COMMENT_BLOCK=27
    COMMENT_LINE=28
    SEMICOLON=29
    COLON=30
    COMMA=31
    LPAREN=32
    RPAREN=33
    ASSIGN=34
    LBRACKET=35
    RBRACKET=36
    OPERATORS=37
    DIGIT=38
    INTEGER=39
    FLOAT=40
    DOT=41
    WS=42
    EQUAL=43
    NOT_EQUAL=44
    GREATER=45
    LESS=46
    GREATER_EQUAL=47
    LESS_EQUAL=48
    LBRACE=49
    RBRACE=50
    EOF_TOKEN=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commandsList(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext,0)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_program

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

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.commandsList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandsListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_Data_Formulas_Visualization_GrammarParser.CommandContext)
            else:
                return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.CommandContext,i)


        def ifStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_Data_Formulas_Visualization_GrammarParser.IfStatementContext)
            else:
                return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.IfStatementContext,i)


        def whileStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_Data_Formulas_Visualization_GrammarParser.WhileStatementContext)
            else:
                return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.WhileStatementContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_Data_Formulas_Visualization_GrammarParser.CommentContext)
            else:
                return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.CommentContext,i)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_commandsList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandsList" ):
                listener.enterCommandsList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandsList" ):
                listener.exitCommandsList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandsList" ):
                return visitor.visitCommandsList(self)
            else:
                return visitor.visitChildren(self)




    def commandsList(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commandsList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 8, 10, 11, 12, 13]:
                    self.state = 44
                    self.command()
                    pass
                elif token in [4]:
                    self.state = 45
                    self.ifStatement()
                    pass
                elif token in [7]:
                    self.state = 46
                    self.whileStatement()
                    pass
                elif token in [27, 28]:
                    self.state = 47
                    self.comment()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 402668946) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readCommand(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ReadCommandContext,0)


        def SEMICOLON(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON, 0)

        def exportCommand(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ExportCommandContext,0)


        def visualizeCommand(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.VisualizeCommandContext,0)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.readCommand()
                self.state = 53
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
                pass
            elif token in [10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.exportCommand()
                self.state = 56
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.visualizeCommand()
                self.state = 59
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT_BLOCK(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.COMMENT_BLOCK, 0)

        def COMMENT_LINE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.COMMENT_LINE, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DATA, 0)

        def ID(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN, 0)

        def readFromFile(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext,0)


        def FORMULA_T(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.FORMULA_T, 0)

        def formulaContent(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext,0)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_readCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadCommand" ):
                listener.enterReadCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadCommand" ):
                listener.exitReadCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadCommand" ):
                return visitor.visitReadCommand(self)
            else:
                return visitor.visitChildren(self)




    def readCommand(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ReadCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_readCommand)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.DATA)
                self.state = 66
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 67
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 68
                self.readFromFile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.FORMULA_T)
                self.state = 70
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 71
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 72
                self.formulaContent()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadFromFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ_FROM(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.READ_FROM, 0)

        def LPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, 0)

        def PATH(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.PATH, 0)

        def RPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_readFromFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadFromFile" ):
                listener.enterReadFromFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadFromFile" ):
                listener.exitReadFromFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadFromFile" ):
                return visitor.visitReadFromFile(self)
            else:
                return visitor.visitChildren(self)




    def readFromFile(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_readFromFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.READ_FROM)
            self.state = 76
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 77
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
            self.state = 78
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExportCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORT_TO_FILE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.EXPORT_TO_FILE, 0)

        def LPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, 0)

        def PATH(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.PATH, 0)

        def RPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, 0)

        def exportToFile(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ExportToFileContext,0)


        def EXPORT_TO_IMAGE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.EXPORT_TO_IMAGE, 0)

        def exportToImage(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ExportToImageContext,0)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_exportCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExportCommand" ):
                listener.enterExportCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExportCommand" ):
                listener.exitExportCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExportCommand" ):
                return visitor.visitExportCommand(self)
            else:
                return visitor.visitChildren(self)




    def exportCommand(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ExportCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exportCommand)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.EXPORT_TO_FILE)
                self.state = 81
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 82
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
                self.state = 83
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 84
                self.exportToFile()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.EXPORT_TO_IMAGE)
                self.state = 86
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 87
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
                self.state = 88
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 89
                self.exportToImage()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExportToFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATASET(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DATASET, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, i)

        def NAME(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.NAME, 0)

        def DOT(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DOT, 0)

        def fileType(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.FileTypeContext,0)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_exportToFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExportToFile" ):
                listener.enterExportToFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExportToFile" ):
                listener.exitExportToFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExportToFile" ):
                return visitor.visitExportToFile(self)
            else:
                return visitor.visitChildren(self)




    def exportToFile(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ExportToFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exportToFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DATASET)
            self.state = 93
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 94
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 95
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 96
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 97
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.NAME)
            self.state = 98
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 99
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 100
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 101
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DOT)
            self.state = 102
            self.fileType()
            self.state = 103
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExportToImageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plotType(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.PlotTypeContext,0)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, i)

        def NAME(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.NAME, 0)

        def ASSIGN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN, 0)

        def DOT(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DOT, 0)

        def imageType(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ImageTypeContext,0)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_exportToImage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExportToImage" ):
                listener.enterExportToImage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExportToImage" ):
                listener.exitExportToImage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExportToImage" ):
                return visitor.visitExportToImage(self)
            else:
                return visitor.visitChildren(self)




    def exportToImage(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ExportToImageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exportToImage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.plotType()
            self.state = 106
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 107
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 108
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 109
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.NAME)
            self.state = 110
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 111
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 112
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 113
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DOT)
            self.state = 114
            self.imageType()
            self.state = 115
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def visualizeFormula(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.VisualizeFormulaContext,0)


        def visualizeData(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.VisualizeDataContext,0)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_visualizeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualizeCommand" ):
                listener.enterVisualizeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualizeCommand" ):
                listener.exitVisualizeCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualizeCommand" ):
                return visitor.visitVisualizeCommand(self)
            else:
                return visitor.visitChildren(self)




    def visualizeCommand(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.VisualizeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_visualizeCommand)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.visualizeFormula()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.visualizeData()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizeFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VISUAL_FORMULA(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_FORMULA, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, i)

        def formulaContent(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, i)

        def RANGE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RANGE, 0)

        def ASSIGN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN, 0)

        def COMMA(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.COMMA, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.INTEGER)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.INTEGER, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.FLOAT)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.FLOAT, i)

        def ID(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_visualizeFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualizeFormula" ):
                listener.enterVisualizeFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualizeFormula" ):
                listener.exitVisualizeFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualizeFormula" ):
                return visitor.visitVisualizeFormula(self)
            else:
                return visitor.visitChildren(self)




    def visualizeFormula(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.VisualizeFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_visualizeFormula)
        self._la = 0 # Token type
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_FORMULA)
                self.state = 122
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 123
                self.formulaContent()
                self.state = 124
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 125
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RANGE)
                self.state = 126
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 127
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 128
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 129
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.COMMA)
                self.state = 130
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 131
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_FORMULA)
                self.state = 134
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 135
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 136
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 137
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RANGE)
                self.state = 138
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 139
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 140
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 141
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.COMMA)
                self.state = 142
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizeDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VISUAL_DATA(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_DATA, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, i)

        def visualizationType(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.VisualizationTypeContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, i)

        def DATASET(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DATASET, 0)

        def ASSIGN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN, 0)

        def ID(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_visualizeData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualizeData" ):
                listener.enterVisualizeData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualizeData" ):
                listener.exitVisualizeData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualizeData" ):
                return visitor.visitVisualizeData(self)
            else:
                return visitor.visitChildren(self)




    def visualizeData(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.VisualizeDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_visualizeData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_DATA)
            self.state = 147
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 148
            self.visualizationType()
            self.state = 149
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 150
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DATASET)
            self.state = 151
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 152
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 153
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 154
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizationTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSOLE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.CONSOLE, 0)

        def plotType(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.PlotTypeContext,0)


        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_visualizationType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualizationType" ):
                listener.enterVisualizationType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualizationType" ):
                listener.exitVisualizationType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualizationType" ):
                return visitor.visitVisualizationType(self)
            else:
                return visitor.visitChildren(self)




    def visualizationType(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.VisualizationTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_visualizationType)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.CONSOLE)
                pass
            elif token in [14, 15, 16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.plotType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAPH(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.GRAPH, 0)

        def BAR(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.BAR, 0)

        def PIE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.PIE, 0)

        def HIST(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.HIST, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_plotType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlotType" ):
                listener.enterPlotType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlotType" ):
                listener.exitPlotType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlotType" ):
                return visitor.visitPlotType(self)
            else:
                return visitor.visitChildren(self)




    def plotType(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.PlotTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_plotType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FileTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CSV(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.CSV, 0)

        def TEXT(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.TEXT, 0)

        def JSON(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.JSON, 0)

        def EXCEL(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.EXCEL, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_fileType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileType" ):
                listener.enterFileType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileType" ):
                listener.exitFileType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileType" ):
                return visitor.visitFileType(self)
            else:
                return visitor.visitChildren(self)




    def fileType(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.FileTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fileType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImageTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PNG(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.PNG, 0)

        def JPG(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.JPG, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_imageType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImageType" ):
                listener.enterImageType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImageType" ):
                listener.exitImageType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImageType" ):
                return visitor.visitImageType(self)
            else:
                return visitor.visitChildren(self)




    def imageType(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ImageTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_imageType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, i)

        def OPERATORS(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.OPERATORS)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.OPERATORS, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.INTEGER)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.INTEGER, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.FLOAT)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.FLOAT, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.WS)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.WS, i)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_formulaContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormulaContent" ):
                listener.enterFormulaContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormulaContent" ):
                listener.exitFormulaContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormulaContent" ):
                return visitor.visitFormulaContent(self)
            else:
                return visitor.visitChildren(self)




    def formulaContent(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_formulaContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 166
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6472549269504) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 169 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.IF, 0)

        def LPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.LBRACE)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LBRACE, i)

        def commandsList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext)
            else:
                return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.RBRACE)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RBRACE, i)

        def SEMICOLON(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON, 0)

        def ELSE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ELSE, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.IF)
            self.state = 172
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 173
            self.condition()
            self.state = 174
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 175
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LBRACE)
            self.state = 176
            self.commandsList()
            self.state = 177
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RBRACE)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 178
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ELSE)
                self.state = 179
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LBRACE)
                self.state = 180
                self.commandsList()
                self.state = 181
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RBRACE)


            self.state = 185
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LBRACE, 0)

        def commandsList(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext,0)


        def RBRACE(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.WHILE)
            self.state = 188
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 189
            self.condition()
            self.state = 190
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 191
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LBRACE)
            self.state = 192
            self.commandsList()
            self.state = 193
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RBRACE)
            self.state = 194
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, i)

        def expression(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ExpressionContext,0)


        def DIGIT(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT, 0)

        def INTEGER(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 197
            self.expression()
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924178903040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.NOT_EQUAL, 0)

        def GREATER(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.GREATER, 0)

        def LESS(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LESS, 0)

        def GREATER_EQUAL(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LESS_EQUAL, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 554153860399104) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





