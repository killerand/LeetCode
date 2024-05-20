/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        // If the input is an array, process it as an array
        return obj.reduce((acc, item) => {
            // Recursively compact each item in the array
            let compactedItem = compactObject(item);
            if (Boolean(compactedItem)) {
                // Only add truthy items to the result array
                acc.push(compactedItem);
            }
            return acc;
        }, []);
    } else if (obj !== null && typeof obj === 'object') {
        // If the input is an object, process it as an object
        return Object.keys(obj).reduce((acc, key) => {
            let value = obj[key];
            let compactedValue = compactObject(value);
            if (Boolean(compactedValue)) {
                // Only add truthy values to the result object
                acc[key] = compactedValue;
            }
            return acc;
        }, {});
    }
    // For primitive values, return the value as is if it's truthy
    return obj;
};