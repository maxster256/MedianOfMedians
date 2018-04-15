# median_select.py
# Selects a middle value in an ordered set

import sys

class MedianOfMedians:
    "An implementation of the Select algorithm in Python"

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def median_of_medians(self, array, index):

        # Return the result for a short array straight away.
        if len(array) <= 10:
            array.sort()
            return array[index]

        # Divides the given array into sublists, each of length 5 (apart from the last one)
        sublist_size = 5  # max items in a sublist
        sublists = []  # list of sublists
        num_medians = int(len(array) / sublist_size)

        if (len(array) % sublist_size) > 0:
            num_medians += 1

        for i in range(num_medians):
            beg = i * sublist_size
            end = min(len(array), beg + sublist_size)

            sublist = array[beg:end]
            sublists.append(sublist)

        # Find the median values for the each sublist generated.
        medians = []

        for sublist in sublists:
            median = self.median_of_medians(sublist, int(len(sublist)/2))
            medians.append(median)

        # Find the median of all of the median values previously found and use it as the pivot element.
        median_of_medians = self.median_of_medians(medians, int(len(medians)/2))
        pivot = median_of_medians  # pivot point value (not index)

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
                sys.stderr.write("select: item: {} < pivot: {}\n".format(item, pivot))
            elif item > pivot:
                greater.append(item)

                self.comparisons += 1
                self.swaps += 1
                sys.stderr.write("select: item: {} > pivot: {}\n".format(item, pivot))
            else:
                equal.append(item)

                self.comparisons += 1
                self.swaps += 1
                sys.stderr.write("select: item: {} == pivot: {}\n".format(item, pivot))

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
