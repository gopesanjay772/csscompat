import sys

cssfile = open('test.css')

text = cssfile.read()
selectors = []

selbuf = ""
inBlock = False
for c in text:
    if not inBlock:
        if c == '{':
            selectors.append(selbuf.strip())
            selbuf = ""
            inBlock = True
        elif c == ',':
            selectors.append(selbuf.strip())
            selbuf = ""
        else:
            selbuf += c
    else:
        if c == '}':
            inBlock = False
cssfile.close()


tok = []
for s in selectors:
    tokens = s.split()
    for t in tokens:
        if t[0] == '.':
            tok.append({'type': 'class', 'selector': t})
        elif t[0] == '#':
            tok.append({'type': 'id', 'selector': t})
        elif t[0].isalpha():
            tok.append({'type': 'element', 'selector': t})
        elif t.find('+') or t.find(':'):
            pass





print selectors
print tok
print(str.format("\nnumber of selectors: {0}", len(selectors)))