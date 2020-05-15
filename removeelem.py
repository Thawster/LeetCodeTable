#nums | [2,1,3,2,4,6,8,2,]
#val | 2
#start | 0
#end | len(nums) | 8

def removeElement(self, nums, val):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], end - 1
        else:
            start +=1
    return start
