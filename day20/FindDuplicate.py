class Solution:
    def findDuplicates(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        ans=[]
        while i<n:
            current_index=nums[i]-1
            if nums[i]!=nums[current_index]:
                nums[i],nums[current_index]=nums[current_index],nums[i]
            else:
                i=i+1
        for i in range(n):
            if nums[i]!=i+1:
                ans.append(nums[i])
        return ans
                
