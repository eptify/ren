grammar ren ;
WS : [ \t\r\n]+ -> channel(HIDDEN) ;
COMMENT : ';' ~[\r\n]* -> skip ;
renlist : '[' value* ']' | '(' value* ')' ;
renmap : '#(' nameValuePair* ')' ;
nameValuePair : name value ;
name : word ':' SPACE ;
value : renlist | renmap | none | logic | name | word
    | anyNumber | anyString | anyDateTime 
    | anyBinary | rentuple | point ;
anyNumber : Number | Percent | Money | NAN | INF ;
anyString : String ; //| impliedString ;
anyDateTime : DateTime | Date | RelDateTime | RelDate | RelTime ;
anyBinary : B16binary | B64binary ;
String : ('"' CHAR* '"') | MultilineString | Tag ;
MSCHAR : ~[{}^] ;
MultilineString : '{' (MSCHAR* | MultilineString) '}' ;
TAGCHAR : ~[<>^] ;
Tag : '<' (TAGCHAR | Tag)* '>' ;
CHAR : ~["^\n\r] ;
Number : SIGN? INT FRAC? EXP? ;
Percent : Number '%' ;
Money : SIGN? '$' INT FRAC? ;
NAN : '1.#NaN' ;
INF : SIGN? '1.#INF' ;
none : 'none' ;
logic : 'true' | 'false' | 'on' | 'off' | 'yes' | 'no' ;
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
word : WordFirstChar WordInnerChar* ;
WordFirstChar : ~[0-9{}"()/\\@#$%^,:;<>[\]'] ;
WordInnerChar : WordFirstChar | DIGIT ;
/*
impliedString : ImplStrFirstChar implStrInnerChar* ;
ImplStrFirstChar : ~[0-9{}"()\\$^,;<>[\]] ;
implStrInnerChar :
    (WordInnerChar | '/' | '\\' | '@' | '#' | '$' | '%' | ',' | ':' | '\'')
    (ImplStrFirstChar | DIGIT | '\\' | '$' | ',') ;
*/
rentuple : INT tuplePart tuplePart+ ;
tuplePart : '.' INT ;
point : Number axis+ ;
axis : 'x' Number ;
B16binary : '16'? '#{' (B16CHAR B16CHAR)* '}' ;
B64binary : '64#{' (B64CHAR B64CHAR B64CHAR B64CHAR)* '}' ;
SIGN : '-' ;
FRAC : '.' INT ;
INT : [0-9]+ ;
EXP : [eE] [+\-]? INT ;
B16CHAR : [0-9A-Fa-f] ;
B64CHAR : [0-9A-Za-z+/=] ;
DIGIT : [0-9] ;
SPACE : [ \t\r\n]+ ;
