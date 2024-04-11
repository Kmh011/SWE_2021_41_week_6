from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    num = {}
    for i in range(len(nums)):
        n = target - nums[i]
        if n in num:
            return [num[n], i]
        num[nums[i]] = i
    return []


nums_input = input("nums = ")
nums = [int(num) for num in nums_input.split()]
target = int(input("target = "))

result = two_sum(nums, target)
print(result)