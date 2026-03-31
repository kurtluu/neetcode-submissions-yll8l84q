class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
        let i = 0;

        if (s.length == 1) { //edge case odd stack
            return false;
        }

        while(i < s.length) {
            console.log("iter: " + i + " s[i]: " + s[i] + " stack: " + stack)
            if (s[i] == '{' || s[i] == '[' || s[i] == '(') {
                stack.push(s[i]);            
            } else { // assuming it's close op
                if ((s[i] == ')' && stack[stack.length - 1] == '(') || 
                    (s[i] == ']' && stack[stack.length - 1] == '[') ||
                    (s[i] == '}' && stack[stack.length - 1] == '{')
                ) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            i++;
        }
        if (stack.length > 0) {
            return false;
        } else {
            return true;
        }
    }
}
