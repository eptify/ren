grammar ren ;
/*parser*/
singleValue : value EOF ;
renlist : '[' value* ']' | '(' value* ')' ;
renmap : '#(' nameValuePair* ')' ;
nameValuePair : name value ;
name : Name ;
value : renlist | renmap | none | logic | name | word
    | anyNumber | anyString | anyDateTime 
    | anyBinary | rentuple | point ;
none : NONE ;
logic : LOGIC ;
point : Point ;
word : Word ;
anyNumber : Number | Percent | Money | NAN | INF ;
anyString : String ; //| ImpliedString ;
anyDateTime : DateTime | Date | RelDateTime | RelDate | RelTime ;
anyBinary : B16binary | B64binary ;
rentuple : TUPLE ;
/*lexer*/
WS : [ \t\r\n]+ -> channel(HIDDEN) ;
COMMENT : ';' ~[\r\n]* -> skip ;
Number : SIGN? INT FRAC? EXP? ;
Percent : Number '%' ;
Money : SIGN? '$' INT FRAC? ;
NAN : '1.#NaN' ;
INF : SIGN? '1.#INF' ;
NONE : 'none' ;
LOGIC : 'true' | 'false' | 'on' | 'off' | 'yes' | 'no' ;
Date : DIGIT DIGIT DIGIT DIGIT '-' DIGIT DIGIT '-' DIGIT DIGIT ;
TimeOfDay : DIGIT DIGIT ':' DIGIT DIGIT Seconds? ;
Seconds : ':' DIGIT DIGIT FRAC? ;
DateTimeSep : '/' | 'T' ;
Timezone : SIGN? 'Z' | SIGN TimeOfDay ;
DateTime : Date DateTimeSep TimeOfDay Timezone? ;
RelDate : SIGN? DIGIT DIGIT DIGIT DIGIT+ '-' INT '-' INT ;
RelTime : SIGN? INT ':' INT RelSeconds? ;
RelSeconds : ':' DIGIT+ FRAC? ;
RelDateTime : RelDate DateTimeSep RelTime ;
// relDateTime : SIGN? INT ':' INT ':' INT ':' relTime ;
Name : Word ':' SPACE ;
Word : WordFirstChar WordInnerChar* ;
fragment WordFirstChar : ~[ \t\r\n0-9{}"()/\\@#$%^,:;<>[\]'] ;
fragment WordInnerChar : WordFirstChar | DIGIT ;
TUPLE : INT TuplePart TuplePart+ ;
fragment TuplePart : '.' INT ;
Point : Number Axis+ ;
Axis : 'x' Number ;
B16binary : '16'? '#{' (B16CHAR B16CHAR)* '}' ;
B64binary : '64#{' (B64CHAR B64CHAR B64CHAR B64CHAR)* '}' ;
fragment SIGN : '-' ;
fragment FRAC : '.' INT ;
INT : [0-9]+ ;
fragment EXP : [eE] [+\-]? INT ;
B16CHAR : [0-9A-Fa-f] ;
B64CHAR : [0-9A-Za-z+/=] ;
fragment DIGIT : [0-9] ;
fragment SPACE : [ \t\r\n]+ ;
String : ('"' CHAR* '"') | MultilineString | Tag ;
MSCHAR : ~[{}^] ;
MultilineString : '{' (MSCHAR* | MultilineString) '}' ;
TAGCHAR : ~[<>^] ;
Tag : '<' (TAGCHAR | Tag)* '>' ;
CHAR : ~["^\n\r] ;
/*
ImpliedString : ImplStrFirstChar ImplStrInnerChar* ;
ImplStrFirstChar : ~[0-9{}"()\\$^,;<>[\]] ;
ImplStrInnerChar :
    (WordInnerChar | '/' | '\\' | '@' | '#' | '$' | '%' | ',' | ':' | '\'')
    (ImplStrFirstChar | DIGIT | '\\' | '$' | ',') ;
*/
