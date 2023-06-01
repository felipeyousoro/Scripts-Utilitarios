%option noyywrap
%option yylineno

%{
    #include <sintatico.tab.h>
    #include <string.h>
    extern YYSTYPE yylval;


%}


%%

[ \r\t\n]                   { /* ignore */ }

LOAD                        { return LOAD; }
FROM                        { return FROM; }

"["                         { return L_SQ_BRACKET; }
"]"                         { return R_SQ_BRACKET; }
"("                         { return L_CUR_BRACKET; }
")"                         { return R_CUR_BRACKET; }

","                         { return COMMA; }
";"                         { return SEMICOLON; }

qvd                         { return QVD; }
\"(\\.|[^"\\])*\"           { return STRING; }
([a-zA-Z0-9\.\-\/\\:])+     { return PATH; }
[_a-zA-Z][_a-zA-Z0-9]*      { return IDENTIFIER; }


.                           { printf("Caractere invalido: %c\n", yytext[0]); }

%%
