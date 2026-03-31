class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hasSet = new Set();
        for (let i = 0; i < nums.length; i++) {
            if (!hasSet.has(nums[i])) {
                hasSet.add(nums[i]);
            } else {
                return true;
            }
        }
        return false;
    }
}
