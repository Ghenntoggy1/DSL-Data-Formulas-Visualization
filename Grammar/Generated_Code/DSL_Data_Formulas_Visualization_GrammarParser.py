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
        4,1,38,159,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,1,1,1,4,1,39,8,1,11,1,12,
        1,40,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,64,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,81,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,3,9,110,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,3,10,135,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,3,12,149,8,12,1,13,1,13,1,14,1,14,
        1,15,1,15,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,0,4,1,0,26,27,1,0,13,16,1,0,19,22,1,0,17,18,150,0,34,
        1,0,0,0,2,38,1,0,0,0,4,51,1,0,0,0,6,53,1,0,0,0,8,63,1,0,0,0,10,65,
        1,0,0,0,12,80,1,0,0,0,14,82,1,0,0,0,16,95,1,0,0,0,18,109,1,0,0,0,
        20,134,1,0,0,0,22,136,1,0,0,0,24,148,1,0,0,0,26,150,1,0,0,0,28,152,
        1,0,0,0,30,154,1,0,0,0,32,156,1,0,0,0,34,35,3,2,1,0,35,1,1,0,0,0,
        36,39,3,4,2,0,37,39,3,6,3,0,38,36,1,0,0,0,38,37,1,0,0,0,39,40,1,
        0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,3,1,0,0,0,42,43,3,8,4,0,43,
        44,5,29,0,0,44,52,1,0,0,0,45,46,3,12,6,0,46,47,5,29,0,0,47,52,1,
        0,0,0,48,49,3,18,9,0,49,50,5,29,0,0,50,52,1,0,0,0,51,42,1,0,0,0,
        51,45,1,0,0,0,51,48,1,0,0,0,52,5,1,0,0,0,53,54,7,0,0,0,54,7,1,0,
        0,0,55,56,5,1,0,0,56,57,5,24,0,0,57,58,5,34,0,0,58,64,3,10,5,0,59,
        60,5,2,0,0,60,61,5,24,0,0,61,62,5,34,0,0,62,64,3,32,16,0,63,55,1,
        0,0,0,63,59,1,0,0,0,64,9,1,0,0,0,65,66,5,8,0,0,66,67,5,32,0,0,67,
        68,5,25,0,0,68,69,5,33,0,0,69,11,1,0,0,0,70,71,5,9,0,0,71,72,5,32,
        0,0,72,73,5,25,0,0,73,74,5,33,0,0,74,81,3,14,7,0,75,76,5,10,0,0,
        76,77,5,32,0,0,77,78,5,25,0,0,78,79,5,33,0,0,79,81,3,16,8,0,80,70,
        1,0,0,0,80,75,1,0,0,0,81,13,1,0,0,0,82,83,5,3,0,0,83,84,5,34,0,0,
        84,85,5,32,0,0,85,86,5,24,0,0,86,87,5,33,0,0,87,88,5,4,0,0,88,89,
        5,34,0,0,89,90,5,32,0,0,90,91,5,24,0,0,91,92,5,37,0,0,92,93,3,28,
        14,0,93,94,5,33,0,0,94,15,1,0,0,0,95,96,3,26,13,0,96,97,5,32,0,0,
        97,98,5,24,0,0,98,99,5,33,0,0,99,100,5,4,0,0,100,101,5,34,0,0,101,
        102,5,32,0,0,102,103,5,24,0,0,103,104,5,37,0,0,104,105,3,30,15,0,
        105,106,5,33,0,0,106,17,1,0,0,0,107,110,3,20,10,0,108,110,3,22,11,
        0,109,107,1,0,0,0,109,108,1,0,0,0,110,19,1,0,0,0,111,112,5,11,0,
        0,112,113,5,32,0,0,113,114,3,32,16,0,114,115,5,33,0,0,115,116,5,
        5,0,0,116,117,5,34,0,0,117,118,5,32,0,0,118,119,5,36,0,0,119,120,
        5,31,0,0,120,121,5,36,0,0,121,122,5,33,0,0,122,135,1,0,0,0,123,124,
        5,11,0,0,124,125,5,32,0,0,125,126,5,24,0,0,126,127,5,33,0,0,127,
        128,5,5,0,0,128,129,5,34,0,0,129,130,5,32,0,0,130,131,5,36,0,0,131,
        132,5,31,0,0,132,133,5,36,0,0,133,135,5,33,0,0,134,111,1,0,0,0,134,
        123,1,0,0,0,135,21,1,0,0,0,136,137,5,12,0,0,137,138,5,32,0,0,138,
        139,3,24,12,0,139,140,5,33,0,0,140,141,5,3,0,0,141,142,5,34,0,0,
        142,143,5,32,0,0,143,144,5,24,0,0,144,145,5,33,0,0,145,23,1,0,0,
        0,146,149,5,23,0,0,147,149,3,26,13,0,148,146,1,0,0,0,148,147,1,0,
        0,0,149,25,1,0,0,0,150,151,7,1,0,0,151,27,1,0,0,0,152,153,7,2,0,
        0,153,29,1,0,0,0,154,155,7,3,0,0,155,31,1,0,0,0,156,157,5,28,0,0,
        157,33,1,0,0,0,8,38,40,51,63,80,109,134,148
    ]

class DSL_Data_Formulas_Visualization_GrammarParser ( Parser ):

    grammarFileName = "DSL_Data_Formulas_Visualization_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Data'", "'Formula'", "'dataset'", "'name'", 
                     "'range'", "'Start'", "'End'", "'ReadFrom'", "'ExportToFile'", 
                     "'ExportToImage'", "'VisualFormula'", "'VisualData'", 
                     "'graph'", "'bar'", "'pie'", "'hist'", "'png'", "'jpg'", 
                     "'csv'", "'txt'", "'json'", "'excel'", "'console'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "':'", "','", "'('", "')'", "'='", 
                     "<INVALID>", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "START", "END", "READ_FROM", 
                      "EXPORT_TO_FILE", "EXPORT_TO_IMAGE", "VISUAL_FORMULA", 
                      "VISUAL_DATA", "GRAPH", "BAR", "PIE", "HIST", "PNG", 
                      "JPG", "CSV", "TEXT", "JSON", "EXCEL", "CONSOLE", 
                      "ID", "PATH", "COMMENT_BLOCK", "COMMENT_LINE", "FORMULA", 
                      "SEMICOLON", "COLON", "COMMA", "LPAREN", "RPAREN", 
                      "ASSIGN", "OPERATORS", "DIGIT", "DOT", "WS" ]

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

    ruleNames =  [ "program", "commandsList", "command", "comment", "readCommand", 
                   "readFromFile", "exportCommand", "exportToFile", "exportToImage", 
                   "visualizeCommand", "visualizeFormula", "visualizeData", 
                   "visualizationType", "plotType", "fileType", "imageType", 
                   "formulaContent" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    START=6
    END=7
    READ_FROM=8
    EXPORT_TO_FILE=9
    EXPORT_TO_IMAGE=10
    VISUAL_FORMULA=11
    VISUAL_DATA=12
    GRAPH=13
    BAR=14
    PIE=15
    HIST=16
    PNG=17
    JPG=18
    CSV=19
    TEXT=20
    JSON=21
    EXCEL=22
    CONSOLE=23
    ID=24
    PATH=25
    COMMENT_BLOCK=26
    COMMENT_LINE=27
    FORMULA=28
    SEMICOLON=29
    COLON=30
    COMMA=31
    LPAREN=32
    RPAREN=33
    ASSIGN=34
    OPERATORS=35
    DIGIT=36
    DOT=37
    WS=38

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
            self.state = 34
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
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 9, 10, 11, 12]:
                    self.state = 36
                    self.command()
                    pass
                elif token in [26, 27]:
                    self.state = 37
                    self.comment()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 201334278) != 0)):
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.readCommand()
                self.state = 43
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
                pass
            elif token in [9, 10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.exportCommand()
                self.state = 46
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.SEMICOLON)
                pass
            elif token in [11, 12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.visualizeCommand()
                self.state = 49
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
            self.state = 53
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
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

        def ID(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN, 0)

        def readFromFile(self):
            return self.getTypedRuleContext(DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext,0)


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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.T__0)
                self.state = 56
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 57
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 58
                self.readFromFile()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.T__1)
                self.state = 60
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 61
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 62
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
            self.state = 65
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.READ_FROM)
            self.state = 66
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 67
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
            self.state = 68
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
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.EXPORT_TO_FILE)
                self.state = 71
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 72
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
                self.state = 73
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 74
                self.exportToFile()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.EXPORT_TO_IMAGE)
                self.state = 76
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 77
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.PATH)
                self.state = 78
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 79
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
            self.state = 82
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.T__2)
            self.state = 83
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 84
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 85
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 86
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 87
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.T__3)
            self.state = 88
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 89
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 90
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 91
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DOT)
            self.state = 92
            self.fileType()
            self.state = 93
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
            self.state = 95
            self.plotType()
            self.state = 96
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 97
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 98
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 99
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.T__3)
            self.state = 100
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 101
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 102
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 103
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.DOT)
            self.state = 104
            self.imageType()
            self.state = 105
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
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.visualizeFormula()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
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

        def ASSIGN(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT)
            else:
                return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT, i)

        def COMMA(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.COMMA, 0)

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
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_FORMULA)
                self.state = 112
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 113
                self.formulaContent()
                self.state = 114
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 115
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.T__4)
                self.state = 116
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 117
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 118
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT)
                self.state = 119
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.COMMA)
                self.state = 120
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT)
                self.state = 121
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_FORMULA)
                self.state = 124
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 125
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
                self.state = 126
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
                self.state = 127
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.T__4)
                self.state = 128
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
                self.state = 129
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
                self.state = 130
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT)
                self.state = 131
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.COMMA)
                self.state = 132
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.DIGIT)
                self.state = 133
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
            self.state = 136
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.VISUAL_DATA)
            self.state = 137
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 138
            self.visualizationType()
            self.state = 139
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.RPAREN)
            self.state = 140
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.T__2)
            self.state = 141
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ASSIGN)
            self.state = 142
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.LPAREN)
            self.state = 143
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.ID)
            self.state = 144
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(DSL_Data_Formulas_Visualization_GrammarParser.CONSOLE)
                pass
            elif token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
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
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
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
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
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
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
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

        def FORMULA(self):
            return self.getToken(DSL_Data_Formulas_Visualization_GrammarParser.FORMULA, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(DSL_Data_Formulas_Visualization_GrammarParser.FORMULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





