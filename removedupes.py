#nums | [0,0,0,1,1,1,3,3,4,5,5,6,8]
#x | 1
#i | 0
#len(nums) | 13

class Solution:
  def removeDuplicates(self, nums):
      x = 1
      for i in range(len(nums)-1):
        if(nums[i]!=nums[i+1]):
          nums[x] = nums[i+1]
          x+=1
      return(x)
      }
}
