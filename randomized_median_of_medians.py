# randomized_median_of_medians.py

import sys
import random

class RandomizedMedianOfMedians:
    "Implementation of the RandomizedSelect algorithm in Python"

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def median_of_medians(self, array, index):

        # Return the result for a short array straight away.
        if len(array) <= 10:
            array.sort()
            return array[index]

        # Choose our pivot separating the values on the given list randomly. Note that the worst case scenario here would be of O(N^2) complexity.
        pivot = array[random.randint(0, len(array) - 1)]

        # Print out the chosen pivot for God-knows-why purpouses.
        sys.stderr.write("Chosen pivot: {}\n".format(pivot))

        # Use the pivot to divide the given list of inputs into separate sets; elements smaller than the pivot, greater than the pivot and equal to the pivot's value.
        lesser = []
        greater = []
        equal = []

        for item in array:
            if item < pivot:
                lesser.append(item)

                self.comparisons += 1
                self.swaps += 1
                sys.stderr.write("random select: item: {} < pivot: {}\n".format(item, pivot))
            elif item > pivot:
                greater.append(item)

                self.comparisons += 1
                self.swaps += 1
                sys.stderr.write("random select: item: {} > pivot: {}\n".format(item, pivot))
            else:
                equal.append(item)

                self.comparisons += 1
                self.swaps += 1
                sys.stderr.write("random select: item: {} == pivot: {}\n".format(item, pivot))

        # Returns the result based on the position of the index (k) we're looking for.
        if index < len(lesser):
            self.comparisons += 1
            sys.stderr.write("select: index: {} is in lesser\n".format(index))

            return self.median_of_medians(lesser, index)
        elif index < len(lesser) + len(equal):
            self.comparisons += 1
            sys.stderr.write("select: index: {} is in equal\n".format(index))

            return equal[0]
        else:
            self.comparisons += 1
            sys.stderr.write("select: index: {} is in greater\n".format(index))

            greater_index = index - (len(lesser) + len(equal))
            return self.median_of_medians(greater, greater_index)
