"""
Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
Subscribe to see which companies asked this question

Hide Tags Backtracking
Hide Similar Problems (M) Next Permutation (M) Permutations (M) Palindrome Permutation II


"""

import unittest


class Solution(object):
    """
    Compared to permutation, hard to use insertion way to generate. Not easy to think about how to deal with duplicates.
    Use recursive way. Think of how to void duplicated swap.

    --- but there is actually a insertion way, see ref3, try to understand it.
    """

    def permuteUnique(self, nums):  # 168ms, 20.36%
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) < 1:
            return []
        nums.sort()
        result = []
        self.dfs(result, [], nums, 0)
        return result

    def dfs(self, result, permu, nums, idx):
        if len(permu) == len(nums):
            result.append(permu)
            return
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            nums[i], nums[idx] = nums[idx], nums[i]
            self.dfs(result, permu + [nums[i]], nums, idx+1)
            nums[i], nums[idx] = nums[idx], nums[i]

    def permuteUnique_ref(self, num): # 105ms, 96.18%
        length = len(num)
        if length == 0: return []
        if length == 1: return [num]
        num.sort()
        res = []
        previousNum = None
        for i in range(length):
            if num[i] == previousNum: continue
            previousNum = num[i]
            for j in self.permuteUnique(num[:i] + num[i + 1:]):
                res.append([num[i]] + j)
        return res

    def permuteUnique_ref2(self, nums): #102ms, 96.91%
        # write your code here
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result

    def permuteUnique_slower(self, nums): #168ms, 20.36%
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums)<1:
            return []
        nums.sort()
        result = []
        used = [False] * len(nums)
        self.dfs1(result, [], nums, used)
        return result

    def dfs1(self, result, permu, nums, used):
        if len(permu) == len(nums):
            result.append(permu)
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                continue
            used[i] = True
            self.dfs1(result, permu+[nums[i]], nums, used)
            used[i] = False

    def permuteUnique_ref3(self, nums): #119ms, 78%
        """
        It is easy to come up with we should skip the same number we meet. 
        But that only covers intra-perm, like from "2,1" to "2,2,1" and "2,2,1", how about the inter-perm duplicate,
        like from "2,1" to "2,1,2" and from "1,2" to "2,1,2".
        When we first encounter the situation from "2,1" to "2,2,1" and "2,2,1",
        if we choose to "continue" and we will insert new "2" into rightmost position to get "2,1,2"
        which duplicates "2,1,2" later from "1,2".
        Why? First we start from permutation "---orig_num---" and insert new number from left to right.
        Once the new number is inserted right of its duplicate number, it looks like "---orig_num---insert_num---",
        which can be observed as "---new_num---orig_num---" extended from another permutation "---orig_num---" by
        inserting insert_num at left position. Because we operate on all permutations generated from previous loop,
        we can always find a previous permutation to cause inter-permation duplicate.
        Therefore, we should "break", other than "continue", after we encounter the first same number.
        :param nums:
        :return:
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: break  # handles duplication
            ans = new_ans
        return ans



    """

    3 different Java solution for this question with detailed explanation
    (from discussion of YaokaiYang )

    public class Solution {
    /**
     * If we are allowed to sort the array, we could sort the array to let the same number cluster together.
     * In this way, avoiding duplicates, which is to avoid the same number being the first number in the permutation, is simplified because we can judge is a number is the same as its previous one and if its previous one has been used.
     * We keep a boolean array to store the numbers being used, whose values are false originally.
     * Each time we use a number, we set its corresponding value in boolean array to be true.
     * And we try further down in the recursion.
     * Once the recursion returns, we backtrack by changing its corresponding boolean value to be false and remove it from the current result.
     * O(n!) time, O(n) space.
     */
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        if (nums == null || nums.length == 0) return ret;

        Arrays.sort(nums);
        boolean[] used = new boolean[nums.length];

        permuteHelper(nums, 0, ret, used, new ArrayList<Integer>());

        return ret;
    }

    private void permuteHelper(int[] nums, int len, List<List<Integer>> ret, boolean[] used, List<Integer> curr) {
        if (len == nums.length) {
            ret.add(new ArrayList<Integer>(curr));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                if (i > 0 && nums[i] == nums[i - 1] && used[i - 1]) {
                    continue;
                }
                used[i] = true;
                curr.add(nums[i]);
                permuteHelper(nums, len + 1, ret, used, curr);
                curr.remove(curr.size() - 1);
                used[i] = false;
            }
        }
    }



    /**
     * Based on the third method of permutations I, which is to swap 2 numbers in the array each time.
     * However, we want to avoid duplicates in this problem.
     * Avoiding duplicates in the permutations we got is actually avoiding let the same number to be the first number of the permutations. And this is also true in the subproblems we met.
     * So we simply keep a hashset at each level of the recursion tree to store the numbers we have used as the first number of the permutations generated from this level
     * Once we find a number already existed in the hashset, we would skip this number.
     * Other ideas is the same as Permutations I. Swap 2 numbers each time, recurse, and swap back. A typical backtracking problem.
     * O(n!) time. O(n ^ 2) space. The recursion would be n-level in depth.
     */
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        if (nums == null || nums.length == 0) return ret;

        permuteHelper(nums, 0, ret);

        return ret;
    }

    private void permuteHelper(int[] nums, int pos, List<List<Integer>> ret) {
        if (pos == nums.length) {
            List<Integer> curr = new ArrayList<>();
            for (int num : nums) {
                curr.add(num);
            }
            ret.add(curr);
            return;
        }

        Set<Integer> used = new HashSet<>();
        for (int i = pos; i < nums.length; i++) {
            if (used.add(nums[i])) {
                swap(nums, pos, i);
                permuteHelper(nums, pos + 1, ret);
                swap(nums, pos, i); //Backtracking
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        if (i == j) return;
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }


    /**
     * BackTracking.
     * If the nums array cannot be changed (i.e. cannot sort the array), than we may need to keep some thing to record which number have been used.
     * In this question, we keep a hashmap with the numbers in the nums as the key and the number of their appearance as value
     * So each time we used a number, we subtract its appearance by 1 and searching down by recursion. So we only use the number with appearance greater than 0.
     * Once we reached the length of the nums, we add current result into the ret list.
     * And by the time the recursion returns, we backtrack by adding back 1 to the appearance and remove the last number of current result.
     * O(n! *) time, O(n) space with consider the recursion stack. The recursion stack would consume O(n) space since the recursion would be n-level in depth where n is the length of nums.
     */
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        if (nums == null || nums.length == 0) return ret;
        Map<Integer, Integer> used = new HashMap<Integer, Integer>();//<number, appearance>
        for (int num : nums) {
            if (used.containsKey(num)) {
                used.put(num, used.get(num) + 1);
            } else {
                used.put(num, 1);
            }
        }
        permuteHelper(nums, 0, ret, new ArrayList<Integer>(), used);

        return ret;
    }

    private void permuteHelper(int[] nums, int start, List<List<Integer>> ret, List<Integer> curr, Map<Integer, Integer> used) {
        if (start == nums.length) {
            ret.add(new ArrayList<Integer>(curr));
            return;
        }

        Set<Integer> keys = used.keySet();
        for (Integer key : keys) { //iterate through the hashmap to generate permutations
            if (used.get(key) > 0) {
                used.put(key, used.get(key) - 1);
                curr.add(key);
                permuteHelper(nums, start + 1, ret, curr, used);
                curr.remove(curr.size() - 1);
                used.put(key, used.get(key) + 1);
            }
        }
    }
}



    """


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,2]
        answer = [
          [1,1,2],
          [1,2,1],
          [2,1,1]
        ]
        result = self.sol.permuteUnique(nums)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()