def find_runner_up(arr):
    new_arr = list(arr)
    new_arr.sort()
    if len(arr) > 1:
        return new_arr[-2]
    elif len(new_arr) == 1:
        return new_arr[0]
    return None


n = int(input())
arr = map(int, input().split())
arr = set(arr)
print(find_runner_up(arr))
