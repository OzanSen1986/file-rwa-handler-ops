'''Product of Array Except Self
Given an integer array nums, return an array answer where answer[i] equals product of all elements except nums[i].
Example:
Input: [1,2,3,4] → Output: [24,12,8,6]'''


def productExceptSelf(nums: list[int] = [1,2,3,4]):
    n = len(nums) #4
    result = [1] * n # [1, 1, 1, 1]

    # Build prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Multiply with suffix products
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result








