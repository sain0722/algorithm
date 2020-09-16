def greedy(coins, k):
    count = 0
    total = k
    for coin in coins:
        if coin <= total:
            cnt = total // coin
            count += cnt
            total -= coin*cnt
        if total == 0:
            break
    return count
input_price = int(input())
change = 1000 - input_price
coins = [500, 100, 50, 10, 5, 1]
print(greedy(coins, change))
