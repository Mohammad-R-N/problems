def average(array):
    my_set = set(array)

    my_set = sum(my_set) / len(my_set)
    return round(my_set, 3)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
