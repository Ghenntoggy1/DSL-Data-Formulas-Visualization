from antlr4 import *
from antlr4.tree.Trees import Trees

from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarLexer import \
    DSL_Data_Formulas_Visualization_GrammarLexer
from Grammar.Generated_Code.DSL_Data_Formulas_Visualization_GrammarParser import \
    DSL_Data_Formulas_Visualization_GrammarParser


def print_parse_tree(argv):
    input = FileStream(argv)
    lexer = DSL_Data_Formulas_Visualization_GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DSL_Data_Formulas_Visualization_GrammarParser(stream)
    tree = parser.program()
    print(Trees.toStringTree(tree, None, parser))


if __name__ == '__main__':
    print_parse_tree("C:\\Users\\user\\Desktop\\Example Program 1.txt")

