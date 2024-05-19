/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    // Wait for both promises to resolve using Promise.all
    const [result1, result2] = await Promise.all([promise1, promise2]);
    
    // Return a new promise that resolves with the sum of the results
    return result1 + result2;
};
