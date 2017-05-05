Ren
---
Python implementation of the [ren data format](http://ren-data.org).

```python
import ren

data = ren.loads("#(a: 1 b: 2)")
ren.dumps(data)
```

TODO
----
[x] implied string literals (url, email, file, issues, etc.)
[x] spaces in binary literals
[x] name loads, dumps
[x] binary literal decoding
[x] timedelta, datetime loads
[x] date, datetime, timedelta dumps
[x] string escaping and unescaping
[x] parenthesized escapes ^(XXXX)
[x] unicode in strings
[x] test suite
[x] loads, dumps interface
[x] raise ValueError on parse errors
[x] unify tests
[x] support parsing multiple values (implied list)
[x] multiline string escaping and unescaping
[x] implied string and tag as separate types
[x] dumps, loads for Date, DateTime with timezone
[x] support python2, python3, pypy
[x] fix flake8 issues
[x] run tests in multiple virtual environments
[x] move grammar target into setup.py
[x] 100% coverage
[ ] indented pretty printing
[ ] simplify grammar and visitor
[ ] improve tests
[ ] continuous integration
[ ] publish to pypi
