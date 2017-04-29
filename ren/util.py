def escape(s):
    s = s.replace('"', '^"')
    s = s.replace('\n', '^/')
    s = s.replace('\r', '^M')
    return s


def unescape(s):
    s = s.replace('^"', '"')
    s = s.replace('^/', '\n')
    s = s.replace('^M', '\r')
    return s
