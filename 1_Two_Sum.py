# https://leetcode.com/problems/two-sum

def twoSum(nums: list[int], target: int) -> list[int]:
    nums_dict = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums_dict:
            return [nums_dict[diff], i]
        nums_dict[num] = i

if __name__ == "__main__":
    nums_list = [[2,7,11,15], [3,2,4], [3,3]]
    targets_list = [9, 6, 6]
    result = [twoSum(nums_list[i], targets_list[i]) for i in range(3)]
    print(result)