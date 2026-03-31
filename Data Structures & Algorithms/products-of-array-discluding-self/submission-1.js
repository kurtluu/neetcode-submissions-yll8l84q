class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        
        const prodNums = [];
        for (let i = 0; i < nums.length; i++) {
            let currProd = 1;
            for (let j = 0; j < nums.length; j++) {
                if (j != i) {
                    currProd = currProd * nums[j];
                }
            }
            prodNums.push(currProd); 
        }
        return prodNums;
    }
}
