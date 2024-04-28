# Generated from D:/Programming/Projects/DSL/DSL_Data_Formulas_Visualization/Grammar/DSL_Data_Formulas_Visualization_Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DSL_Data_Formulas_Visualization_GrammarParser import DSL_Data_Formulas_Visualization_GrammarParser
else:
    from DSL_Data_Formulas_Visualization_GrammarParser import DSL_Data_Formulas_Visualization_GrammarParser

# This class defines a complete listener for a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser.
class DSL_Data_Formulas_Visualization_GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#program.
    def enterProgram(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#program.
    def exitProgram(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#commandsList.
    def enterCommandsList(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#commandsList.
    def exitCommandsList(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#command.
    def enterCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommandContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#command.
    def exitCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommandContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#comment.
    def enterComment(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommentContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#comment.
    def exitComment(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommentContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readCommand.
    def enterReadCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ReadCommandContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readCommand.
    def exitReadCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ReadCommandContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readFromFile.
    def enterReadFromFile(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readFromFile.
    def exitReadFromFile(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportCommand.
    def enterExportCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportCommandContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportCommand.
    def exitExportCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportCommandContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToFile.
    def enterExportToFile(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportToFileContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToFile.
    def exitExportToFile(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportToFileContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToImage.
    def enterExportToImage(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportToImageContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToImage.
    def exitExportToImage(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportToImageContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeCommand.
    def enterVisualizeCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeCommandContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeCommand.
    def exitVisualizeCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeCommandContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeFormula.
    def enterVisualizeFormula(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeFormulaContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeFormula.
    def exitVisualizeFormula(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeFormulaContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeData.
    def enterVisualizeData(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeDataContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeData.
    def exitVisualizeData(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeDataContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizationType.
    def enterVisualizationType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizationTypeContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizationType.
    def exitVisualizationType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizationTypeContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#plotType.
    def enterPlotType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.PlotTypeContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#plotType.
    def exitPlotType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.PlotTypeContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#fileType.
    def enterFileType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.FileTypeContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#fileType.
    def exitFileType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.FileTypeContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#imageType.
    def enterImageType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ImageTypeContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#imageType.
    def exitImageType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ImageTypeContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#formulaContent.
    def enterFormulaContent(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#formulaContent.
    def exitFormulaContent(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#ifStatement.
    def enterIfStatement(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#ifStatement.
    def exitIfStatement(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition.
    def enterCondition(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition.
    def exitCondition(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_objects.
    def enterCondition_objects(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.Condition_objectsContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_objects.
    def exitCondition_objects(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.Condition_objectsContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_numbers.
    def enterCondition_numbers(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.Condition_numbersContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_numbers.
    def exitCondition_numbers(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.Condition_numbersContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#expression.
    def enterExpression(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#expression.
    def exitExpression(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExpressionContext):
        pass



del DSL_Data_Formulas_Visualization_GrammarParser