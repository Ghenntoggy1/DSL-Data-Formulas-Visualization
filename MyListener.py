import os

from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarListener import DSL_Data_Formulas_Visualization_GrammarListener
from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarParser import DSL_Data_Formulas_Visualization_GrammarParser
from Grammar.test import Test

import matplotlib.pyplot as plt  # Visualization
import numpy as np  # mathematical operations + arrays
import tkinter as tk  # context menu for Reading Files
from tkinter import filedialog  # context menu for Reading Files
import math  # mathematical operations


class MyListener(DSL_Data_Formulas_Visualization_GrammarListener):
    def __init__(self):
        super().__init__()
        self.variables = {'np': np,
                          'v1': Test(),
                          'v2': Test(),
                          }
        self.pointer = None
        self.filePath = None

    def enterProgram(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ProgramContext):
        print("Enter Program")

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#program.
    def exitProgram(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ProgramContext):
        # del MyListener
        print(f"Variables: {self.variables}")
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
        if ctx.FORMULA_T() is not None:
            print("Enter Read Formula Command")
            self.variables[ctx.ID().getText()] = None
            self.pointer = ctx.ID().getText()
        if ctx.DATA() is not None:
            print("Enter Read Data Command")
            self.variables[ctx.ID().getText()] = None
            self.pointer = ctx.ID().getText()

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readCommand.
    def exitReadCommand(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ReadCommandContext):
        self.pointer = None
        print("Exit Read Command")


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readFromFile.
    def enterReadFromFile(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext):
        if ctx.PATH() is not None:
            print("Enter Read From File")
            file_path = ctx.PATH().getText().replace('"', '')
            print(file_path)
            if os.path.isfile(file_path):
                print(f"File existent: {file_path}")
                if file_path != "":
                    tail = os.path.split(file_path)[1]
                    tail = tail.split(".")[1]
                else:
                    tail = None
                if tail not in ["xlsx", "csv", "txt"]:
                    print("Invalid file format!")
                    file_path = ""
                while file_path == "":
                    file_path = filedialog.askopenfilename(initialdir=tail[0],
                                                           title="Select a dataset file (.xlsx, .csv, .txt)")
                    if file_path != "":
                        tail = os.path.split(file_path)[1]
                        tail = tail.split(".")[1]
                    print(tail)
                    if tail not in ["xlsx", "csv", "txt"]:
                        print("Invalid file format!")
                        file_path = ""
                self.filePath = file_path
            elif os.path.exists(file_path):
                print(f"File path existent but not file: {file_path}")
                root = tk.Tk()
                root.withdraw()
                root.attributes("-topmost", True)
                file_path = filedialog.askopenfilename(initialdir=file_path,
                                                       title="Select a dataset file (.xlsx, .csv, .txt)")
                if file_path != "":
                    tail = os.path.split(file_path)[1]
                    tail = tail.split(".")[1]
                else:
                    tail = None
                if tail not in ["xlsx", "csv", "txt"]:
                    print("Invalid file format!")
                    file_path = ""
                while file_path == "":
                    file_path = filedialog.askopenfilename(initialdir=file_path,
                                                           title="Select a dataset file (.xlsx, .csv, .txt)")
                    if file_path != "":
                        tail = os.path.split(file_path)[1]
                        tail = tail.split(".")[1]
                    print(tail)
                    if tail not in ["xlsx", "csv", "txt"]:
                        print("Invalid file format!")
                        file_path = ""

                print(f"File path: {file_path}")
                self.filePath = file_path

            else:
                print(f"File path doesn't exist: {file_path}")
                root = tk.Tk()
                root.withdraw()
                root.attributes("-topmost", True)

                desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

                file_path = filedialog.askopenfilename(initialdir=desktop_path,  # initialdir="" for project opening
                                                       title="Select a dataset file (.xlsx, .csv, .txt)")
                if file_path != "":
                    tail = os.path.split(file_path)[1]
                    tail = tail.split(".")[1]
                else:
                    tail = None
                if tail not in ["xlsx", "csv", "txt"]:
                    print("Invalid file format!")
                    file_path = ""
                while file_path == "":
                    file_path = filedialog.askopenfilename(initialdir=file_path,
                                                           title="Select a dataset file (.xlsx, .csv, .txt)")
                    if file_path != "":
                        tail = os.path.split(file_path)[1]
                        tail = tail.split(".")[1]
                    if tail not in ["xlsx", "csv", "txt"]:
                        print("Invalid file format!")
                        file_path = ""
                print(f"File path: {file_path}")
                self.filePath = file_path
            self.variables[self.pointer] = self.filePath
            print("FINAL FILE PATH: ", self.filePath)

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#readFromFile.
    def exitReadFromFile(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.ReadFromFileContext):
        self.filePath = None


    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#empty.
    def enterEmpty(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.EmptyContext):
        print("Enter Empty")
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        file_path = filedialog.askopenfilename(initialdir="",
                                               title="Select a dataset file (.xlsx, .csv, .txt)")
        if file_path != "":
            tail = os.path.split(file_path)[1]
            tail = tail.split(".")[1]
        else:
            tail = None
        if tail not in ["xlsx", "csv", "txt"]:
            print("Invalid file format!")
            file_path = ""
        while file_path == "":
            file_path = filedialog.askopenfilename(initialdir=file_path,
                                                   title="Select a dataset file (.xlsx, .csv, .txt)")
            if file_path != "":
                tail = os.path.split(file_path)[1]
                tail = tail.split(".")[1]
            print(tail)
            if tail not in ["xlsx", "csv", "txt"]:
                print("Invalid file format!")
                file_path = ""
        print(f"File path: {file_path}")
        self.filePath = file_path
        self.variables[self.pointer] = self.filePath

    # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#empty.
    def exitEmpty(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.EmptyContext):
        self.filePath = None
        print("Exit Empty")


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

        formula_content = None
        range_start = None
        range_end = None

        for child in ctx.children:
            if isinstance(child, DSL_Data_Formulas_Visualization_GrammarParser.FormulaWholeContext):
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
        print(f'{self.variables}')

        if formula_content is None or range_start is None or range_end is None:
            print("Error: Formula content or range values could not be parsed.")
            return
        print(f"Formula: {formula_content}")

        x = np.linspace(range_start, range_end, 200)

        formula_content = self._process_formula_content(formula_content)
        formula = formula_content.split()
        while any([token in self.variables.keys() for token in formula]):
            print(f"Formula: {formula}")
            for i in range(len(formula)):
                token = formula[i]
                if token in self.variables.keys():
                    formula[i] = self.variables[token]

            formula_content = ' '.join(formula)
            formula_content = self._process_formula_content(formula_content)
            formula = formula_content.split()

        formula_content = ' '.join(formula)
        formula_content = self._process_formula_content(formula_content, replace_with_python_mappings=True)
        formula_content = formula_content.replace('^', ' ** ')


        free_variable = None
        known_tokens = {'sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'sqr', '+', '-', '*', '/', '^', }
        for token in formula:
            if token[0].isalpha() and not (token in self.variables.keys() or token in known_tokens):
                free_variable = token
                break

        if not free_variable:
            print("Could not detect the free variable in the formula - assuming 'x' as the free variable")
            free_variable = 'x'

        print(f"Formula: {formula}")
        print(f"Formula: {formula_content}")
        y = eval(formula_content, {'np': np, free_variable: x})
        print(f"Y: {y}")
        print(type(y))
        if type(y) is not np.ndarray:
            y = [y] * 200
        plt.figure()
        plt.plot(x, y)
        if ctx.formulaWhole().getText() == "".join(formula):
            plt.title(f'Formula Visualization: {"".join(formula)}')
        else:
            plt.title(f'Formula Visualization: {ctx.formulaWhole().getText()} = {"".join(formula)}')
        plt.xlabel(free_variable)
        plt.ylabel('Formula result')
        plt.grid(True)
        plt.show()
        print(f"variables: {self.variables}")

    def _process_formula_content(self, formula_string, replace_with_python_mappings=False):
        mapping_dict_spaces = {
            '+': ' + ',
            '-': ' - ',
            '*': ' * ',
            '/': ' / ',
            '(': ' ( ',
            ')': ' ) ',
            'sin': ' sin',
            'exp': ' exp',
            'cos': ' cos',
            'tan': ' tan',
            'log': ' log',
            'sqrt': ' sqrt',
            'sqr (': ' square (',  # '(' is required so that it doesn't match sqrt
            'sqr(': ' square(',
            '^': ' ^ '
        }
        mapping_dict_python_mappings = {
            'sin': 'np.sin',
            'exp': 'np.exp',
            'cos': 'np.cos',
            'tan': 'np.tan',
            'log': 'np.log',
            'sqrt': 'np.sqrt',
            'sqr (': 'np.square (',
            'sqr(': 'np.square(',
            '^': '**'
        }
        mapping_dict = mapping_dict_python_mappings if replace_with_python_mappings else mapping_dict_spaces

        for original, new in mapping_dict.items():
            formula_string = formula_string.replace(original, new)
        return formula_string


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

    # Enter a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#formulaWhole.
    def enterFormulaWhole(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.FormulaWholeContext):
        print("Enter Formula Whole")
        text = ctx.getText()
        if self.pointer is not None:
            self.variables[self.pointer] = text
        # Exit a parse tree produced by DSL_Data_Formulas_Visualization_GrammarParser#formulaWhole.
    def exitFormulaWhole(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.FormulaWholeContext):
        print("Exit Formula Whole")

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
