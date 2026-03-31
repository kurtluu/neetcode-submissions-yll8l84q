class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        let res = nums;
        nums = nums.concat(res);
        return nums;
    }
}
