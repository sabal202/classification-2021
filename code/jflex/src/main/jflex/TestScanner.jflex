package ru.spbu.apmath.pt.lexer;

import java.io.IOException;
import ru.spbu.apmath.pt.lexer.TokenTypes;


%%

%class TestScanner
%public
%unicode
%ignorecase
%type TokenTypes
%function getNextToken
%pack
%char

%{


public String getText() {
    return yytext();
}

public int getCurPosistion() {
    return yylength();
}

%}

ALPHA = [a-zA-Z]
DIGIT = [0-9]


COMMENT   = "/*"  ~"*/"

IDENTIFIER = {ALPHA} ({ALPHA} | {DIGIT})*

INTEGER = 0 | [1-9][0-9]*


%%

<YYINITIAL> {
    {IDENTIFIER} { return TokenTypes.TOKEN_IDENTIFIER; }
    {INTEGER} { return TokenTypes.TOKEN_INTEGER; }
    {COMMENT} {  }
    . {    }
}
