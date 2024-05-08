/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    function mapWithIndex(arr, fn) {
        const mappedArray = [];
        for (let i = 0; i < arr.length; i++) {
            mappedArray.push(fn(arr[i], i));
        }
        return mappedArray;
    }

    return mapWithIndex(arr, fn);
};
