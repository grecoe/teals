import collections

cell_data = collections.namedtuple("cell", "content width")

def print_row(columns, data, print_border = True):
    border = '|' if print_border else ' '
    buffer = ''
    for idx in range(len(data)):
        spacer = border if not len(buffer) else '|'
        buffer += spacer + str(data[idx]).center(columns[idx])
    buffer += border
    print(buffer)

def print_banner(columns, data):

    is_multi_row = False
    if isinstance(data[0], list):
        is_multi_row = True

    if not columns:
        columns = []
        # Figure it out
        if is_multi_row:
            for row in data:
                for idx in range(len(row)):
                    width = len(str(row[idx])) + 2
                    if len(columns) > idx:
                        columns[idx] = width if width > columns[idx] else columns[idx]
                    else:
                        columns.append(width) 
        else:
            for d in data:
                columns.append(len(d) + 2)

    elif is_multi_row:
        for row in data:
            assert(len(columns) == len(row))
    else:
        assert(len(columns) == len(data))

    width = 1 # account for outer bars
    for col in columns:
        width += col + 1

    banner = '-' * width
    print(banner)
    if is_multi_row:
        for row in data:
            print_row(columns, row)
    else:
        print_row(columns, data)

    print(banner)

    return banner, columns
