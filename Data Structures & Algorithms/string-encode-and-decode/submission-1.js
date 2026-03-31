class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let str ="";
        for (let i = 0; i < strs.length; i++) {
            str += strs[i] + "|";
        }
        return str;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        console.log(str);
        const currStr = "";
        const strs = [];
        str.split("|").forEach( currStr => {
            strs.push(currStr);
        });
        strs.pop();
        return strs;
    }
}
