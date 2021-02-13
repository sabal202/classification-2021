package ru.spbu.apmath.pt.lexer;

import java.io.StringReader;

public class LexerExample {

    public static void main(String[] args) throws Exception {
        //Разбиваем строку на токены (комментарии игнорируем).
        final String exampleText = "hello world 2012 /* comment */ ";

        final TestScanner scanner = new TestScanner(new StringReader(exampleText));

        TokenTypes token = null;
        while ((token = scanner.getNextToken()) != null) {
            System.out.println(token + " " + scanner.getText() + " " + scanner.getCurPosistion());
        }
    }
}
