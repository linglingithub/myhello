
import unittest

/**
Move 0s To The End I
Given an array of integers, move all the 0s to the right end of the array.

The relative order of the elements in the original array does not need to be maintained.

Assumptions:

The given array is not null.
Examples:

{1} --> {1}
{1, 0, 3, 0, 1} --> {1, 3, 1, 0, 0} or {1, 1, 3, 0, 0} or {3, 1, 1, 0, 0}

*/


public class Solution {
    public int[] moveZero(int[] array) {
        // Write your solution here.
        if(array == null || array.length() <= 1){
            return array;
        }
        int i = 0;
        int j = array.length() - 1;
        while(i <= j){
            if(array[i] == 0){
                int tmp = array[j];
                array[j] = array[i];
                array[i] = tmp;
                j--;
            }else{
                i++;
            }
        }
        return array;
    }


    public static void main(String [ ] args){
        Solution sol = new Solution();
        arr = sol.moveZero([0, -1, 1, 9, 0, 2]);
        System.out.println(arr);
    }

}



