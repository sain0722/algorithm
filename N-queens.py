# 201533812 이상민


# i = 저장한 queen 의 개수
# ex) queens(2) = 여태까지 2 개의 퀸의 위치를 저장했음.
# 호출 시 최초 i=0
def queens(i=0):

    # promising 체크
    if promising(i):
        # 솔루션이 완성되었는가?
        # i가 N번째 퀸까지 저장이 되었는가??
        if i == N:

            # 출력 폼에 맞추기 위해 result_str 에 저장하고, result_list 에 넣는다.
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

        # 같은 열에 있거나, 서로의 범위에 있는 대각선에 있는지 체크
        # col[i] - col[k] = 열의 차이,      i - k = 행의 차이
        # 행의 차이와 열의 차이가 같다면 대각선의 위치이다.
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            switch = False
        k += 1

    return switch


def print_solution():

    total_number = 0

    # 출력을 위한 범위 설정
    epoch = len(result_list) // N

    # 결과 출력
    for i in range(1, epoch + 1):
        print("{}: {}".format(i, result_list[N * (i - 1): N * i]).replace("'", ""))
        total_number = i
    # N * N 체스판에서 queen 을 놓을 수 있는 경우의 수
    # for 문의 마지막 i 값이 총 경우의 수이다.
    print("Total Number:", total_number)


if __name__ == "__main__":

    # 4 <= N <= 10 이므로, 범위에서 벗어난 값을 입력하지 못하게 설정.
    while True:
        N = int(input())

        if N < 4 or N > 10:
            print("[범위 오류] 4부터 10 사이의 값을 입력하시오.")
        else:
            break

    # col 을 전역에 선언
    col = [0] * (N + 1)

    # 결과값을 저장할 리스트 선언
    result_list = []

    # queens 호출
    queens()

    # 출력형태를 맞춘 결과를 print
    print_solution()
