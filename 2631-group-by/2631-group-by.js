/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    // Initialize an empty object to hold the grouped results
    const grouped = {};

    // Iterate over each element in the array
    for (let i = 0; i < this.length; i++) {
        const item = this[i];
        const key = fn(item); // Get the key by applying the function to the item
        
        // If the key does not exist in the grouped object, create it
        if (!grouped[key]) {
            grouped[key] = [];
        }

        // Push the current item into the appropriate group
        grouped[key].push(item);
    }

    // Return the grouped object
    return grouped;
};