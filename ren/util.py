import re


def escape(s):
    s = s.replace('"', '^"')
    s = s.replace('\n', '^/')
    s = s.replace('\r', '^M')
    s = s.replace('\0', '^@')
    return s


RE = re.compile("(\^\([a-fA-F0-9]+\))")


def unescape(s):
    s = s.replace('^"', '"')
    s = s.replace('^/', '\n')
    s = s.replace('^M', '\r')
    s = s.replace('^@', '\0')
    matches = RE.search(s)
    if matches:
        for group in matches.groups():
            hex = group[2:-1]
            s = s.replace(group, unichr(int(hex, 16)))
    return s
