import java.lang.*;

 /* Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */


//Idea for this problem is that we must perform a traversal through all the nodes.
//Summary: use recursion and keep track of the inequaility/comparison for "good nodes"
class Solution {
    public int goodNodes(TreeNode root) {
        return function(root, (int)Math.pow(10,4)*-1);
    }
    
    public int function(TreeNode root, int largest){
        int specialValue = 0;
        if (root == null){
            return 0;
        }
        else if (root.val>=largest){
            largest = root.val;
            specialValue = 1;
        }
        return specialValue + function(root.left, largest) + function (root.right, largest);
    }
}
