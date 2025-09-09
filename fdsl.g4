grammar fdsl;

//Parse Rules
program : feats EOF;

feats : feat+;

feat : 'feature:' name '=' expr;

name : IDENTIFIER;

expr : logicExpr;

// AND, OR
logicExpr : cmpExpr (logicalOp cmpExpr)*; //fek konam inja bayad OR ro mizashtam bad AND ro bekhater Order

// >, <, ==, ...
cmpExpr  : arithExpr  (compareOp  arithExpr )?;

//these two at the bottom are told to be better but im using kawan's style
arithExpr : arithExpr  ('+'|'-') term | term;

term: term ('*'|'/') factor | factor;

factor : NUMBER | STRING | BOOL | IDENTIFIER | '(' expr  ')';
//bucket va ... ezafe konim? masalan to python bucket(age, [18, 25, 35])
compareOp : COMPARE_OP;

logicalOp : LOGICAL_OP;

// Lexer Rules
// (in this niggas AST will be removed if called directly brothers)
COMPARE_OP      : '>' | '>=' | '<' | '<=' | '==' | '!=';
LOGICAL_OP      : 'AND' | 'OR';

NUMBER          : [0-9]+ ('.' [0-9]+)?;
IDENTIFIER      : [a-zA-Z_] [a-zA-Z0-9_]*;
STRING          : '"' .*? '"';
BOOL : 'true' | 'false';

WS              : [ \t\r\n]+ -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
