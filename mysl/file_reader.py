
def line_to_tuple_in_list(file, separator, ignore_headline=False):
    lines = list()
    with open(file) as f:
        if ignore_headline:
            next(f)
        for line in f:
            line = line[:-1] #removing \n
            if separator is None:
                lines.append(line)
            else:
                lines.append(tuple(line.split(separator)))
    return lines


def line_to_list(file, ignore_headline=False):
    lines = line_to_tuple_in_list(file, separator=None, ignore_headline=ignore_headline)
    return lines


def write_item_per_line(file, content, headline=None):
    write_tupla_per_line(file, content, separator=None, headline=headline)


def write_tupla_per_line(file, tuplas, separator=None, headline=None):
    with open(file, 'w') as f:
        if headline is not None:
            content = [headline] + tuplas
        else:
            content = tuplas

        for t in content:
            if separator is None: # t is a string, not a tuple.
                f.write(t)
                f.write('\n')
            else:
                for i, part in enumerate(t):
                    f.write(str(part))
                    if i < len(t) - 1:
                        f.write(separator)
                f.write('\n')


