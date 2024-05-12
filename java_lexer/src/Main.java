import org.antlr.v4.runtime.*; // 导入ANTLR运行时所需的类，用于处理词法分析。
import java.io.IOException;     // 导入IOException，用于处理可能的输入输出异常。
import java.util.List;         // 导入List接口，用于使用列表数据结构。

public class Main {
    public static void main(String[] args) throws IOException { // 主方法，声明可能抛出的IOException。
        if (args.length < 1) { // 检查命令行参数的数量，如果少于1，则打印错误信息并返回。
            System.err.println("Input path is required"); // 在标准错误流中输出错误信息。
            return; // 退出方法。
        }
        String source = args[0]; // 获取命令行参数中的第一个参数，通常是源文件的路径。
        CharStream input = CharStreams.fromFileName(source); // 从文件名创建字符流，用于词法分析。
        SysYLexer sysYLexer = new SysYLexer(input); // 创建SysY语言的词法分析器实例，输入就是之前创建的字符流。

        MyErrorListener myErrorListener = new MyErrorListener(); // 创建自定义错误监听器。
        sysYLexer.removeErrorListeners(); // 移除默认的错误监听器。
        sysYLexer.addErrorListener(myErrorListener); // 添加自定义的错误监听器。

        List<? extends Token> myTokens = sysYLexer.getAllTokens(); // 获取所有的词法标记。

        if (myErrorListener.hasError()) { // 如果在词法分析过程中发生错误，
            myErrorListener.printLexerErrorInformation(); // 打印错误信息。
        } else {
            for (Token t : myTokens) { // 遍历所有的词法标记。
                String tokenType = SysYLexer.VOCABULARY.getSymbolicName(t.getType()); // 获取标记的类型名。
                String text = t.getText(); // 获取标记的文本。
                int line = t.getLine(); // 获取标记所在的行号。
                // 如果标记类型是整数常量，并且文本以“0x”、“0X”或“0”开头，
                if ("INTEGER_CONST".equals(tokenType) && (text.startsWith("0x") || text.startsWith("0X") || text.startsWith("0"))) {
                    long value = Long.decode(text); // 解析标记文本为长整型数值。
                    text = Long.toString(value); // 将解析后的数值转换为字符串。
                }
                System.err.printf("%s %s at Line %d.\n", tokenType, text, line); // 在标准错误流中输出标记信息。
            }
        }
    }
}
