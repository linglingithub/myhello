"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner lists elements must follow the lexicographic order.

=== should give examples like this
["eqdf", qcpr]
((q-e) + 26) % 26=12,((d-q)+26) % 26 = 13, ((f - d) + 26) % 26 = 2
((c - q) + 26) % 26= 12, ((p - c) + 26) % 26 = 13, ((r - p) + 26) % 26 = 2
so "eqdf" and "qcpr" are the grouped shifted strings
"""


import collections

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strings:
            shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
            d[shift].append(s)

        # return d.values()
        return map(sorted, d.values())

if __name__ == '__main__':
    sol = Solution()
    pro_list = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    result = sol.groupStrings(pro_list)
    print result


