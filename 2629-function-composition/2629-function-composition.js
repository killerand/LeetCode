/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        if (functions.length === 0) {
            // If the list of functions is empty, return the identity function
            return x;
        } else {
            // Define the composed function recursively
            let result = x;
            for (let i = functions.length - 1; i >= 0; i--) {
                result = functions[i](result);
            }
            return result;
        }
    }
};

