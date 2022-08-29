from typing import List

from typing import List
class Solution:
    def threeSum_old(self, nums: List[int]) -> List[List[int]]:
        triplets_arr = []
        for i in range(len(nums) - 2):
            for j in range(1, len(nums) - 1):
                for k in range(2, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets_arr.append([nums[i], nums[j], nums[k]])
        return triplets_arr
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets_arr = []
        for i in range(len(nums) - 1):
            s = set()
            current_sum = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                if current_sum - nums[j] in s:
                    triplets_arr.append([nums[i], nums[j], current_sum - nums[j]])
                    continue
                s.add(nums[j])
        return triplets_arr



test_set = [ [-1,0,1,2,-1,-4], [], [5,6,4,3,0], [2,2,5,-1,-1,0,-4]]

sol = Solution()
print('first')
for el in test_set:
    print(sol.threeSum_old(el))

print('second')
for el in test_set:
    print(sol.threeSum(el))
