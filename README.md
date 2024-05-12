# compiler-lexer
## python_lexer

用python完成的C语言词法分析器，[测试文件](python_lexer/test.c)，[输出文件](python_lexer/output.txt)。

## java_lexer

使用语言识别工具ANTLR4，和Java语言来完成。使用时需要先安装`antlr4`

- 生成lexer和parser

  ```bash
  antlr4 SysYLexer.g4
  ```

  

- 编译并运行测试文件

  ```bash
  javac *.java
  java Main ../test1.sysy
  ```

  

详见[njucompilers实验](http://docs.compilers.cpl.icu/#/2024/lab1-lexer/lab1-lexer)

