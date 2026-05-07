/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        // Instantiate the solution node and required variables.
        ListNode solNode = new ListNode(0);
        ListNode currNode = solNode;
        int carry = 0;

        // Sum up all the values in l1 and l2 into carry.
        while (carry != 0 || l1 != null || l2 != null){
            if (l1 != null){
                carry += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                carry += l2.val;
                l2 = l2.next;
            }
            // Modulus operator because the ones place would be the sum of l1 and l2.
            currNode.next = new ListNode(carry%10);
            // The tens place, if it is a 1 because l1 + l2 >= 10, will be carried forward
            // to the next node.
            carry /= 10;
            currNode = currNode.next;
        }

        // We return the next node of solution node because solution node's current
        // value is 0 when it was instantiated.
        return solNode.next;
    }
}