/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (Array.isArray(obj)) {
        // Check if array is empty
        return obj.length === 0;
    } else if (typeof obj === 'object' && obj !== null) {
        // Check if object is empty
        return Object.keys(obj).length === 0;
    }
    // If obj is neither an array nor an object (although not expected per problem statement)
    return false;
};
