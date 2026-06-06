class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        num=sorted(nums)
       
        for i in range(0,len(num)):
            if i > 0 and num[i] == num[i-1]:
                continue
            left=i+1
            right=len(num)-1
            while left<right:
                if num[i]+num[left]+num[right]==0:
                    res=sorted([num[i],num[left],num[right]])
                    ans.append(res)
                    while left < right and num[left] == num[left + 1]:
                        left += 1
                    while left < right and num[right] == num[right - 1]:
                        right -= 1
                    left+=1
                    right-=1
                elif num[i]+num[left]+num[right]<0:
                    left+=1
                else:
                    right-=1
        return ans
