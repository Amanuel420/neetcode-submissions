class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr=1
        l=[1]*(len(nums))

        for i in range(len(nums)):
            l[i]=pr
            pr*=nums[i]
            
        po=1
        for j in range(len(nums)-1,-1,-1):
            l[j]*=po
            po*=nums[j]
        return l




        