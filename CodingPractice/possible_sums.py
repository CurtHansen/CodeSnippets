def possibleSums(coins, quantity):
    set_of_unique_sums = {0}
    set_new_sums = set()

    for coin, count in zip(coins, quantity):
        quantities_possible = range(0, count + 1)

        set_new_sums.clear()

        for quantity_chosen_for_coin in quantities_possible:
            incremental_value = coin * quantity_chosen_for_coin

            for existing_value in set_of_unique_sums:
                set_new_sums |= {existing_value + incremental_value}

        set_of_unique_sums |= set_new_sums

    """swap
    def recursive_compute(level, quantities_chosen):

        if level == num_distinct_coins:
            sum = 0
            for i in range(num_distinct_coins):
                sum += coins[i] * quantities_chosen[i]
            if sum > 0:
                set_of_sums.add(sum)

        else:
            for j in range(0, quantity[level] + 1):
                quantities_chosen[level] = j
                recursive_compute(level+1, quantities_chosen)

    empty_quantities_chosen = [0] * num_distinct_coins
    recursive_compute(0, empty_quantities_chosen)
    """

    set_of_unique_sums.remove(0)

    return len(set_of_unique_sums)


if __name__ == '__main__':
    print(possibleSums([10, 50, 100], [1, 2, 1]))