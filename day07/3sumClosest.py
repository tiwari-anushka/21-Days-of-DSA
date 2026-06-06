class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        num=sorted(nums)
        ans={}
        for i in range(0,len(num)):
            left=i+1
            right=len(num)-1
            while left<right:
                current_sum=num[i]+num[left]+num[right]
                if current_sum==target:
                    return target
                ans[current_sum]=abs(target-(current_sum))
                if current_sum<target:
                    left+=1
                else:
                    right-=1
        return min(ans, key=ans.get)
