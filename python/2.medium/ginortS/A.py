# s = list(input().strip())
s = list("Sorting1234 ".strip())


def func(s):
    upper_words = []
    lower_words = []
    digits = []
    for i in s:
        if i.isupper():
            upper_words.append(i)
        elif i.islower():
            lower_words.append(i)
        elif i.isdigit():
            digits.append(i)
    upper_words.sort()
    lower_words.sort()
    digits.sort()
    odd_sorted = []
    even_sorted = []
    for j in digits:
        if int(j) % 2 != 0:
            odd_sorted.append(j)
        else:
            even_sorted.append(j)
    upper_words = "".join(upper_words)
    lower_words = "".join(lower_words)
    odd_sorted = "".join(odd_sorted)
    even_sorted = "".join(even_sorted)

    return f"{lower_words}{upper_words}{odd_sorted}{even_sorted}"


print(func(s))
