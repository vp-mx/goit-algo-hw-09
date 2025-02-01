import time


def find_coins_greedy(amount: int) -> dict[int, int]:
    """Greedy algorithm to find the minimum number of coins for a given amount.

    :param: amount (int): The amount of money to be changed into coins.
    :return: dict: A dictionary with coin denominations as keys and the number of each coin as values.
    """

    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin  # How many coins of this type we can use.
        if count > 0:
            result[coin] = count
            amount %= coin  # Update the remaining amount.
    return result


def find_min_coins(amount: int) -> dict[int, int]:
    """Dynamic programming algorithm to find the minimum number of coins for a given amount.

    :param: amount (int): The amount of money to be changed into coins.
    :return: dict: A dictionary with coin denominations as keys and the number of each coin as values.
    """
    coins = [1, 2, 5, 10, 25, 50]
    min_coins = [0] + [float("inf")] * amount
    coin_count = [0] + [None] * amount

    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_count[x] = coin

    result = {}
    while amount > 0:
        coin = coin_count[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


def measure_time(func: callable, amount: int) -> float:
    """Measure the time a function takes to run.

    :param func: (callable): The function to measure.
    :param amount: (int): The amount to pass to the function.
    :return: float: The time taken to run the function.
    """
    start = time.perf_counter()
    func(amount)
    return time.perf_counter() - start


def evaluate_efficiency() -> tuple[list[int], list[float], list[float]]:
    """Evaluates the efficiency of the greedy and dynamic programming algorithms.

    :return: A tuple containing the list of amounts, greedy times, and dynamic programming times.
    """
    amounts = [100, 1000, 10000, 100000, 1000000]
    greedy_times = [measure_time(find_coins_greedy, amt) for amt in amounts]
    dp_times = [measure_time(find_min_coins, amt) for amt in amounts]
    return amounts, greedy_times, dp_times


if __name__ == "__main__":
    amounts, greedy_times, dp_times = evaluate_efficiency()

    print("Greedy Algorithm Times:")
    for amt, t in zip(amounts, greedy_times):
        print(f"Amount: {amt:>7} - Time: {t:.6f} seconds")

    print("\nDynamic Programming Algorithm Times:")
    for amt, t in zip(amounts, dp_times):
        print(f"Amount: {amt:>7} - Time: {t:.6f} seconds")
