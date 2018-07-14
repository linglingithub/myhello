
"""
give a list of bags, containing the amount of gold

two players can take turns to take a bag from either end of the list of bags
find out the max gold the first player can get.

two players are using the same strategy to get the bag, both want to
maximize the gold they can get

basic idea:

supose func is the function that will calc the max gold of a first player given a list of bags
func(l, r) = max (
    bags[l] + sums[l+ 1, r] - func(l+1, r),
    bags[r] + sums[l, r - 1] - func(l, r - 1))

sums[x, y] can be obtained by getting values from both sides



"""
def max_gold(bags):
    _cache = {}
    _sums = _process_sums(bags)
    _process_cache(bags, _cache)
    return _helper(bags, 0, len(bags) - 1, _cache, _sums)

def _helper(bags, left, right, cache, sums):
    if (left, right) in cache:
        return cache[(left, right)]
    take_left = bags[left] + sums[(left + 1,right)] - _helper(bags, left + 1, right, cache, sums)
    take_right = bags[right] + sums[(left, right - 1)] - _helper(bags, left, right - 1, cache, sums)
    cache[(left, right)] = max(take_left, take_right)
    return cache[(left, right)]

def _process_cache(bags, cache):
    # single item left
    for i in range(len(bags)):
        cache[(i, i)] = bags[i]
    # two items left
    for i in range(len(bags) - 1):
        cache[(i, i + 1)] = max(bags[i], bags[i + 1])
    # three items left -- can already apply complex one, no need to do
    return cache

def _process_sums(bags):
    prefix_sum = [x for x in bags]
    for i in range(1, len(bags)):
        prefix_sum[i] += prefix_sum[i - 1]
    prefix_sum.insert(0, 0)
    # now sums[0, n - 1] -- prefix[n] - prefix[0]
    sums = {}
    for i in range(len(bags)):
        for j in range(i, len(bags)):
            sums[(i, j)] = prefix_sum[j + 1] - prefix_sum[i]
    return sums





bags1 = [1, 2, 23, 4]   # 24
bags = [1, 2, 3, 4] # 4 + 2 = 6

print(max_gold(bags))