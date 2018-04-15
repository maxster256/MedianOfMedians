# median.py

import argparse
from randomized_median_of_medians import RandomizedMedianOfMedians
from median_of_medians import MedianOfMedians
import sys
import random

parser = argparse.ArgumentParser()

parser.add_argument(
    '--r',
    nargs = 2,
    type = int,
)

parser.add_argument(
    '--p',
    nargs = 2,
    type = int,
)

args = parser.parse_args()

if args.p != None:

    # Operate on the randomized permutation of the set {1, 2, ..., n}
    n = args.p[0]
    k = args.p[1]

    data = random.sample(range(n), n)

    sys.stderr.write("Input array: {}\nK given: {}\n".format(data, k))

    for select in [MedianOfMedians(), RandomizedMedianOfMedians()]:
        result = select.median_of_medians(data, k)

        for point in data:
            if point == result:
                print(" [{}] ".format(result), end="")
            else:
                print(" {} ".format(point), end="")

        sys.stderr.write("Total comparisons: {}, swaps: {}\n".format(select.comparisons, select.swaps))
        print("")

elif args.r != None:

    # Operate on random data of the length of n
    n = args.r[0]
    k = args.r[1]

    data = []
    for i in range(n):
        data.append(random.randint(0, n*10))

    sys.stderr.write("Input array: {}\nK given: {}\n".format(data, k))

    for select in [MedianOfMedians(), RandomizedMedianOfMedians()]:
        result = select.median_of_medians(data, k)

        for point in data:
            if point == result:
                print(" [{}] ".format(result), end="")
            else:
                print(" {} ".format(point), end="")

        sys.stderr.write("Total comparisons: {}, swaps: {}\n".format(select.comparisons, select.swaps))
        print("")
