def swap_case(s):
    new_str = ""
    for word in s:
        if word.isupper():
            new_str += word.lower()
        else:
            new_str += word.upper()
    return new_str


if __name__ == "__main__":
    s = "Python2"
    result = swap_case(s)
    print(result)
