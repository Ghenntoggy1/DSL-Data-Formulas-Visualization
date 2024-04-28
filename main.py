from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Trees import Trees
import sys

from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarLexer import \
    DSL_Data_Formulas_Visualization_GrammarLexer
from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarParser import \
    DSL_Data_Formulas_Visualization_GrammarParser

from MyListener import MyListener


def print_parse_tree(argv):
    input = FileStream(argv)
    lexer = DSL_Data_Formulas_Visualization_GrammarLexer(input)
    print(sys.path)
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
        exit(1)

    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    # print_parse_tree(".\\Grammar\\Example_Program_Code\\Example_Program_1.txt")
    # print_parse_tree(".\\Grammar\\Example_Program_Code\\Example_Program_2.txt")
    # print_parse_tree(".\\Grammar\\Example_Program_Code\\Example_Program_3.txt")
    print_parse_tree(".\\Grammar\\Example_Program_Code\\Example_Program_4.txt")

