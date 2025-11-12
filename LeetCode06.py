'''Given an integer array nums and an integer k, return the k most 
frequent elements in the array.
Input:
nums = [1,1,1,2,2,3], k = 2

Output:
[1, 2]
Explanation:
1 appears 3 times
2 appears 2 times
3 appears 1 time
So the two most frequent are: [1, 2].
'''

def topKFrequent(nums: list[int], k: int) -> list[int]:
    result = {}
    for num in nums:
        result[num] = result.get(num,0) + 1
    sorted_list = sorted(result.items(), key=lambda x:x[1], reverse=True)
    return [num for num, count in sorted_list[:k]]


print(topKFrequent(nums=[1, 3, 3, 3, 1, 1, 4, 4, 4, 4, 4, 2, 2], k=2))









