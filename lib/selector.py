class Selector(object):
    TYPE_CLASS = 'class'
    TYPE_ID = 'id'
    TYPE_ELEMENT = 'element'
    def __init__(self, raw, type):
        __raw = raw
        _type = type
