coins = [1, 2, 5, 10, 20, 50, 100, 200]
memo = {}
def number_of_combos(n, min_coin):
    if n == 0:
        return 1
    key = f'{n}|{min_coin}'
    if key not in memo:
        count = 0
        for coin in coins:
            if coin < min_coin:
                continue
            if coin > n:
                break
            count += number_of_combos(n - coin, coin)
        memo[key] = count
    return memo[key]

print(number_of_combos(200, 1))