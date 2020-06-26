def queens(i):

    global result_list
    if promising(i):
        if i == N:
            for index in range(1, N + 1):
                result_str = "<{}, {}>".format(index, col[index])
                result_list.append(result_str)

        else:
            for j in range(1, N + 1):
                col[i+1] = j
                queens(i + 1)


def promising(i):

    k = 1
    switch = True

    while k < i and switch:
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            switch = False
        k += 1

    return switch


N = int(input())
col = [0] * (N+1)
result_list = []

queens(0)

epoch = len(result_list) // N + 1
for i in range(1, epoch):
    print("{}: {}".format(i, result_list[N * (i-1): N * i]).replace("'", ""))

print("Total Number: ", i)