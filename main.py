from antlr4 import *
import argparse

from CustomListener import CustomListener
from gen.fdslLexer import fdslLexer
from gen.fdslParser import fdslParser
from abstract_syntax_tree.ast_to_networkx_graph import show_ast


from PythonGenerator import PythonGenerator
from SQLGenerator import SQLGenerator
from YAMLGenerator import YAMLGenerator
from JSONGenerator import JSONGenerator


# def main(arguments):
# 	stream = FileStream(arguments.input, encoding='utf8')
# 	lexer = fdslLexer(stream)
#
# 	token_stream = CommonTokenStream(lexer)
#
# 	parser = fdslParser(token_stream)
# 	parse_tree = parser.program()
#
# 	ast_builder_listener = CustomListener()
# 	ast_builder_listener.rule_names = parser.ruleNames
# 	walker = ParseTreeWalker()
# 	walker.walk(t=parse_tree, listener=ast_builder_listener)
# 	ast = ast_builder_listener.ast
# 	show_ast(ast.root)
# 	traversal = ast.traverse_ast(ast.root)
# 	print(traversal) #to print the abstract_syntax_tree traverse output
#
# 	# code_gen = CodeGenerator()
# 	# final_code =code_gen.generate(traversal)
# 	# print(final_code)
#
# 	# to write the output to a given filefor usage
# 	# with open('evm_generator_output.txt','w') as evm_gen_out:
# 	# 	evm_gen_out.write(final_code)
#
#
# # need a change in the output place
# if __name__ == '__main__':
# 	argparser = argparse.ArgumentParser()
# 	argparser.add_argument('-i', '--input', help='Input source', default=r'input/test1.txt')
# 	argparser.add_argument('-o', '--output', help='Output path', default=r'output/test.evm-bytecode')
# 	args = argparser.parse_args()
# 	main(args)


def main(arguments):
    stream = FileStream(arguments.input, encoding='utf8')
    lexer = fdslLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = fdslParser(token_stream)

    parse_tree = parser.program()

    ast_builder_listener = CustomListener()
    ast_builder_listener.rule_names = parser.ruleNames
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_builder_listener)

    ast = ast_builder_listener.ast
    show_ast(ast.root)
    traversal = ast.traverse_ast(ast.root)

    # Output traversal for debug
    print("\nAST Post-Order Traversal:")
    print(traversal)

    # Generate and print code for each format
    print("\n--- Python Output (Pandas) ---")
    print(PythonGenerator().generate(traversal))

    print("\n--- SQL Output ---")
    print(SQLGenerator().generate(traversal))

    print("\n--- YAML Output ---")
    print(YAMLGenerator().generate(traversal))

    print("\n--- JSON Output ---")
    print(JSONGenerator().generate(traversal))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', help='Input source', default=r'input/test2.txt')
    args = argparser.parse_args()
    main(args)
