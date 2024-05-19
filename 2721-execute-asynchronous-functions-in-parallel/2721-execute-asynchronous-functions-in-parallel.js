/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let count = 0;
        const totalFunctions = functions.length;

        // Iterate through each function
        functions.forEach((func, index) => {
            func().then(result => {
                results[index] = result;
                count++;
                // Check if all functions have resolved
                if (count === totalFunctions) {
                    resolve(results);
                }
            }).catch(err => {
                reject(err); // Reject if any function rejects
            });
        });
    });
};
