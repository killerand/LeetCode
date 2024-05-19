/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    let intervalId = null;
    const result = [];
    const start = performance.now(); // Define start time here

    // Function to execute fn with args and push result to result array
    const executeAndLog = () => {
        const returnedValue = fn(...args);
        const diff = Math.floor(performance.now() - start);
        result.push({ "time": diff, "returned": returnedValue });
    };

    // Execute fn immediately and start the interval
    executeAndLog();
    intervalId = setInterval(executeAndLog, t);

    // Function to cancel the interval
    const cancelFn = () => {
        if (intervalId !== null) {
            clearInterval(intervalId);
            intervalId = null;
        }
    };

    // Return the cancel function
    return cancelFn;
};