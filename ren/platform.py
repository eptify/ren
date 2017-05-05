from __future__ import absolute_import

import platform
import base64


if platform.python_version().startswith('2'):
    from ren.py2grammar.renLexer import renLexer
    from ren.py2grammar.renParser import renParser
    from ren.py2grammar.renVisitor import renVisitor


    def _unichr(x):
        return unichr(x)


    def b64decode(s):
        return base64.b64decode(s)


    def b64encode(s):
        return base64.b64encode(s)


    def iteritems(d):
        return d.iteritems()


    def isstr(x):
        return isinstance(x, basestring)


else:
    from ren.py3grammar.renLexer import renLexer
    from ren.py3grammar.renParser import renParser
    from ren.py3grammar.renVisitor import renVisitor


    def _unichr(x):
        return chr(x)


    def b64decode(s):
        return base64.b64decode(s).decode()


    def b64encode(s):
        return base64.b64encode(bytes(s, "utf-8")).decode()


    def iteritems(d):
        return d.items()


    def isstr(x):
        return isinstance(x, str)
