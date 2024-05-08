/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  function reduceCustom(nums, fn, init) {
    let result = init;

    for (let i = 0; i < nums.length; i++) {
      result = fn(result, nums[i]);
    }

    return result;
  }

  return nums.length === 0 ? init : reduceCustom(nums, fn, init);
};
