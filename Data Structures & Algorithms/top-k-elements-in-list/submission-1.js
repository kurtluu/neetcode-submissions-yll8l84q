class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const hashMap = new Map();
        let result = [];

        for (let i = 0; i < nums.length; i++) {
            if (!hashMap.has(nums[i])) {
                hashMap.set(nums[i], 1);
            } else {
                hashMap.set(nums[i], hashMap.get(nums[i]) + 1);
            }
        }
        

        while (k > 0) {
            console.log(hashMap);
            let greatestValueReduce = -Infinity; // Initialize with a very small number
            let keyOfGreatestValue = null;

            hashMap.forEach((value, key) => {
                if (value > greatestValueReduce) {
                    greatestValueReduce = value;
                    keyOfGreatestValue = key;
                }
            });

            hashMap.delete(keyOfGreatestValue)
            result.push(keyOfGreatestValue);
            k--;
        }
        return result;
        
    }
}
