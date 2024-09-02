import json


def line(char='-', length=80):
    if not isinstance(char, str):
        char = '-'
    if not isinstance(length, int):
        length = 80

    print(char * length)


def dir2(obj):
    attrs = []
    for attr in dir(obj):
        if not attr.startswith('_'):
            attrs.append(attr)
    return attrs


def deep_copy(obj):
    return json.loads(json.dumps(obj))


def to_float(s):
    try:
        return float(s)
    except ValueError:
        return None
    
