#!/usr/bin/python

# from recursive_sorting import merge_sort
import argparse
import sys
sys.path.insert(
    1, '/Users/zachiggins/lambdaSchool/cs/sorting/src/recursive_sorting/')
# importing my merge_sort function from yesterday :)


def find_max_profit(prices):
    profits = []  # holds all possible buy/sell profit combinations
    i = 0  # index pointer
    while i < len(prices) - 1:
        for index, price in enumerate(prices):
            if index + 1 < len(prices):
                for item in prices[index:]:
                    profit = item - price
                    if profit != 0:
                        profits.append(profit)
                i += 1

    # print(profits, "profits")
    profits.sort()
    # print(profits, "sorted profits")
    highest_profit = profits[-1]
    return highest_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
