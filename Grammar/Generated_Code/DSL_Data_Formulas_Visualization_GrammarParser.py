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
        4,1,51,227,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,1,1,1,1,1,1,1,4,1,55,
        8,1,11,1,12,1,56,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,68,8,2,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,80,8,4,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,97,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,3,9,126,8,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,151,8,10,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,3,12,165,8,12,1,13,1,
        13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,4,16,180,
        8,16,11,16,12,16,181,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,200,8,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,3,20,215,8,20,
        1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,0,0,24,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        0,7,1,0,28,29,1,0,38,40,1,0,14,17,1,0,20,23,1,0,18,19,1,0,43,44,
        1,0,43,48,222,0,48,1,0,0,0,2,54,1,0,0,0,4,67,1,0,0,0,6,69,1,0,0,
        0,8,79,1,0,0,0,10,81,1,0,0,0,12,96,1,0,0,0,14,98,1,0,0,0,16,111,
        1,0,0,0,18,125,1,0,0,0,20,150,1,0,0,0,22,152,1,0,0,0,24,164,1,0,
        0,0,26,166,1,0,0,0,28,168,1,0,0,0,30,170,1,0,0,0,32,179,1,0,0,0,
        34,183,1,0,0,0,36,187,1,0,0,0,38,203,1,0,0,0,40,214,1,0,0,0,42,216,
        1,0,0,0,44,220,1,0,0,0,46,224,1,0,0,0,48,49,3,2,1,0,49,1,1,0,0,0,
        50,55,3,4,2,0,51,55,3,36,18,0,52,55,3,38,19,0,53,55,3,6,3,0,54,50,
        1,0,0,0,54,51,1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,56,1,0,0,0,
        56,54,1,0,0,0,56,57,1,0,0,0,57,3,1,0,0,0,58,59,3,8,4,0,59,60,5,30,
        0,0,60,68,1,0,0,0,61,62,3,12,6,0,62,63,5,30,0,0,63,68,1,0,0,0,64,
        65,3,18,9,0,65,66,5,30,0,0,66,68,1,0,0,0,67,58,1,0,0,0,67,61,1,0,
        0,0,67,64,1,0,0,0,68,5,1,0,0,0,69,70,7,0,0,0,70,7,1,0,0,0,71,72,
        5,1,0,0,72,73,5,26,0,0,73,74,5,35,0,0,74,80,3,10,5,0,75,76,5,8,0,
        0,76,77,5,26,0,0,77,78,5,35,0,0,78,80,3,32,16,0,79,71,1,0,0,0,79,
        75,1,0,0,0,80,9,1,0,0,0,81,82,5,9,0,0,82,83,5,33,0,0,83,84,5,27,
        0,0,84,85,5,34,0,0,85,11,1,0,0,0,86,87,5,10,0,0,87,88,5,33,0,0,88,
        89,5,27,0,0,89,90,5,34,0,0,90,97,3,14,7,0,91,92,5,11,0,0,92,93,5,
        33,0,0,93,94,5,27,0,0,94,95,5,34,0,0,95,97,3,16,8,0,96,86,1,0,0,
        0,96,91,1,0,0,0,97,13,1,0,0,0,98,99,5,2,0,0,99,100,5,35,0,0,100,
        101,5,33,0,0,101,102,5,26,0,0,102,103,5,34,0,0,103,104,5,3,0,0,104,
        105,5,35,0,0,105,106,5,33,0,0,106,107,5,26,0,0,107,108,5,41,0,0,
        108,109,3,28,14,0,109,110,5,34,0,0,110,15,1,0,0,0,111,112,3,26,13,
        0,112,113,5,33,0,0,113,114,5,26,0,0,114,115,5,34,0,0,115,116,5,3,
        0,0,116,117,5,35,0,0,117,118,5,33,0,0,118,119,5,26,0,0,119,120,5,
        41,0,0,120,121,3,30,15,0,121,122,5,34,0,0,122,17,1,0,0,0,123,126,
        3,20,10,0,124,126,3,22,11,0,125,123,1,0,0,0,125,124,1,0,0,0,126,
        19,1,0,0,0,127,128,5,12,0,0,128,129,5,33,0,0,129,130,3,32,16,0,130,
        131,5,34,0,0,131,132,5,6,0,0,132,133,5,35,0,0,133,134,5,33,0,0,134,
        135,7,1,0,0,135,136,5,32,0,0,136,137,7,1,0,0,137,138,5,34,0,0,138,
        151,1,0,0,0,139,140,5,12,0,0,140,141,5,33,0,0,141,142,5,26,0,0,142,
        143,5,34,0,0,143,144,5,6,0,0,144,145,5,35,0,0,145,146,5,33,0,0,146,
        147,7,1,0,0,147,148,5,32,0,0,148,149,7,1,0,0,149,151,5,34,0,0,150,
        127,1,0,0,0,150,139,1,0,0,0,151,21,1,0,0,0,152,153,5,13,0,0,153,
        154,5,33,0,0,154,155,3,24,12,0,155,156,5,34,0,0,156,157,5,2,0,0,
        157,158,5,35,0,0,158,159,5,33,0,0,159,160,5,26,0,0,160,161,5,34,
        0,0,161,23,1,0,0,0,162,165,5,24,0,0,163,165,3,26,13,0,164,162,1,
        0,0,0,164,163,1,0,0,0,165,25,1,0,0,0,166,167,7,2,0,0,167,27,1,0,
        0,0,168,169,7,3,0,0,169,29,1,0,0,0,170,171,7,4,0,0,171,31,1,0,0,
        0,172,180,5,26,0,0,173,180,5,25,0,0,174,180,3,34,17,0,175,180,5,
        38,0,0,176,180,5,39,0,0,177,180,5,40,0,0,178,180,5,42,0,0,179,172,
        1,0,0,0,179,173,1,0,0,0,179,174,1,0,0,0,179,175,1,0,0,0,179,176,
        1,0,0,0,179,177,1,0,0,0,179,178,1,0,0,0,180,181,1,0,0,0,181,179,
        1,0,0,0,181,182,1,0,0,0,182,33,1,0,0,0,183,184,5,33,0,0,184,185,
        3,32,16,0,185,186,5,34,0,0,186,35,1,0,0,0,187,188,5,4,0,0,188,189,
        5,33,0,0,189,190,3,40,20,0,190,191,5,34,0,0,191,192,5,49,0,0,192,
        193,3,2,1,0,193,199,5,50,0,0,194,195,5,5,0,0,195,196,5,49,0,0,196,
        197,3,2,1,0,197,198,5,50,0,0,198,200,1,0,0,0,199,194,1,0,0,0,199,
        200,1,0,0,0,200,201,1,0,0,0,201,202,5,30,0,0,202,37,1,0,0,0,203,
        204,5,7,0,0,204,205,5,33,0,0,205,206,3,40,20,0,206,207,5,34,0,0,
        207,208,5,49,0,0,208,209,3,2,1,0,209,210,5,50,0,0,210,211,5,30,0,
        0,211,39,1,0,0,0,212,215,3,42,21,0,213,215,3,44,22,0,214,212,1,0,
        0,0,214,213,1,0,0,0,215,41,1,0,0,0,216,217,5,26,0,0,217,218,7,5,
        0,0,218,219,5,26,0,0,219,43,1,0,0,0,220,221,7,1,0,0,221,222,3,46,
        23,0,222,223,7,1,0,0,223,45,1,0,0,0,224,225,7,6,0,0,225,47,1,0,0,
        0,12,54,56,67,79,96,125,150,164,179,181,199,214
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
                     "<INVALID>", "<INVALID>", "';'", "':'", "','", "'('", 
                     "')'", "'='", "'['", "']'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "<INVALID>", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='", "'{'", "'}'", "'<EOF>'" ]

    symbolicNames = [ "<INVALID>", "DATA", "DATASET", "NAME", "IF", "ELSE", 
                      "RANGE", "WHILE", "FORMULA_T", "READ_FROM", "EXPORT_TO_FILE", 
                      "EXPORT_TO_IMAGE", "VISUAL_FORMULA", "VISUAL_DATA", 
                      "GRAPH", "BAR", "PIE", "HIST", "PNG", "JPG", "CSV", 
                      "TEXT", "JSON", "EXCEL", "CONSOLE", "OPERATORS", "ID", 
                      "PATH", "COMMENT_BLOCK", "COMMENT_LINE", "SEMICOLON", 
                      "COLON", "COMMA", "LPAREN", "RPAREN", "ASSIGN", "LBRACKET", 
                      "RBRACKET", "DIGIT", "INTEGER", "FLOAT", "DOT", "WS", 
                      "EQUAL", "NOT_EQUAL", "GREATER", "LESS", "GREATER_EQUAL", 
                      "LESS_EQUAL", "LBRACE", "RBRACE", "EOF_TOKEN" ]

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
    RULE_primaryExpression = 17
    RULE_ifStatement = 18
    RULE_whileStatement = 19
    RULE_condition = 20
    RULE_condition_objects = 21
    RULE_condition_numbers = 22
    RULE_expression = 23

    ruleNames =  [ "program", "commandsList", "command", "comment", "readCommand", 
                   "readFromFile", "exportCommand", "exportToFile", "exportToImage", 
                   "visualizeCommand", "visualizeFormula", "visualizeData", 
                   "visualizationType", "plotType", "fileType", "imageType", 
                   "formulaContent", "primaryExpression", "ifStatement", 
                   "whileStatement", "condition", "condition_objects", "condition_numbers", 
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
    OPERATORS=25
    ID=26
    PATH=27
    COMMENT_BLOCK=28
    COMMENT_LINE=29
    SEMICOLON=30
    COLON=31
    COMMA=32
    LPAREN=33
    RPAREN=34
    ASSIGN=35
    LBRACKET=36
    RBRACKET=37
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
            self.state = 48
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
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 8, 10, 11, 12, 13]:
                    self.state = 50
                    self.command()
                    pass
                elif token in [4]:
                    self.state = 51
                    self.ifStatement()
                    pass
                elif token in [7]:
                    self.state = 52
                    self.whileStatement()
                    pass
                elif token in [28, 29]:
                    self.state = 53
                    self.comment()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 805322130) != 0)):
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
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.readCommand()
                self.state = 59
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
                pass
            elif token in [10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.exportCommand()
                self.state = 62
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.visualizeCommand()
                self.state = 65
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
            self.state = 69
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
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
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.DATA)
                self.state = 72
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 73
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 74
                self.readFromFile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.FORMULA_T)
                self.state = 76
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 77
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 78
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
            self.state = 81
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.READ_FROM)
            self.state = 82
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 83
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
            self.state = 84
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
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.EXPORT_TO_FILE)
                self.state = 87
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 88
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
                self.state = 89
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 90
                self.exportToFile()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.EXPORT_TO_IMAGE)
                self.state = 92
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 93
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
                self.state = 94
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 95
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
            self.state = 98
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DATASET)
            self.state = 99
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 100
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 101
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 102
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 103
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.NAME)
            self.state = 104
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 105
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 106
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 107
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DOT)
            self.state = 108
            self.fileType()
            self.state = 109
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
            self.state = 111
            self.plotType()
            self.state = 112
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 113
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 114
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 115
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.NAME)
            self.state = 116
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 117
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 118
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 119
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DOT)
            self.state = 120
            self.imageType()
            self.state = 121
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
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.visualizeFormula()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_FORMULA)
                self.state = 128
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 129
                self.formulaContent()
                self.state = 130
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 131
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RANGE)
                self.state = 132
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 133
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 134
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 135
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.COMMA)
                self.state = 136
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 137
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_FORMULA)
                self.state = 140
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 141
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 142
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 143
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RANGE)
                self.state = 144
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 145
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 146
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 147
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.COMMA)
                self.state = 148
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 149
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
            self.state = 152
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_DATA)
            self.state = 153
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 154
            self.visualizationType()
            self.state = 155
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 156
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DATASET)
            self.state = 157
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 158
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 159
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 160
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
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.CONSOLE)
                pass
            elif token in [14, 15, 16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
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
            self.state = 166
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
            self.state = 168
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
            self.state = 170
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

        def primaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_Data_Formulas_Visualization_GrammarParser.PrimaryExpressionContext)
            else:
                return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.PrimaryExpressionContext,i)


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
            self.state = 179 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 179
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26]:
                    self.state = 172
                    self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                    pass
                elif token in [25]:
                    self.state = 173
                    self.match(DSL_Data_Formulas_Visualization_GrammarParser.OPERATORS)
                    pass
                elif token in [33]:
                    self.state = 174
                    self.primaryExpression()
                    pass
                elif token in [38]:
                    self.state = 175
                    self.match(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT)
                    pass
                elif token in [39]:
                    self.state = 176
                    self.match(DSL_Data_Formulas_Visualization_GrammarParser.INTEGER)
                    pass
                elif token in [40]:
                    self.state = 177
                    self.match(DSL_Data_Formulas_Visualization_GrammarParser.FLOAT)
                    pass
                elif token in [42]:
                    self.state = 178
                    self.match(DSL_Data_Formulas_Visualization_GrammarParser.WS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6330882457600) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN, 0)

        def formulaContent(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext,0)


        def RPAREN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primaryExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 184
            self.formulaContent()
            self.state = 185
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
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
        self.enterRule(localctx, 36, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.IF)
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
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 194
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ELSE)
                self.state = 195
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LBRACE)
                self.state = 196
                self.commandsList()
                self.state = 197
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RBRACE)


            self.state = 201
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
        self.enterRule(localctx, 38, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.WHILE)
            self.state = 204
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 205
            self.condition()
            self.state = 206
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 207
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LBRACE)
            self.state = 208
            self.commandsList()
            self.state = 209
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RBRACE)
            self.state = 210
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

        def condition_objects(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.Condition_objectsContext,0)


        def condition_numbers(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.Condition_numbersContext,0)


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
        self.enterRule(localctx, 40, self.RULE_condition)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.condition_objects()
                pass
            elif token in [38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.condition_numbers()
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


    class Condition_objectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, i)

        def EQUAL(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_condition_objects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_objects" ):
                listener.enterCondition_objects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_objects" ):
                listener.exitCondition_objects(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_objects" ):
                return visitor.visitCondition_objects(self)
            else:
                return visitor.visitChildren(self)




    def condition_objects(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.Condition_objectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_condition_objects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 218
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_numbersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ExpressionContext,0)


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

        def getRuleIndex(self):
            return DSL_Data_Formulas_Visualization_GrammarParser.RULE_condition_numbers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_numbers" ):
                listener.enterCondition_numbers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_numbers" ):
                listener.exitCondition_numbers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_numbers" ):
                return visitor.visitCondition_numbers(self)
            else:
                return visitor.visitChildren(self)




    def condition_numbers(self):

        localctx = DSL_Data_Formulas_Visualization_GrammarParser.Condition_numbersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_condition_numbers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 221
            self.expression()
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
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
        self.enterRule(localctx, 46, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
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





