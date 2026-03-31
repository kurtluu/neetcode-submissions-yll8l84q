class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {       
        const cleanedS = s.replace(/[^a-zA-Z0-9\s]/g, '').toLocaleLowerCase().replace(/\s/g, ""); 

        let l = 0;
        let r = cleanedS.length - 1;

        console.log(cleanedS);

        while(l < r) {
            console.log(cleanedS[l] + " " + cleanedS[r])
            if(cleanedS[l] != cleanedS[r]) {
                return false;
            }            
            l++;
            r--;
        }
        return true;
    }
}
