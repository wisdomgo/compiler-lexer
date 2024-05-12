# 枚举所有的Token类型，比如关键字、标识符等
from enum import Enum


class TokenType(Enum):
    # 特殊类型
    EOF = 'EOF'
    WS = 'WS'
    LINE_COMMENT = 'LINE_COMMENT'
    MULTILINE_COMMENT = 'MULTILINE_COMMENT'

    # 基本单位
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'
    STRING = 'STRING'

    # 关键字
    CONST = 'CONST'
    INT = 'int'
    VOID = 'void'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    BREAK = 'break'
    CONTINUE = 'continue'
    RETURN = 'return'

    # 运算符
    PLUS = '+'
    MINUS = '-'
    MUL = '*'
    DIV = '/'
    MOD = '%'
    ASSIGN = '='
    EQ = '=='
    NEQ = '!='
    LT = '<'
    GT = '>'
    LE = '<='
    GE = '>='
    NOT = '!'
    AND = '&&'
    OR = '||'

    L_PAREN = '('
    R_PAREN = ')'
    L_BRACE = '{'
    R_BRACE = '}'
    L_BRACKET = '['
    R_BRACKET = ']'
    COMMA = ','
    SEMICOLON = ';'
