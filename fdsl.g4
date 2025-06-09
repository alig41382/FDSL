grammar fdsl;

//Parse Rules
program : featureDefinitions EOF;

featureDefinitions : featureDefinition+;

featureDefinition : 'feature:' featureName '=' expression;

featureName : IDENTIFIER;

expression : logicalExpression;

// AND, OR
logicalExpression : comparisonExpression (LOGICAL_OP comparisonExpression)*;

// >, <, ==, ...
comparisonExpression : arithmeticExpression (COMPARE_OP arithmeticExpression)?;

// +, -
arithmeticExpression : term (('+' | '-') term)*;

// *, /
term : factor (('*' | '/') factor)*;

// num, var or anotha expr
factor : NUMBER | IDENTIFIER | '(' expression ')';
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