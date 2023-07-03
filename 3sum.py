class Solution(object):
    def threeSum(self, nums):
        triplets = []
        n = len(nums)
        
        # Sorting the array
        nums.sort()
        
        for i in range(n-2):
            # Skipping duplicate values
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skipping duplicate values
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                        
        return triplets
