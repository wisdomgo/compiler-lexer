# 定义词法单元（Token）的数据结构
from token_type import TokenType


class Token:
    def __init__(self, type, lexeme, line, column):
        self.type = type
        self.lexeme = lexeme
        self.line = line
        self.column = column

    def __str__(self):
        return f'{repr(self.type.name)}, {repr(self.lexeme)}, line = {self.line}, column ={self.column}'
