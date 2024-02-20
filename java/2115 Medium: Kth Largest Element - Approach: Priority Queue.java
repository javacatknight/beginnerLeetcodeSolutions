import java.util.*;
// Heapsort Priority Queue 
// Store all [1st,2nd,...kth] largest numbers
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue <Integer> q = new PriorityQueue <Integer> ();
        for (int i =0; i<k; i++){
            q.add(nums[i]);
        }

        for (int z=k; z<nums.length; z++){
            if (q.peek() < nums[z]){
                q.poll();
                q.add(nums[z]);
            }
        }
        return q.poll();
        
    } 

}
