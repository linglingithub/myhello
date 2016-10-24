"""
Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 --> 1,3,2
3,2,1 --> 1,2,3
1,1,5 --> 1,5,1
Subscribe to see which companies asked this question

Hide Tags Array
Hide Similar Problems (M) Permutations (M) Permutations II (M) Permutation Sequence (M) Palindrome Permutation II


"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


##################################################



class Solution_old:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1: return num
        partition = -1
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                partition = i
                break
        if partition == -1:
            num.reverse()
            return num
        else:
            for i in range(len(num)-1, partition, -1):
                if num[i] > num[partition]:
                    num[i],num[partition] = num[partition],num[i]
                    break
        num[partition+1:len(num)]=num[partition+1:len(num)][::-1]
        return num

# if __name__ == '__main__':
#     sol = Solution()
#     print sol.nextPermutation(1432)