def mergesort(nums):
    if not nums or len(nums)==1:
        return
    msort_helper(nums, 0, len(nums)-1)

def msort_helper(nums, l, r):
    if l >= r:
        return
    mid = l + int((r-l)/2)
    msort_helper(nums, l, mid)
    msort_helper(nums, mid+1, r)
    merge(nums, l, mid, r)

def merge(nums, l, m, r):
    if l == m and m == r:
        return
    tmp = []
    i, j = l, m+1
    while i < m+1 and j < r+1:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    if i < m+1:
        tmp.extend(nums[i:m+1])
    else:
        tmp.extend(nums[j:r+1])
    nums[l:r+1] = tmp

if __name__ == '__main__':
    nums = [1,3,5,6,2,4,3]
    mergesort(nums)
    print(nums)