import sys

cssfile = open('test.css')

selectors = []
selbuf = ""
text = cssfile.read()
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

print selectors
print(len(selectors))