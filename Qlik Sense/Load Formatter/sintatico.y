%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    void yyerror(char *s);

%}

%token LOAD
%token FROM

%token L_SQ_BRACKET
%token R_SQ_BRACKET
%token L_CUR_BRACKET
%token R_CUR_BRACKET

%token STRING
%token PATH
%token IDENTIFIER

%token COMMA
%token SEMICOLON

%token QVD

%start begin

%%

begin:
    LOAD has_one_or_more_fields from_rule
        { return 0; }
    ;

has_one_or_more_fields:
    IDENTIFIER COMMA has_many_fields
    ;

has_many_fields:
    has_one_or_more_fields
    |
    ;

from_rule:
    FROM L_SQ_BRACKET PATH R_SQ_BRACKET L_CUR_BRACKET QVD R_CUR_BRACKET
    ;


%%


void yyerror(char *s){
    printf("ERROR\n");
    exit(1);
}

int main(int argc, char** argv){
    yyparse();

    printf("OK\n");
    return 0;
}
