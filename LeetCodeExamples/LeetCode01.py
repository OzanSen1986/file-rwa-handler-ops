
# def twoSum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         need = target - num
#         if need in seen:
#             return [seen[need], i]
#         seen[num] = i

# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))


# [True, True, True]

# My solution
def Anagram(s: str, t: str) ->bool:
    if len(s) != len(t):
        return f'{s} and {t} does not have equal lenghts'
    
    count = {}
    for char in s:
       count[char] = count.get(char,0) + 1
    
    for char in t:
        if char not in count or count[char] ==0:
            return False
        count[char] -=1
    return True

print(Anagram(s='madam', t='damam'))
