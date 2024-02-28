grammar DSL_Data_Formulas_Visualization_Grammar;

// Parser rules
program : commandsList;

commandsList : command+;

command : readCommand SEMICOLON
        | exportCommand SEMICOLON
        | visualizeCommand SEMICOLON;

readCommand : 'Data' ID ASSIGN readFromFile
            | 'Formula' ID ASSIGN formulaContent;

readFromFile : READ_FROM LPAREN PATH RPAREN;

exportCommand : 'ExportToFile' LPAREN PATH RPAREN exportToFile
              | 'ExportToImage' LPAREN PATH RPAREN exportToImage;

exportToFile : 'dataset' ASSIGN LPAREN ID RPAREN 'name' ASSIGN LPAREN ID DOT fileType RPAREN;

exportToImage : plotType LPAREN ID RPAREN 'name' ASSIGN LPAREN ID DOT imageType RPAREN;

visualizeCommand : visualizeFormula
                 | visualizeData;

visualizeFormula : VISUAL_FORMULA LPAREN formulaContent RPAREN 'range' ASSIGN LPAREN DIGIT COMMA DIGIT RPAREN
                 | VISUAL_FORMULA LPAREN ID RPAREN 'range' ASSIGN LPAREN DIGIT COMMA DIGIT RPAREN;

visualizeData : VISUAL_DATA LPAREN visualizationType RPAREN 'dataset' ASSIGN LPAREN ID RPAREN;

visualizationType : 'console' | plotType;

plotType : GRAPH | BAR | PIE | HIST;

fileType : CSV | TEXT | JSON | EXCEL;

imageType : PNG | JPG;

formulaContent : FORMULA;


// Lexer rules
START : 'Start';
END : 'End';
READ_FROM : 'ReadFrom';
EXPORT_TO : 'Export';
VISUAL_FORMULA : 'VisualFormula';
VISUAL_DATA : 'VisualData';
GRAPH : 'graph';
BAR : 'bar';
PIE : 'pie';
HIST : 'hist';
PNG : 'png';
JPG : 'jpg';
CSV : 'csv';
TEXT : 'text';
JSON : 'json';
EXCEL : 'excel';
ID : [a-zA-Z_/]+[a-zA-Z0-9_/]*;
PATH : '"' [a-zA-Z0-9_/]+ '"';
FORMULA : 'formula[' (ID | OPERATORS | LPAREN | RPAREN | DIGIT | '+' | '-' | '*' | '/' | '^' | WS)+ ']';
SEMICOLON : ';';
COLON : ':';
COMMA : ',';
LPAREN : '(';
RPAREN : ')';
ASSIGN : '=';
MINUS : '-';
OPERATORS : '*' | '^' | 'log' | 'sqr' | 'sqrt' | 'fact';
DATA : 'data';
DIGIT : '-'? [0-9]+;
DOT : '.';
WS : [ \t\r\n]+ -> skip; // Skip whitespace