grammar fdsl;

//Parse Rules
program : feats EOF;

feats : feat+;

feat : 'feature:' name '=' expr;

name : IDENTIFIER;

expr : logicExpr;

// AND, OR
logicExpr : cmpExpr (LOGICAL_OP cmpExpr)*;

// >, <, ==, ...
cmpExpr  : arithExpr  (COMPARE_OP arithExpr )?;

//these two at the bottom are told to be better but im using kawan's style
// +, -
//arithExpr  : term (('+' | '-') term)*;
arithExpr : arithExpr  ('+'|'-') term | term;

// *, /
//term : factor (('*' | '/') factor)*;
term: term ('*'|'/') factor | factor;

// num, var or anotha expr
factor : NUMBER | IDENTIFIER | '(' expr  ')';
//bucket va ... ezafe konim? masalan to python bucket(age, [18, 25, 35])



// Lexer Rules
// (in this niggas AST will be removed if called directly brothers)
COMPARE_OP      : '>' | '>=' | '<' | '<=' | '==';
LOGICAL_OP      : 'AND' | 'OR';

NUMBER          : [0-9]+ ('.' [0-9]+)?;
IDENTIFIER      : [a-zA-Z_] [a-zA-Z0-9_]*;
STRING          : '"' .*? '"';

// Whitespace/newlines
WS              : [ \t\r\n]+ -> skip;