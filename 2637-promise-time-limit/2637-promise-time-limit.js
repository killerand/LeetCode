/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        // Create a promise that resolves after t milliseconds
        const timeoutPromise = new Promise((resolve, reject) => {
            setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
        });

        try {
            // Race between the execution of fn and the timeout promise
            const result = await Promise.race([fn(...args), timeoutPromise]);
            return result;
        } catch (err) {
            throw err;
        }
    };
};