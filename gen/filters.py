import re
import inflect

def lower_camel_case(s):
    return re.sub(r'[\W]+(\w)', lambda p: p.group(1).upper(), s)


def lower_snake_case(s):
    lst = []
    for i in re.split(r'[\W]+', s):
        if len(i) > 1:
            lst.append(i[0].lower() + i[1:])
        else:
            lst.append(i[0].lower())
    return '_'.join(lst)


def upper_snake_case(s):
    lst = []
    for i in re.split(r'[\W]+', s):
        if len(i) > 1:
            lst.append(i[0].upper() + i[1:])
        else:
            lst.append(i[0].upper())
    return '_'.join(lst)


def upper_camel_case(s):
    return re.sub(r'^(\w)', lambda p: p.group(1).upper(), lower_camel_case(s))


def pluralize(s):
    return inflect.engine().plural(s)


filters = {
    'upper_camel_case': upper_camel_case,
    'lower_camel_case': lower_camel_case,
    'lower_snake_case': lower_snake_case,
    'upper_snake_case': upper_snake_case,
    'plural': pluralize,
}

if __name__ == "__main__":
    import sys
    orig = " ".join(sys.argv[1:])
    for k, v in filters.items():
        tx = v(orig)
        print(f"{orig} ==> {k}:  {tx}")
