# Generated from D:/Programming/Projects/DSL/DSL_Data_Formulas_Visualization/Grammar/DSL_Data_Formulas_Visualization_Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DSL_Data_Formulas_Visualization_GrammarParser import DSL_Data_Formulas_Visualization_GrammarParser
else:
    from DSL_Data_Formulas_Visualization_GrammarParser import DSL_Data_Formulas_Visualization_GrammarParser

# This class defines a complete generic visitor for a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser.

class DSL_Data_Formulas_Visualization_GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#program.
    def visitProgram(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#commandsList.
    def visitCommandsList(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#command.
    def visitCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#comment.
    def visitComment(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readCommand.
    def visitReadCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ReadCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readFromFile.
    def visitReadFromFile(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportCommand.
    def visitExportCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToFile.
    def visitExportToFile(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportToFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToImage.
    def visitExportToImage(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExportToImageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeCommand.
    def visitVisualizeCommand(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeFormula.
    def visitVisualizeFormula(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeData.
    def visitVisualizeData(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizeDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizationType.
    def visitVisualizationType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.VisualizationTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#plotType.
    def visitPlotType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.PlotTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#fileType.
    def visitFileType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.FileTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#imageType.
    def visitImageType(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ImageTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#formulaContent.
    def visitFormulaContent(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#ifStatement.
    def visitIfStatement(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#whileStatement.
    def visitWhileStatement(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition.
    def visitCondition(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_objects.
    def visitCondition_objects(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.Condition_objectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_numbers.
    def visitCondition_numbers(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.Condition_numbersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#expression.
    def visitExpression(self, ctx:DSL_Data_Formulas_Visualization_GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)



del DSL_Data_Formulas_Visualization_GrammarParser