import csv
import os
from dateutil import parser as date_parser
from datetime import datetime
import pandas
import matplotlib.dates as mdates
from tabulate import tabulate

from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarListener import \
    DSL_Data_Formulas_Visualization_GrammarListener
from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarParser import \
    DSL_Data_Formulas_Visualization_GrammarParser
from Grammar.test import Test

import matplotlib.pyplot as plt  # Visualization
import numpy as np  # mathematical operations + arrays
import tkinter as tk  # context menu for Reading Files
from tkinter import filedialog  # context menu for Reading Files


class MyListener(DSL_Data_Formulas_Visualization_GrammarListener):
    def __init__(self):
        super().__init__()
        self.variables = {'np': np,
                          'v1': Test(),
                          'v2': Test(),
                          }
        # self.variables['v2'] = self.variables['v1']
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
                red_file_path = file_path
                print(f"File existent: {file_path}")
                if file_path != "":
                    head = os.path.split(file_path)[1]
                    tail = head.split(".")[1]
                else:
                    tail = None
                if tail not in ["xlsx", "csv", "txt"]:
                    print("Invalid file format!")
                    file_path = ""
                while file_path == "":
                    file_path = filedialog.askopenfilename(initialdir=os.path.split(red_file_path)[0],
                                                           title="Select a dataset file (.xlsx, .csv, .txt)")
                    if file_path != "":
                        tail = os.path.split(file_path)[1]
                        tail = tail.split(".")[1]
                        red_file_path = file_path
                    if tail not in ["xlsx", "csv", "txt"]:
                        print("Invalid file format!")
                        file_path = ""
                self.filePath = file_path
            elif os.path.exists(file_path):
                print(f"File path existent but not file: {file_path}")
                red_file_path = file_path
                root = tk.Tk()
                root.withdraw()
                root.attributes("-topmost", True)
                file_path = filedialog.askopenfilename(initialdir=red_file_path,
                                                       title="Select a dataset file (.xlsx, .csv, .txt)")
                if file_path != "":
                    tail = os.path.split(file_path)[1]
                    tail = tail.split(".")[1]
                    red_file_path = os.path.split(file_path)[0]
                    print(red_file_path)
                else:
                    tail = None
                if tail not in ["xlsx", "csv", "txt"]:
                    print("Invalid file format!")

                    file_path = ""
                while file_path == "":
                    file_path = filedialog.askopenfilename(initialdir=red_file_path,
                                                           title="Select a dataset file (.xlsx, .csv, .txt)")
                    if file_path != "":
                        tail = os.path.split(file_path)[1]
                        tail = tail.split(".")[1]
                        red_file_path = os.path.split(file_path)[0]
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
                    file_path = filedialog.askopenfilename(initialdir=desktop_path,
                                                           title="Select a dataset file (.xlsx, .csv, .txt)")
                    if file_path != "":
                        tail = os.path.split(file_path)[1]
                        tail = tail.split(".")[1]
                        desktop_path = os.path.split(file_path)[0]
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
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = filedialog.askopenfilename(initialdir=desktop_path,
                                               title="Select a dataset file (.xlsx, .csv, .txt)")
        if file_path != "":
            tail = os.path.split(file_path)[1]
            tail = tail.split(".")[1]
            desktop_path = os.path.split(file_path)[0]
        else:
            tail = None
        if tail not in ["xlsx", "csv", "txt"]:
            print("Invalid file format!")
            file_path = ""
        while file_path == "":
            file_path = filedialog.askopenfilename(initialdir=desktop_path,
                                                   title="Select a dataset file (.xlsx, .csv, .txt)")
            if file_path != "":
                tail = os.path.split(file_path)[1]
                tail = tail.split(".")[1]
                desktop_path = os.path.split(file_path)[0]
            print(tail)
            if tail not in ["xlsx", "csv", "txt"]:
                print("Invalid file format!")
                file_path = ""
        print(f"File path: {file_path}")
        self.filePath = file_path
        self.variables[self.pointer] = self.filePath

    # TODO:
    # If user closes file selector we need it to remake it so it is an error case.
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
        free_variable1 = None
        known_tokens = {'sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'sqr', '+', '-', '*', '/', '^', }
        for token in formula:
            if token[0].isalpha() and not (token in self.variables.keys() or token in known_tokens):
                if free_variable is None:
                    free_variable = token
                elif free_variable is not None and free_variable != token:
                    free_variable1 = token
                    break

        if not free_variable:
            print("Could not detect the free variable in the formula - assuming 'x' as the free variable")
            free_variable = 'x'

        print(f"Formula: {formula}")
        print(f"Formula: {formula_content}")
        if free_variable1 is None:
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
        else:
            x, y = np.meshgrid(x, x)
            z = eval(formula_content, {'np': np, free_variable: x, free_variable1: y})
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(x, y, z)
            if ctx.formulaWhole().getText() == "".join(formula):
                plt.title(f'Formula Visualization: {"".join(formula)}')
            else:
                plt.title(f'Formula Visualization: {ctx.formulaWhole().getText()} = {"".join(formula)}')
            ax.set_xlabel(free_variable)
            ax.set_ylabel(free_variable1)
            ax.set_zlabel('Formula result')
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
            'fact': 'np.math.factorial',
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
    # Inside enterVisualizeData method:
    def enterVisualizeData(self, ctx: DSL_Data_Formulas_Visualization_GrammarParser.VisualizeDataContext):
        plot_type = ctx.visualizationType().getText()
        dataset_name = ctx.ID().getText()

        if dataset_name in self.variables:
            file_path = self.variables[dataset_name]

            if file_path is not None and os.path.isfile(file_path):
                if file_path.endswith('.txt'):
                    # Handle txt file
                    with open(file_path, 'r') as file:
                        data = file.read()
                    try:
                        data = eval(data)
                        if not isinstance(data, list):
                            raise ValueError("Data is not in the expected format")
                    except Exception as e:
                        print("Error evaluating data from file:", e)
                        return

                    if plot_type == "bar":
                        # Get all years from the data sorted
                        all_dates = sorted(set(date for values, dates in [item[1:] for item in data] for date in dates))
                        all_dates_datetime = [datetime.strptime(date, '%Y-%m-%d') for date in all_dates]

                        # Get all values per year
                        values_per_year = {date: {item[0]: 0 for item in data} for date in all_dates_datetime}

                        # Fill the dictionary with actual data
                        for item in data:
                            company, values, dates = item
                            for value, date in zip(values, dates):
                                values_per_year[datetime.strptime(date, '%Y-%m-%d')][company] = value

                        # Plot each company's data
                        bar_width = 1 / (len(data) + 1)
                        num_companies = len(data)
                        index = np.arange(len(all_dates))
                        index -= int((num_companies - 1) * bar_width / 2)

                        for i, item in enumerate(data):
                            company, values, years = item
                            company_values = [values_per_year[date_parser.parse(str(year))][company] for year in
                                              all_dates_datetime]
                            plt.bar(index + i * bar_width, company_values, bar_width, label=company)

                        # Add labels and title
                        plt.xlabel('Timestamps')
                        plt.ylabel('Values')
                        plt.title(f"Bar Graph - {os.path.split(file_path)[-1]}")
                        plt.xticks(index + bar_width * (num_companies - 1) / 2,
                                   [date.strftime('%Y-%m-%d') for date in all_dates_datetime],
                                   rotation=45)
                        plt.legend()
                        plt.grid(True)
                        plt.show()

                    elif plot_type == "pie":
                        # Plot pie chart for each tuple
                        for item in data:
                            company, values, dates = item
                            specific_dates = sorted(set(date for date in dates))
                            specific_dates_datetime = [datetime.strptime(date, '%Y-%m-%d') for date in specific_dates]
                            values_per_year = {date: {item[0]: 0} for date in specific_dates_datetime}
                            for value, date in zip(values, dates):
                                values_per_year[datetime.strptime(date, '%Y-%m-%d')][company] = value
                            company_values = [values_per_year[date_parser.parse(str(year))][company] for year in
                                              specific_dates_datetime]
                            plt.pie(company_values, labels=[f"{date_pie}" for date_pie in
                                                            [date.strftime('%Y-%m-%d') for date in
                                                             specific_dates_datetime]],
                                    autopct=self._autopct_format(company_values))

                            plt.title(f"Pie Chart - {os.path.split(file_path)[-1]} for {item[0]}")
                            plt.show()
                    elif plot_type == "graph":
                        # Plot points for each tuple
                        for i, item in enumerate(data):
                            company, values, dates = item
                            min_length = min(len(values), len(dates))  # Find the minimum length
                            values = values[:min_length]  # Truncate values to match dates
                            dates = dates[:min_length]  # Truncate dates to match values

                            specific_dates_datetime = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

                            # Combine dates and values and sort by date
                            sorted_pairs = sorted(zip(specific_dates_datetime, values))
                            sorted_dates, sorted_values = zip(*sorted_pairs)

                            plt.plot(sorted_dates, sorted_values, marker='o', linestyle='-', label=f"{company}")

                        # Set x-axis labels as intervals
                        # Set the locator for the x-axis to ensure proper formatting
                        plt.gca().xaxis.set_major_locator(mdates.YearLocator())
                        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
                        plt.xticks(rotation=45)
                        plt.title(f"Graph - {os.path.split(file_path)[-1]}")
                        plt.xlabel("Timestamps")
                        plt.ylabel("Values")
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif plot_type == "console":
                        print("Data from TXT file:")
                        contents = {}
                        for item in data:
                            company, values, dates = item
                            if company not in contents:
                                if len(values) == len(dates):
                                    contents[company] = pandas.Series(values, index=dates)
                                else:
                                    min_length = min(len(values), len(dates))  # Find the minimum length
                                    values = values[:min_length]  # Truncate values to match dates
                                    dates = dates[:min_length]  # Truncate dates to match values
                                    contents[company] = pandas.Series(values, index=dates)

                            else:
                                if len(values) == len(dates):
                                    old_series = contents[company]
                                    old_series.add(pandas.Series(values, index=dates))
                                else:
                                    min_length = min(len(values), len(dates))  # Find the minimum length
                                    values = values[:min_length]  # Truncate values to match dates
                                    dates = dates[:min_length]  # Truncate dates to match values
                                    old_series = contents[company]
                                    old_series.add(pandas.Series(values, index=dates))
                        df = pandas.DataFrame(contents).transpose()
                        # df['Date'] = pandas.to_datetime(df['Date'])
                        #
                        # # Setting 'Date' column as the index
                        # df.set_index('Date', inplace=True)
                        #
                        # # Performing linear interpolation
                        # df_interpolated = df.interpolate(method='time')
                        #
                        # print(df_interpolated)
                        print(tabulate(df, headers='keys', tablefmt='psql'))
                        print("Individual pieces of Data from TXT File:")
                        for index, row in df.iterrows():
                            print(f"\nGroup: {index}")
                            df_grouped = df.loc[[index]]
                            print(tabulate(df_grouped, headers='keys', tablefmt='psql'))
                    else:
                        print("Unsupported plot type:", plot_type)
                elif file_path.endswith('.csv'):
                    # Handle csv file
                    data = []
                    with open(file_path, 'r') as file:
                        reader = csv.reader(file)
                        headers = next(reader)  # Skip the header
                        data_dict = {}

                        for row in reader:
                            if len(row) != 3:
                                # Skip rows that do not have exactly 3 values
                                continue
                            company, value, date = row
                            try:
                                value = int(value)
                            except ValueError:
                                # Skip rows where value is not an integer
                                continue
                            if company not in data_dict:
                                data_dict[company] = ([], [])
                            data_dict[company][0].append(value)
                            data_dict[company][1].append(date)

                        for company, (values, dates) in data_dict.items():
                            data.append((company, values, dates))

                    if plot_type == "bar":
                        # Get all years from the data sorted
                        all_dates = sorted(set(date for values, dates in [item[1:] for item in data] for date in dates))
                        all_dates_datetime = [datetime.strptime(date, '%Y-%m-%d') for date in all_dates]

                        # Get all values per year
                        values_per_year = {date: {item[0]: 0 for item in data} for date in all_dates_datetime}

                        # Fill the dictionary with actual data
                        for item in data:
                            company, values, dates = item
                            for value, date in zip(values, dates):
                                values_per_year[datetime.strptime(date, '%Y-%m-%d')][company] = value

                        # Plot each company's data
                        bar_width = 1 / (len(data) + 1)
                        num_companies = len(data)
                        index = np.arange(len(all_dates))
                        index -= int((num_companies - 1) * bar_width / 2)

                        for i, item in enumerate(data):
                            company, values, years = item
                            company_values = [values_per_year[date_parser.parse(str(year))][company] for year in
                                              all_dates_datetime]
                            plt.bar(index + i * bar_width, company_values, bar_width, label=company)

                        # Add labels and title
                        plt.xlabel('Timestamps')
                        plt.ylabel('Values')
                        plt.title(f"Bar Graph - {os.path.split(file_path)[-1]}")
                        plt.xticks(index + bar_width * (num_companies - 1) / 2,
                                   [date.strftime('%Y-%m-%d') for date in all_dates_datetime], rotation=45)

                        plt.legend()
                        plt.grid(True)
                        plt.show()


                    elif plot_type == "pie":
                        # Plot pie chart for each tuple
                        for item in data:
                            company, values, dates = item
                            specific_dates = sorted(set(date for date in dates))
                            specific_dates_datetime = [datetime.strptime(date, '%Y-%m-%d') for date in specific_dates]
                            values_per_year = {date: {item[0]: 0} for date in specific_dates_datetime}
                            for value, date in zip(values, dates):
                                values_per_year[datetime.strptime(date, '%Y-%m-%d')][company] = value
                            company_values = [values_per_year[date_parser.parse(str(year))][company] for year in
                                              specific_dates_datetime]
                            plt.pie(values,
                                    labels=[f"{datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')}" for
                                            date in dates], autopct=self._autopct_format(company_values))

                            plt.title(f"Pie Chart for {company}")

                            plt.show()

                    elif plot_type == "graph":
                        # Plot points for each tuple
                        for i, item in enumerate(data):
                            plt.plot(item[2], item[1], marker='o', linestyle='-', label=f"{item[0]}")

                        # Set x-axis labels as dates
                        plt.xticks(item[2],
                                   [datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d') for date in item[2]],
                                   rotation=45)
                        plt.title(f"Graph - {os.path.split(file_path)[-1]}")
                        plt.xlabel("Dates")
                        plt.ylabel("Values")
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif plot_type == "console":
                        df = pandas.read_csv(file_path)
                        print("Data from CSV file:")
                        print(tabulate(df, headers='keys', tablefmt='psql'))
                        print("Individual pieces of Data from CSV File:")
                        grouped = df.groupby(f"{df.columns[0]}")
                        for company, group in grouped:
                            print(f"\n{df.columns[0]}: {company}")
                            print(tabulate(group, headers='keys', tablefmt='psql'))
                    else:
                        print("Unsupported plot type:", plot_type)


                elif file_path.endswith(".xlsx"):
                    # Handle Excel file
                    df = pandas.read_excel(file_path)
                    data = []
                    for row in df.itertuples(index=False):
                        data.append(row)
                    if plot_type == "bar":
                        df.sort_values(by=df.columns[0], inplace=True)
                        # Plot barchart for group
                        bar_width = 1 / (len(data) + 1)
                        num_companies = len(data)
                        index = np.arange(len(df.iloc[:, 0]))
                        index -= int((num_companies - 1) * bar_width / 2)
                        for group in df.columns[1:]:  # Exclude the first column which contains timestamps
                            # Extract the timestamp and values for the current group
                            timestamps = df.iloc[:, 0]
                            values = df[group]

                            i = df.columns.get_loc(group) - 1
                            try:
                                # Plot the values for the current group against timestamps
                                plt.bar(index + i * bar_width, values, width=bar_width, label=group)
                            except Exception as e:
                                print(f"Error plotting data for {group}: {e}")

                        plt.xlabel('Timestamps')
                        plt.ylabel('Values')
                        plt.title(f"Bar Graph - {os.path.split(file_path)[-1]}")
                        plt.xticks(index + bar_width * (num_companies - 1) / 2,
                                   [date.strftime('%Y-%m-%d') for date in df.iloc[:, 0]], rotation=45)

                        plt.legend()
                        plt.grid(True)
                        plt.show()

                    elif plot_type == "pie":
                        # Plot pie chart
                        for group in df.columns[1:]:  # Exclude the first column which contains timestamps
                            # Extract the timestamp and values for the current group
                            timestamps = df.iloc[:, 0]
                            values = df[group]

                            try:
                                # Plot the values for the current group against timestamps
                                plt.pie(values,
                                        labels=[f"{datetime.strftime(timestamp, '%Y-%m-%d')}" for timestamp in
                                                timestamps],
                                        autopct=self._autopct_format(values))

                            except Exception as e:
                                print(f"Error plotting data for {group}: {e}")
                            plt.title(f"Pie Chart - {os.path.split(file_path)[-1]} for {group}")
                            plt.show()
                    elif plot_type == "graph":
                        # Plot graph for each group
                        df.sort_values(by=df.columns[0], inplace=True)
                        for group in df.columns[1:]:  # Exclude the first column which contains timestamps
                            # Extract the timestamp and values for the current group
                            timestamps = df.iloc[:, 0]

                            values = df[group]

                            try:
                                # Plot the values for the current group against timestamps
                                plt.plot(timestamps, values, marker='o', linestyle='-', label=group)

                            except Exception as e:
                                print(f"Error plotting data for {group}: {e}")

                        # Additional plotting configurations
                        plt.xticks([date.strftime('%Y-%m-%d') for date in df.iloc[:, 0]], rotation=45)
                        plt.title(f"Graph - {os.path.split(file_path)[-1]}")
                        plt.xlabel("Timestamp")
                        plt.ylabel("Values")
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif plot_type == "console":
                        print("Data from Excel file:")
                        print(tabulate(df, headers='keys', tablefmt='psql'))
                        print("Individual pieces of Data from Excel File:")
                        for group in df.columns[1:]:
                            print(f"Group: {group}")
                            print(tabulate(df[[df.columns[0], group]], headers='keys', tablefmt='psql'))

                else:
                    print("Unsupported plot type:", plot_type)
            else:
                print("Invalid file path or file does not exist:", file_path)
        else:
            print(f"Dataset '{dataset_name}' either not found or not a valid file path.")

    # Define a custom function to format the percentage and actual value
    def _autopct_format(self, values):
        def _inner_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f'{pct:.1f}%\n({val:d})'

        return _inner_autopct

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
        print(f"Params: {params[0]} {operator} {params[1]}")
        if operator == "==" and params[0] == params[1]:
            value_eval = True
        elif operator == "!=" and params[0] != params[1]:
            value_eval = True
        elif operator == "==" and params[0] != params[1]:
            value_eval = False
        elif operator == "!=" and params[0] == params[1]:
            value_eval = False
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
