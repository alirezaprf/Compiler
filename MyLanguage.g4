grammar MyLanguage;

program: function_list EOF;

function_list : function_def function_list
          | function_def;

function_def : type IDENTIFIER '(' arguments? ')' block
         | type IDENTIFIER '(' ')' block;

arguments : argument (',' argument)*;

argument : type IDENTIFIER;

type : 'int'
     | 'double'
     | 'boolean'
     | 'void';

block : '{' statement_list '}';

statement_list : statement statement_list
           | empty;

statement : conditionWithElse
          | conditionNoElse;

conditionWithElse: 'if' '(' expression ')' conditionWithElse 'else' conditionWithElse
          | ';'
          | block
          | type var_list ';'
          | IDENTIFIER '=' expression ';'
          | IDENTIFIER '++' ';'
          | IDENTIFIER '--' ';'
          | 'return' ';'
          | 'return' expression ';'
          | loop_stmt
          | expression ';';

conditionNoElse: 'if' '(' expression ')' statement
          | 'if' '(' expression ')' conditionWithElse 'else' conditionNoElse;


loop_stmt : 'loop' expression statement
          | 'do-loop' statement 'until' expression
          | 'for-loop' '(' init_stmt ';' expression ';' post_stmt ')' statement ;

init_stmt : type IDENTIFIER '=' expression;

post_stmt : IDENTIFIER '=' expression
          | IDENTIFIER '++'
          | IDENTIFIER '--'
          | empty ;


var_list : var_list var
      | var;

var : IDENTIFIER
     | IDENTIFIER '=' expression;

expression : logicalOrExpression;

logicalOrExpression : logicalAndExpression
                    | logicalOrExpression '||' logicalAndExpression;

logicalAndExpression : equalityExpression
                     | logicalAndExpression '&&' equalityExpression;

equalityExpression : relationalExpression (('==' | '!=') relationalExpression)?;

relationalExpression : additiveExpression (('<' | '>' | '<=' | '>=') additiveExpression)?;

additiveExpression : multiplicativeExpression
                   | additiveExpression ('+' | '-') multiplicativeExpression;

multiplicativeExpression : unaryExpression
                         | multiplicativeExpression ('*' | '/') unaryExpression;

unaryExpression : primaryExpression
                | <assoc=right> '-' unaryExpression
                | <assoc=right> '!' unaryExpression;

primaryExpression : number
                  | IDENTIFIER
                  | 'true'
                  | 'false'
                  | STRING
                  | IDENTIFIER '(' ')'
                  | IDENTIFIER '(' parameters ')'
                  | '(' expression ')';

number : INTEGER | DOUBLE ;

parameters : expression (',' expression)*;

empty :;

IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;

INTEGER : [0-9]+;

DOUBLE : [0-9]+'.'[0-9]+;

STRING : '"' ~["]* '"';

WS : [ \t\r\n]+ -> skip;
