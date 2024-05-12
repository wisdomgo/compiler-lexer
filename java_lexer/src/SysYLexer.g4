lexer grammar SysYLexer;

CONST : 'CONST';
INT : 'int';
VOID : 'void';
IF : 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
CONTINUE: 'continue';
RETURN : 'return';
PLUS : '+';
MINUS : '-';
MUL : '*';
DIV : '/';
MOD : '%';
ASSIGN: '=';
EQ : '==';
NEQ : '!=';
LT : '<';
GT : '>';
LE : '<=';
GE : '>=';
NOT : '!';
AND : '&&';
OR : '||';
L_PAREN : '(';
R_PAREN : ')';
L_BRACE : '{';
R_BRACE : '}';
L_BRACKT : '[';
R_BRACKT : ']';
COMMA : ',';

SEMICOLON : ';';
IDENT : [a-zA-Z_] [a-zA-Z_0-9]* ;
INTEGER_CONST
    :   '0' [0-7]*             
    |   '0' 'x' [0-9a-fA-F]+  
    |   '0' 'X' [0-9a-fA-F]+  
    |   [1-9] [0-9]*          
    ;
WS
   : [ \r\n\t]+ ->skip
   ;
LINE_COMMENT
   : '//' .*? '\n' ->skip
   ;

MULTILINE_COMMENT
   : '/*' .*? '*/' ->skip
   ;