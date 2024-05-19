/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    // Initialize the result array
    const chunkedArray = [];
    
    // Loop through the array, incrementing by the chunk size
    for (let i = 0; i < arr.length; i += size) {
        // Slice the array from the current index to the current index + size
        const chunk = arr.slice(i, i + size);
        // Push the chunk into the result array
        chunkedArray.push(chunk);
    }
    
    // Return the chunked array
    return chunkedArray;
};
