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
    input = FileStream(argv)
    lexer = DSL_Data_Formulas_Visualization_GrammarLexer(input)

    stream = CommonTokenStream(lexer)
    stream.fill()
    print("Tokens:")
    for token in stream.tokens:
        print(
            f"[<{lexer.symbolicNames[token.type]}> ='{token.text}']")

    parser = DSL_Data_Formulas_Visualization_GrammarParser(stream)

    tree = parser.program()
    print("Parse Tree:")
    tree_str = Trees.toStringTree(tree, None, parser)
    print(tree_str)
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found, exiting...")
        exit(1)
    print("Parsing successful, no syntax errors found.")
    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    # execute_code(".\\Grammar\\Example_Program_Code\\Example_Program_1.txt")
    # execute_code(".\\Grammar\\Example_Program_Code\\Example_Program_2.txt")
    # execute_code(".\\Grammar\\Example_Program_Code\\Example_Program_3.txt")
    # execute_code(".\\Grammar\\Example_Program_Code\\Example_Program_4.txt")

    execute_code(".\\Grammar\\Example_Program_Code\\Example_1_Midterm_2.txt")
    input("Press Enter to continue...")
    execute_code(".\\Grammar\\Example_Program_Code\\Example_2_Midterm_2.txt")
    input("Press Enter to continue...")
    execute_code(".\\Grammar\\Example_Program_Code\\Example_3_Midterm_2.txt")

