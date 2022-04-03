def findSplitPoint(nums):
    sums = sum(nums)
    left, right = 0, sums
    for i in range(len(nums)):
        if left == right:
            return nums[:i], nums[i:]
        left += nums[i]
        right -= nums[i]
    return (nums, []) if left == right else None


def findCutTwo(nums):
    left = 0
    right = len(nums) - 1
    sum_left = nums[left]
    sum_right = nums[right]
    while left <= right:
        if sum_right < sum_left:
            right -= 1
            sum_right += nums[right]
        elif sum_left < sum_right:
            left += 1
            sum_left += nums[left]
        else:
            right -= 1
            left += 1
            sum_right += nums[right]
            sum_left += nums[left]
    return (nums[:left+1], nums[right:]) if sum_left == sum_right else None

if __name__ == "__main__":
    print(findCutTwo([2, 3, 5, 0]))
