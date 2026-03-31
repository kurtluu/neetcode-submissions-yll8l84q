class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let l = 0;
        let r = 1;
        while (r <= nums.length) {                   
            // console.log("l: " + l + " r: " + r);
            console.log(nums.length)
            if (nums[l] == nums[r]) {
                return true;
            }
            r++;    
            
            if (r == nums.length) {
                l++;
                r = l + 1;
            }
        }
        return false;
    }
}
