from lexer import Lexer
from token_type import TokenType


def main():
    file_path = 'test.c'  # 指定文件名
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
            lexer = Lexer(source_code)
            token = lexer.next_token()
            while token.type != TokenType.EOF:
                print(token)
                token = lexer.next_token()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")


if __name__ == "__main__":
    main()
