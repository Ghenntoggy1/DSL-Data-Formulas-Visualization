from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Trees import Trees
import sys

from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarLexer import \
    DSL_Data_Formulas_Visualization_GrammarLexer
from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarParser import \
    DSL_Data_Formulas_Visualization_GrammarParser
from Grammar.test import Test

from MyListener import MyListener


def execute_code(argv):
    # Input from file
    input = FileStream(argv)

    # Lexical Analysis
    stream = perform_lexical_analysis(input)

    # Syntax Analysis
    tree, parser = perform_syntax_analysis(stream)

    # Semantic Analysis - Execution of Code
    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


# Lexical Analysis
def perform_lexical_analysis(input):
    lexer = DSL_Data_Formulas_Visualization_GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    stream.fill()
    print_tokens(stream, lexer)

    return stream


def print_tokens(stream, lexer):
    print("Tokens:")
    for token in stream.tokens:
        print(
            f"[<{lexer.symbolicNames[token.type]}> ='{token.text}']")


# Semantic Analysis
def perform_syntax_analysis(stream):
    parser = DSL_Data_Formulas_Visualization_GrammarParser(stream)
    tree = parser.program()
    print_tree(tree, parser)

    return tree, parser


def print_tree(tree, parser):
    print("Parse Tree:")
    tree_str = Trees.toStringTree(tree, None, parser)
    print(tree_str)
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found, exiting...")
        exit(1)
    print("Parsing successful, no syntax errors found.")

if __name__ == '__main__':
    input_file = FileStream(".\\Grammar\\Example_Program_Code\\Example_Exam_Lexer_Parser.txt")
    stream = perform_lexical_analysis(input_file)
    tree, parser = perform_syntax_analysis(stream)
    input("Press Enter to continue...")

    execute_code(".\\Grammar\\Example_Program_Code\\Example_Exam_Formulas.txt")
    input("Press Enter to continue...")

    execute_code(".\\Grammar\\Example_Program_Code\\Example_Exam_Data.txt")
