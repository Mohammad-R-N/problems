def find_weird(n):
    if n % 2 != 0:
        return "Weird"
    elif (n % 2 == 0) and (n in range(6, 21)):
        return "Weird"
    return "Not Weird"


if __name__ == "__main__":
    n = int(input().strip())
    print(find_weird(n))
