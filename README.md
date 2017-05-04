TODO
----
[x] implied string literals (url, email, file, issues, etc.)
[x] spaces in binary literals
[x] fix name loads, dumps
[x] binary literal decoding
[x] timedelta, datetime loads
[x] date, datetime, timedelta dumps
[x] string escaping and unescaping
[x] parenthesized escapes (^(line), ^(tab), ^(XXXX), etc.)
[x] unicode in strings
[x] test suite
[x] directory layout
[x] loads, dumps, load, dump, interface
[x] raise ValueError on parse errors
[x] unify tests
[x] support parsing multiple values (implied list)
[x] multiline string escaping and unescaping
[x] implied string and tag as separate types
[x] remove RelDate, RelDateTime
[x] dumps, loads for Date, DateTime with timezone
[ ] simplify visitor, grammar lexer and parser rules
[ ] support python3, pypy
[ ] move make target implementations into setup.py
[ ] indented pretty printing
[ ] fix any lint issues

[ ] allow words starting with '<', '>' that aren't valid tags
[ ] optional 3 character currency tags (e.g. USD$2.50, EUR$2.00)
[ ] base 2 and octal literals
