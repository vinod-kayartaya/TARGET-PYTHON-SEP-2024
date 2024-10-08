import json, time

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
    

def csv2json(csv_filename, json_filename=None):
    if not csv_filename.lower().endswith('.csv'):
        raise ValueError('You must supply a .csv filename as the first argument')
    
    if json_filename is None:
        json_filename = f'{csv_filename[:-4]}.{time.time()}.json'

    if not json_filename.lower().endswith('.json'):
        raise ValueError('You must supply a .json filename as the second argument')

    with open(csv_filename, encoding='utf-8') as file:
        header = file.readline().strip().split(',')
        data = []
        for each_line in file:
            values = each_line.strip().split(',')
            d = dict(zip(header, values))
            data.append(d)
        
    with open(json_filename, mode='wt', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)
        print(f'JSON data saved to {json_filename}')


def lined(fn):
    def wrapper():
        print('-'*50)
        retval = fn()
        print('-'*50)
        return retval 
    
    return wrapper

def repeat(n=10):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fn(*args, **kwargs)
        return wrapper
    return decorator

def args_to_uppercase(fn):
    def decorator(*args, **kwargs):
        new_args = []
        for each_arg in args:
            if isinstance(each_arg, str):
                new_args.append(each_arg.upper())
            else:
                new_args.append(each_arg)
        
        new_kwargs = {}
        for key, val in kwargs.items():
            if isinstance(val, str):
                new_kwargs[key] = val.upper()
            else:
                new_kwargs[key] = val
        fn(*new_args, **new_kwargs)

    return decorator
