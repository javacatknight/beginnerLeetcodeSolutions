#Solution better formmated here: https://leetcode.com/problems/house-robber/solutions/4165890/a-guide-to-problem-solving-thinking-through-the-question/
class Solution:
    def rob(self, nums: List[int]) -> int:

#PLANNING
# Regard the constraints. Notice 0<=nums[i], i.e. all positive values => will always get more money when robbing.
# Consider this in a induction-like perspective (base case, inductive case), and consider the goal at any given house k. (Goal is to find the maxLootAtReachingThiHouse(x)).
# Inductive: At a given house k, should I rob?
# Yes - if maxLootAt(k-1) < maxLootAt(k-2) + lootAtThisHouse(k). Let's denote this as a < b + c
# No otherwise. 

#INTUITION
# It might feel like this is against intuition. Example array: [3, 53, 52]. At k=2, clearly we want b+c. But at k=3, we'll check if a' < b'+ c', and decide we do want b'+c'! And b' is in fact old a (despite us originally choosing b+c, over a). So we'll be able to correct ourselves as we go/it's okay if we "choose wrong" at one step, it self corrects.
# So let's assume this is true and to have the maxLoot at the end of the street, is the same as having the maxLoot at the last house.


#EXECUTION!
#Can solve either iteratively or recursively.
        #base cases.
        maxLootk_2 = 0 
        maxLootk_1 = nums[0]
        for i in range (1, len (nums)):
            newMaxLootk_1 = max(maxLootk_2 + nums[i], maxLootk_1) #when i+=1, this is our new k-1
            maxLootk_2 = maxLootk_1
            maxLootk_1 = newMaxLootk_1
        
        return max(maxLootk_2,maxLootk_1)
    
    # Now try the recursive approach, and the ammortizing approach.
