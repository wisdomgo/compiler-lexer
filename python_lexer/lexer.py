from mytoken import Token
from token_type import TokenType


class Lexer:
    def __init__(self, source):
        self.source = source
        self.current = 0
        self.line = 1
        self.column = 1
        self.keywords = {
            'CONST': TokenType.CONST,
            "int": TokenType.INT,
            "void": TokenType.VOID,
            "return": TokenType.RETURN,
            "if": TokenType.IF,
            "else": TokenType.ELSE,
            "while": TokenType.WHILE,
            "break": TokenType.BREAK,
            "continue": TokenType.CONTINUE,

        }

    def next_token(self):
        while self.current < len(self.source):
            char = self.source[self.current]
            if char.isdigit():
                return self.number()
            elif char.isalpha() or char == '_':
                return self.identifier()
            elif char.isspace():
                self.skip_whitespace()
                continue
            elif char == '/':
                if self.source[self.current + 1] in {
                    '/',
                    '*'
                }:
                    self.skip_comment()
                else:
                    return self.read_operator()
            elif char in {
                '+',
                '-',
                '*',
                '%',
                '(',
                ')',
                ';',
                '{',
                '}',
                '[',
                ']',
            }:
                return self.read_operator()
            elif char == '#':
                return self.read_identifier()
            else:
                self.current += 1
        return Token(TokenType.EOF, '', self.line, self.column)  # 源代码末尾

    def identifier(self):
        start = self.current
        while self.current < len(self.source) and (
                self.source[self.current].isalnum() or self.source[self.current] == '_'):
            self.current += 1
        text = self.source[start:self.current]
        token_type = self.keywords.get(text, TokenType.IDENTIFIER)
        return Token(token_type, text, self.line, self.column)

    def number(self):
        start = self.current
        while self.current < len(self.source) and self.source[self.current].isdigit():
            self.current += 1
        number = self.source[start:self.current]
        return Token(TokenType.NUMBER, number, self.line, self.column)

    def skip_whitespace(self):
        while self.current < len(self.source) and self.source[self.current].isspace():
            if self.source[self.current] == '\n':
                self.line += 1
                self.column = 0
            self.current += 1
            self.column += 1

    def skip_comment(self):
        if self.source[self.current:self.current + 2] == '//':
            while self.current < len(self.source) and self.source[self.current] != '\n':
                self.current += 1
            return self.next_token()
        elif self.source[self.current:self.current + 2] == '/*':
            self.current += 2
            while self.current < len(self.source) - 1 and self.source[self.current:self.current + 2] != '*/':
                if self.source[self.current] == '\n':
                    self.line += 1
                    self.column = 0
                self.current += 1
            self.current += 2
            return self.next_token()
        else:
            self.current += 1

    def read_operator(self):
        start = self.current
        if self.source[self.current: self.current + 2] in {
            '==',
            '!=',
            '<=',
            '>=',
            '&&',
            '||',
        }:
            self.current += 2
        else:
            self.current += 1
        op = self.source[start:self.current]
        op_type = TokenType[op
        .replace('&&', 'AND')
        .replace('||', 'OR')
        .replace('==', 'EQ')
        .replace('!=', 'NEQ')
        .replace('<=', 'LE')
        .replace('>=', 'GE')
        .replace('!', 'NOT')
        .replace('+', 'PLUS')
        .replace('-', 'MINUS')
        .replace('*', 'MUL')
        .replace('/', 'DIV')
        .replace('%', 'MOD')
        .replace('=', 'ASSIGN')
        .replace('<', 'LT')
        .replace('>', 'GT')
        .replace('(', 'L_PAREN')
        .replace(')', 'R_PAREN')
        .replace('{', 'L_BRACE')
        .replace('}', 'R_BRACE')
        .replace('[', 'L_BRACKET')
        .replace(']', 'R_BRACKET')
        .replace(',', 'COMMA')
        .replace(';', 'SEMICOLON')]
        return Token(op_type, op, self.line, self.column)

    def read_identifier(self):
        start = self.current
        while self.current < len(self.source) and self.source[self.current] != '\n':
            self.current += 1
        directive_line = self.source[start:self.current]
        print(directive_line)
        if '<' in directive_line:
            self.read_filename(directive_line)
        return Token(TokenType.IDENTIFIER, directive_line.strip(), self.line, self.column)

    def read_filename(self, directive_line):
        # print(2)
        # print(directive_line)
        directive, filename = directive_line.split('<')
        filename = filename.split('>')[0]
        return Token(TokenType.STRING, filename, self.line, self.column)
