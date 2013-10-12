class SyntaxItem(object):
    def __init__(self, name, definition):
        self._name = name
        self._defi = definition


class CSSToken(SyntaxItem):
    def __init__(self, name, definition):
        super(CSSToken, self).__init__(name, definition)


class CSSMacro(SyntaxItem):
    def __init__(self, name, definition):
        super(CSSMacro, self).__init__(name, definition)


class CSSTokenizer(object):
    def __init__(self):
        self.validtoks = {
            'IDENT': CSSToken('IDENT', '{ident}'),
            'ATKEYWORD': CSSToken('ATKEYWORD', '@{ident}'),
            'STRING': CSSToken('STRING', '{string}'),
            'BAD_STRING': CSSToken('BAD_STRING', '{badstring}'),
            'BAD_URI': CSSToken('BAD_URI', '{baduri}'),
            'BAD_COMMENT': CSSToken('BAD_COMMENT', '{badcomment}'),
            'HASH': CSSToken('HASH', '#{name}'),
            'NUMBER': CSSToken('NUMBER', '{num}'),
            'PERCENTAGE': CSSToken('PERCENTAGE', '{num}%'),
            'DIMENSION': CSSToken('DIMENSION', '{num}{ident}'),
            'URI': CSSToken('URI', 'url\({w}{string}{w}\)|url\({w}([!#$%&*-\[\]-~]|{nonascii}|{escape})*{w}\)'),
            'UNICODE-RANGE': CSSToken('UNICODE-RANGE', 'u\+[0-9a-f?]{1,6}(-[0-9a-f]{1,6})?'),
            'CDO': CSSToken('CDO', '<!--'),
            'CDC': CSSToken('CDC', '-->'),
            ':': CSSToken(':', ':'),
            ';': CSSToken(';', ';'),
            '{': CSSToken('{', '\{'),
            '}': CSSToken('}', '\}'),
            '(': CSSToken('(', '\('),
            ')': CSSToken(')', '\)'),
            '[': CSSToken('[', '\['),
            ']': CSSToken(']', '\]'),
            'S': CSSToken('S', '[ \t\r\n\f]+'),
            'COMMENT': CSSToken('COMMENT', '\/\*[^*]*\*+([^/*][^*]*\*+)*\/'),
            'FUNCTION': CSSToken('FUNCTION', '{ident}\('),
            'INCLUDES': CSSToken('INCLUDES', '~='),
            'DASHMASH': CSSToken('DASHMASH', '|='),
            'DELIM': CSSToken('DELIM', '') # anything not matched by the above
        }

        self.macros = {
            'ident': CSSMacro('ident', '[-]?{nmstart}{nmchar}*'),
            'name': CSSMacro('name', '{nmchar}+'),
            'nmstart': CSSMacro('nmstart', '[_a-z]|{nonascii}|{escape}'),
            'nonascii': CSSMacro('nonascii', '[^\\0-\\237]'),
            'unicode': CSSMacro('unicode', '\\[0-9a-f]{1,6}(\r\n|[ \n\r\t\f])?'),
            'escape': CSSMacro('escape', '{unicode}|\\[^\n\r\f0-9a-f]'),
            'nmchar': CSSMacro('nmchar', '[_a-z0-9-]|{nonascii}|{escape}'),
            'num': CSSMacro('num', '[0-9]+|[0-9]*\.[0-9]+'),
            'string': CSSMacro('string', '{string1}|{string2}'),
            'string1': CSSMacro('string1', '\"([^\n\r\f\\"]|\\{nl}|{escape})*\"'),
            'string2': CSSMacro('string2', '\'([^\n\r\f\\\']|\\{nl}|{escape})*\''),
            'badstring': CSSMacro('badstring', '{badstring1}|{badstring2}'),
            'badstring1': CSSMacro('badstring1', '\"([^\n\r\f\\"]|\\{nl}|{escape})*\\?'),
            'badstring2': CSSMacro('badstring2', '\'([^\n\r\f\\\']|\\{nl}|{escape})*\\?'),
            'badcomment': CSSMacro('badcomment', '{badcomment1}|{badcomment2}'),
            'badcomment1': CSSMacro('badcomment1', '\/\*[^*]*\*+([^/*][^*]*\*+)*'),
            'badcomment2': CSSMacro('badcomment2', '\/\*[^*]*(\*+[^/*][^*]*)*'),
            'baduri': CSSMacro('baduri', '{baduri1}|{baduri2}|{baduri3}'),
            'baduri1': CSSMacro('baduri1', 'url\({w}([!#$%&*-~]|{nonascii}|{escape})*{w}'),
            'baduri2': CSSMacro('baduri2', 'url\({w}{string}{w}'),
            'baduri3': CSSMacro('baduri3', 'url\({w}{badstring}'),
            'nl': CSSMacro('nl', '\n|\r\n|\r|\f'),
            'w': CSSMacro('w', '[ \t\r\n\f]*'),
        }