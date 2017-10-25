"""
31. Next Permutation

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

import unittest


class Solution(object):
    def nextPermutation(self, nums):
        """
        find the first reversed order from right --> '12543', pos = 2,  ; 53421, pos = 2 , 54321, 54123； 543122, pos=
        if pos = 0, reverse whole list
        else: swap pos-1 and [pos:] 中比pos-1大的最小数，n-1, then sort the [pos:] part --> 13542, 
        (ref: 最后是不需要sort的，因为换过去之后，后面已经是按降序排列了，所以直接reverse就可以了。???)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:  # should add = here, for equal vals, case7
            i -= 1
        if i == 0:
            nums.reverse()
            return
        min_bigger = self.find(nums, i - 1)
        nums[i-1], nums[min_bigger] = nums[min_bigger], nums[i-1] # not i, i-1 is the pos to be swapped
        nums[i:] = reversed(nums[i:])  # not exactly in place, create a shallow copy of nums[i:]

    def find(self, nums, pos):
        target = nums[pos]
        i = pos+1 # can't init as pos, otherwise dead loop
        while i < len(nums):
            if nums[i] > target:
                i += 1
            else:
                break   # don't forget to add break, otherwise dead loop for case 5
        return i - 1

class Solution1(object):
    def nextPermutation(self, nums): # 66ms, 82.19% --- 72ms, 57.19%
        """
        Trying to find the lexicographical order
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 2:
            return
        right_descending = (nums[-1] > nums[-2])
        if right_descending:
            nums[-1], nums[-2] = nums[-2], nums[-1]
        else:
            idx = len(nums)-1
            while nums[idx]<=nums[idx-1]:
                idx -= 1
                if idx==0:
                    break
            if idx==0: #already the biggest permu, return the first one
                nums.reverse()
            else:
                # nums[idx:] = sorted(nums[idx:])
                # or trying to do reverse, could be a little faster ===>
                swaplen = (len(nums) - idx) / 2
                for i in range(swaplen):
                    nums[idx+i], nums[-1-i] = nums[-1-i], nums[idx+i]
                # <====
                for i in range(idx, len(nums)):
                    if nums[i]<=nums[idx-1]:
                        continue
                    else:
                        nums[i], nums[idx-1] = nums[idx-1], nums[i]
                        break








class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3]
        answer = [1,3,2]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case2(self):
        nums = [3, 2, 1]
        answer = [1, 2, 3]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case3(self):
        nums = [1,1,5]
        answer = [1,5,1]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case4(self): # ====>
        nums = [1, 3, 2]
        answer = [2, 1, 3]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case5(self):  # ====>
        nums = [2,3,1]
        answer = [3,1,2]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case6(self):  # ====>
        nums = [1,5,1]
        answer = [5,1,1]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case07(self):  # ====>
        nums = [5,1,1]
        answer = [1,1,5]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



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