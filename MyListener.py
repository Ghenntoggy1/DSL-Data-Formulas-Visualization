import antlr4

from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarListener import DSL_Data_Formulas_Visualization_GrammarListener
from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarParser import DSL_Data_Formulas_Visualization_GrammarParser
from Grammar.test import Test

import matplotlib.pyplot as plt
import numpy as np
import math


class MyListener(DSL_Data_Formulas_Visualization_GrammarListener):
    def __init__(self):
        super().__init__()
        self.variables = {'v1': Test(),
                          'v2': Test(),
                          'formula': 'x^2'}  # Variables are stored in a dictionary

    def enterProgram(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ProgramContext):
        print("Enter Program")

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#program.
    def exitProgram(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ProgramContext):
        # del MyListener
        print("Exit Program")

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#commandsList.
    def enterCommandsList(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#commandsList.
    def exitCommandsList(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.CommandsListContext):
        pass

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#command.
    def enterCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.CommandContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#command.
    def exitCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.CommandContext):
        pass

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#comment.
    def enterComment(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.CommentContext):
        # TODO: delete if elif, leave pass -> now it s for testing purposes
        print("Enter Comment")
        if ctx.COMMENT_LINE():
            print(f"Comment Line: {ctx.COMMENT_LINE().getText()}")
        elif ctx.COMMENT_BLOCK():
            print(f"Comment Block: {ctx.COMMENT_BLOCK().getText()}")
        else:
            pass


    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#comment.
    def exitComment(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.CommentContext):
        print("Exit Comment")
        # pass

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readCommand.
    def enterReadCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ReadCommandContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readCommand.
    def exitReadCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ReadCommandContext):
        pass

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readFromFile.
    def enterReadFromFile(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readFromFile.
    def exitReadFromFile(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext):
        pass

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportCommand.
    def enterExportCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ExportCommandContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportCommand.
    def exitExportCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ExportCommandContext):
        pass

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToFile.
    def enterExportToFile(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ExportToFileContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToFile.
    def exitExportToFile(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ExportToFileContext):
        pass

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToImage.
    def enterExportToImage(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ExportToImageContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#exportToImage.
    def exitExportToImage(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ExportToImageContext):
        pass

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeCommand.
    def enterVisualizeCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizeCommandContext):
        print("Enter Visualize Command")

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeCommand.
    def exitVisualizeCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizeCommandContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeFormula.
    def enterVisualizeFormula(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizeFormulaContext):
        # basic implementation of formula visualization
        # TODO make it work for other variable names, not only x
        # TODO make it accept formula as a variable

        formula_content = None
        range_start = None
        range_end = None

        for child in ctx.children:
            if isinstance(child, DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext):
                print(f"Formula content: {child.getText()}")
                if child.getText() in self.variables.keys():
                    formula_content = self.variables[child.getText()]
                else:
                    formula_content = child.getText()
            elif child.getText() == 'range':
                # according to grammar, range numbers are at fixed positions after 'range'
                try:
                    range_start = float(ctx.children[ctx.children.index(child) + 3].getText())
                    range_end = float(ctx.children[ctx.children.index(child) + 5].getText())
                except (IndexError, ValueError) as e:
                    print(f"Error parsing range values: {e}")
                    return

        if formula_content is None or range_start is None or range_end is None:
            print("Error: Formula content or range values could not be parsed.")
            return
        print(f"Formula: {formula_content}")

        x = np.linspace(range_start, range_end, 200)
        formula_content = formula_content.replace("sin", "np.sin").replace("exp", "np.exp")
        formula_content = formula_content.replace("log", "np.log").replace("sqrt", "np.sqrt")
        formula_content = formula_content.replace("fact", "np.math.factorial")
        formula_content = formula_content.replace('sqr(', 'np.square(')  # '(' is required so that it doesn't match sqrt
        formula_content = formula_content.replace('^', '**')
        y = eval(formula_content, {"x": x, "np": np})

        plt.figure()
        plt.plot(x, y)
        plt.title('Formula Visualization')
        plt.xlabel('x')
        plt.ylabel('Formula result')
        plt.grid(True)
        plt.show()

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeFormula.
    def exitVisualizeFormula(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizeFormulaContext):
        print("Exit Visualize Formula")
        # pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeData.
    def enterVisualizeData(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizeDataContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizeData.
    def exitVisualizeData(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizeDataContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizationType.
    def enterVisualizationType(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizationTypeContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#visualizationType.
    def exitVisualizationType(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizationTypeContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#plotType.
    def enterPlotType(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.PlotTypeContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#plotType.
    def exitPlotType(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.PlotTypeContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#fileType.
    def enterFileType(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.FileTypeContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#fileType.
    def exitFileType(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.FileTypeContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#imageType.
    def enterImageType(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ImageTypeContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#imageType.
    def exitImageType(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ImageTypeContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#formulaContent.
    def enterFormulaContent(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#formulaContent.
    def exitFormulaContent(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.FormulaContentContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#primaryExpression.
    def enterPrimaryExpression(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#primaryExpression.
    def exitPrimaryExpression(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#ifStatement.
    def enterIfStatement(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.IfStatementContext):
        pass


    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#ifStatement.
    def exitIfStatement(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#whileStatement.
    def enterWhileStatement(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#whileStatement.
    def exitWhileStatement(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition.
    def enterCondition(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition.
    def exitCondition(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_objects.
    def enterCondition_objects(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.Condition_objectsContext):
        params = []
        condition = ctx
        operator = None
        # Check each method if it's relevant for condition
        for method_name in dir(condition):
            if callable(getattr(condition, method_name)) and not method_name.startswith("__"):
                method = getattr(condition, method_name)
                # Check if method returns a token
                if hasattr(method, "__self__") and hasattr(method.__self__, "getRuleIndex"):
                    # Check if the method is one of the variable tokens
                    if method_name in ["ID"] and len(method()) > 0:
                        for token in method():
                            params.append(token.getText())
                    if method_name in ["EQUAL", "NOT_EQUAL"]:
                        if method() is not None:
                            operator = method().getText()

        print(f"Params: {params}")
        print(f"Expression: {operator}")

        for i in range(len(params)):
            if params[i] in self.variables.keys():
                params[i] = self.variables[params[i]]
            else:
                # Not sure if None substitution is the best way to handle this. In essence, if the variable is not in
                # the variables dictionary, it means that it's not defined, and languages throw an error.
                # params[i] = None

                raise NameError(f"Variable {params[i]} is not defined.")
        print(f"Params: {params}")
        value_eval = params[0] == params[1]
        print(f"Evaluated: {value_eval}")
        self.variables['cond_eval'] = value_eval


    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_objects.
    def exitCondition_objects(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.Condition_objectsContext):
        print("Exit Condition Objects")
        # pass


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_numbers.
    def enterCondition_numbers(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.Condition_numbersContext):
        self.params = []
        condition = ctx
        # Check each method if it's relevant for condition
        for method_name in dir(condition):
            if callable(getattr(condition, method_name)) and not method_name.startswith("__"):
                method = getattr(condition, method_name)
                # Check if method returns a token
                if hasattr(method, "__self__") and hasattr(method.__self__, "getRuleIndex"):
                    # Check if the method is one of the variable tokens
                    if method_name in [
                        "DIGIT", "INTEGER", "FLOAT",
                    ] and len(method()) > 0:
                        for token in method():
                            self.params.append(token.getText())

        print(f"Params: {self.params}")
        print(f"Expression: {condition.expression().getText()}")


    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#condition_numbers.
    def exitCondition_numbers(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.Condition_numbersContext):
        if 'cond_eval' not in self.variables.keys():
            self.variables['cond_eval'] = None
        value_eval = eval(self.params[0] + " " + ctx.expression().getText() + " " + self.params[1])
        print(f"Evaluated: {value_eval}")
        self.variables['cond_eval'] = value_eval
        print("Exit Condition Numbers")

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#expression.
    def enterExpression(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#expression.
    def exitExpression(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ExpressionContext):
        pass
