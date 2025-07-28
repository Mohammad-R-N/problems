import textwrap


def wrap(string, max_width):
    new_str = ""
    for i, j in enumerate(string):
        if (i + 1) % max_width == 0:
            new_str += j

            new_str += "\n"
        else:
            new_str += j
    return new_str


if __name__ == "__main__":
    # string, max_width = input(), int(input())
    result = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)
    print(result)
