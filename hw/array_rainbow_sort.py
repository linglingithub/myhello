class Solution:
    # todo
    def rainbow_sort(self, arr):
        """
        three colors, sort to three parts
        :param arr:
        :return:
        """
        i, j = 0, len(arr) - 1
        # [0, i) is the good area for 0s, (j, len(arr) - 1] is the good area for 2s
        while i <= j:
            if arr[i] == 0:
                i += 1
            if arr[j] == 2:
                j -= 1

    def rainbow_sort_k_colors(self, arr):
        """
        Method 1: quick sort, time O(nlogn) average, worst O(n^2), space O(n) ???
        Method 2: counting sort, time O(n), space O(k)
        :param arr:
        :return:
        """