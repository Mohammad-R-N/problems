if __name__ == "__main__":
    holder = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        holder.append([name, score])

    for i in range(len(holder)):
        temp = None
        for j in range(len(holder)):
            if holder[j][1] < holder[i][1]:
                temp = holder[i]
                holder[i] = holder[j]
                holder[j] = temp

    for i in range(len(holder)):
        temp = None
        for j in range(len(holder)):
            if holder[j][0] > holder[i][0] and holder[j][1] == holder[i][1]:
                temp = holder[i]
                holder[i] = holder[j]
                holder[j] = temp

    test_number = -1
    for k in range(len(holder)):

        if holder[test_number][1] != holder[test_number - 1][1]:
            second_lowest = holder[test_number - 1][1]
            break
        test_number -= 1

    for m in range(len(holder)):
        if holder[m][1] == second_lowest:
            print(holder[m][0])
