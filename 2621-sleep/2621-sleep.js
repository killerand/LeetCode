/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    // Return a promise that resolves after millis milliseconds
    return new Promise(resolve => {
        setTimeout(resolve, millis);
    });
}