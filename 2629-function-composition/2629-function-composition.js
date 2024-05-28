/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        // Apply each function from right to left
        return functions.reduceRight((acc, fn) => fn(acc), x);
    }
};