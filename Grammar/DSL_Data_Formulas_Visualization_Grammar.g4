grammar DSL_Data_Formulas_Visualization_Grammar;

// Parser rules
program : commandsList;

commandsList : (command | ifStatement | whileStatement | comment)+;

command : readCommand SEMICOLON
        | exportCommand SEMICOLON
        | visualizeCommand SEMICOLON;

comment : COMMENT_BLOCK
        | COMMENT_LINE;

// TODO: Add dialog for data selection file -> empty parenthesis
readCommand : DATA ID ASSIGN readFromFile
            | FORMULA_T ID ASSIGN formulaWhole;

readFromFile : READ_FROM LPAREN (PATH | empty) RPAREN;

empty : ;

exportCommand : EXPORT_TO_FILE LPAREN PATH RPAREN exportToFile
              | EXPORT_TO_IMAGE LPAREN PATH RPAREN exportToImage;

exportToFile : DATASET ASSIGN LPAREN ID RPAREN NAME ASSIGN LPAREN ID DOT fileType RPAREN;

exportToImage : plotType LPAREN ID RPAREN NAME ASSIGN LPAREN ID DOT imageType RPAREN;

visualizeCommand : visualizeFormula
                 | visualizeData;

visualizeFormula : VISUAL_FORMULA LPAREN formulaWhole RPAREN RANGE ASSIGN LPAREN ( DIGIT | INTEGER | FLOAT ) COMMA ( DIGIT | INTEGER | FLOAT ) RPAREN;

visualizeData : VISUAL_DATA LPAREN visualizationType RPAREN DATASET ASSIGN LPAREN ID RPAREN;

visualizationType : CONSOLE | plotType;

plotType : GRAPH | BAR | PIE | HIST;

fileType : CSV | TEXT | JSON | EXCEL;

imageType : PNG | JPG;

formulaWhole : formulaContent;

formulaContent : (ID | OPERATORS | primaryExpression | DIGIT | INTEGER | FLOAT | WS)+;

primaryExpression : LPAREN  formulaContent  RPAREN;

ifStatement : IF LPAREN condition RPAREN LBRACE commandsList RBRACE
             ( ELSE LBRACE commandsList RBRACE )? SEMICOLON ;

whileStatement : WHILE LPAREN condition RPAREN LBRACE commandsList RBRACE SEMICOLON;

condition :  condition_objects | condition_numbers;

condition_objects : ID (EQUAL | NOT_EQUAL) ID;

condition_numbers : (DIGIT | INTEGER | FLOAT) expression (DIGIT | INTEGER | FLOAT);

expression : (EQUAL | NOT_EQUAL | GREATER | LESS | GREATER_EQUAL | LESS_EQUAL) ;

// Lexer rules
DATA : 'Data';
DATASET: 'dataset';
NAME : 'name';
IF : 'if';
ELSE : 'else';
RANGE : 'range';
WHILE : 'while';
FORMULA_T : 'Formula';
READ_FROM : 'ReadFrom';
EXPORT_TO_FILE : 'ExportToFile';
EXPORT_TO_IMAGE : 'ExportToImage';
VISUAL_FORMULA : 'VisualFormula';
VISUAL_DATA : 'VisualData';
GRAPH : 'graph';
BAR : 'bar';
PIE : 'pie';
HIST : 'hist';
PNG : 'png';
JPG : 'jpg';
CSV : 'csv';
TEXT : 'txt';
JSON : 'json';
EXCEL : 'excel';
CONSOLE : 'console';
OPERATORS : '*' | '^' | 'log' | 'sqr' | 'sqrt' | 'fact' | '+' | '-';
ID : [a-zA-Z_/]+[a-zA-Z0-9_/]*;
PATH : '"' [a-zA-Z0-9_:.\\ ]+ '"';
COMMENT_BLOCK : '/*' .*? '*/';
COMMENT_LINE : '#' ~[\r\n]*;
SEMICOLON : ';';
COLON : ':';
COMMA : ',';
LPAREN : '(';
RPAREN : ')';
ASSIGN : '=';
LBRACKET : '[';
RBRACKET : ']';
DIGIT : [0-9];
INTEGER : '-'? DIGIT+;
FLOAT : INTEGER DOT DIGIT+;
DOT : '.';
WS : [ \t\r\n]+ -> skip; // Skip whitespace
SPACE: [ \t\r\n];
EQUAL : '==';
NOT_EQUAL : '!=';
GREATER : '>';
LESS : '<';
GREATER_EQUAL : '>=';
LESS_EQUAL : '<=';

LBRACE : '{';
RBRACE : '}';
EOF_TOKEN : '<EOF>';