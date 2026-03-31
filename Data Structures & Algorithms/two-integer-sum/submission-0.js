class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hashMap = new Map();
        for(let i = 0; i < nums.length; i++) {
            let complement = target - nums[i];
            
            console.log(i + " complement: " + complement)
            if (hashMap.has(target - complement)) {
                return [hashMap.get(target - complement), i]
            } else {
                hashMap.set(complement, i);
            }
        }
        
        console.log(hashMap)
        return [];
    }
}
