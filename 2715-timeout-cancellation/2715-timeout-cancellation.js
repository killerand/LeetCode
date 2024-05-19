/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    let timeoutId = null;

    // Function to execute fn with args after t milliseconds
    const delayedExecution = () => {
        timeoutId = setTimeout(() => {
            fn(...args);
        }, t);
    };

    // Function to cancel the delayed execution
    const cancelFn = () => {
        if (timeoutId) {
            clearTimeout(timeoutId);
            timeoutId = null;
        }
    };

    // Schedule delayed execution
    delayedExecution();

    // Return the cancel function
    return cancelFn;
};

// Example usage
const result = [];
const fn = (x) => x * 5;
const args = [2];
const t = 20;
const cancelTimeMs = 50;

const start = performance.now();

const log = (...argsArr) => {
    const diff = Math.floor(performance.now() - start);
    result.push({ "time": diff, "returned": fn(...argsArr) });
};

const cancelFn = cancellable(log, args, t);

setTimeout(cancelFn, cancelTimeMs);

setTimeout(() => {
    console.log(result); // [{"time":20,"returned":10}]
}, Math.max(t, cancelTimeMs) + 15);