import org.antlr.v4.runtime.BaseErrorListener; // 导入ANTLR的基础错误监听器类。
import org.antlr.v4.runtime.RecognitionException; // 导入识别异常类。
import org.antlr.v4.runtime.Recognizer; // 导入识别器类。

public class MyErrorListener extends BaseErrorListener { // 自定义错误监听器类继承自ANTLR的基础错误监听器。
    private boolean errorOccurred = false; // 定义一个布尔变量，记录是否发生错误。
    private StringBuilder errorMessages = new StringBuilder(); // 使用StringBuilder存储错误信息。

    @Override
    public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol,
                            int line, int charPositionInLine, String msg,
                            RecognitionException e) { // 重写syntaxError方法来定义发生语法错误时的行为。
        errorOccurred = true; // 标记已发生错误。
        errorMessages.append("Error type A at Line ") // 向errorMessages添加错误信息，指定错误类型和位置。
                   .append(line).append(": ").append(msg).append("\n");
    }

    public boolean hasError() { // 提供一个公共方法来检查是否发生过错误。
        return errorOccurred;
    }

    public void printLexerErrorInformation() { // 提供一个公共方法来打印所有收集的错误信息。
        System.err.println(errorMessages.toString()); // 在标凘错误流中输出错误信息。
    }
}
