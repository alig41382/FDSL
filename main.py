from antlr4 import *
import argparse
from pathlib import Path

from CustomListener import CustomListener
from gen.fdslLexer import fdslLexer
from gen.fdslParser import fdslParser
from abstract_syntax_tree.ast_to_networkx_graph import show_ast


from PythonGenerator import PythonGenerator
from SQLGenerator import SQLGenerator
from YAMLGenerator import YAMLGenerator
from JSONGenerator import JSONGenerator


def resolve_output_paths(input_path: str, out_dir: str | None, pyth_out: str | None, sql_out: str | None, yaml_out: str | None, json_out: str | None):
    stem = Path(input_path).stem
    # Base directory for defaults
    base_dir = Path(out_dir) if out_dir else Path(f"output/{stem}")
    base_dir.mkdir(parents=True, exist_ok=True)

    pyth_out = Path(pyth_out) if pyth_out else base_dir / f"{stem}.py"
    sql_path = Path(sql_out) if sql_out else base_dir / f"{stem}.sql"
    yaml_path = Path(yaml_out) if yaml_out else base_dir / f"{stem}.yaml"
    json_path = Path(json_out) if json_out else base_dir / f"{stem}.json"
    return pyth_out ,sql_path, yaml_path, json_path

def write_in_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(content)


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

    pyth_code = PythonGenerator().generate(traversal)
    sql_code = SQLGenerator().generate(traversal)
    yaml_code = YAMLGenerator().generate(traversal)
    json_code = JSONGenerator().generate(traversal)

    # Output traversal for debug
    print("\nAST Post-Order Traversal:")
    print(traversal)

    # Generate and print code for each format
    print("\n--- Python Output (Pandas) ---")
    print(pyth_code)

    print("\n--- SQL Output ---")
    print(sql_code)

    print("\n--- YAML Output ---")
    print(yaml_code)

    print("\n--- JSON Output ---")
    print(json_code)

    pyth_path ,sql_path, yaml_path, json_path = resolve_output_paths(
        input_path=arguments.input,
        out_dir=arguments.out_dir,
        pyth_out=arguments.pyth_out,
        sql_out=arguments.sql_out,
        yaml_out=arguments.yaml_out,
        json_out=arguments.json_out,
    )

    write_in_file(pyth_path, pyth_code)
    write_in_file(sql_path, sql_code)
    write_in_file(yaml_path, yaml_code)
    write_in_file(json_path, json_code)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', help='Input source', default=r'input/test3.txt')
    argparser.add_argument('-o', '--out-dir', help='Directory to place all outputs (created if missing)')
    argparser.add_argument('-pyo', '--pyth-out', help='Output path for Python code')
    argparser.add_argument('-sqlo', '--sql-out', help='Explicit path for SQL output file (overrides --out-dir)')
    argparser.add_argument('-yamlo', '--yaml-out', help='Explicit path for YAML output file (overrides --out-dir)')
    argparser.add_argument('-jsono', '--json-out', help='Explicit path for JSON output file (overrides --out-dir)')
    args = argparser.parse_args()
    main(args)
