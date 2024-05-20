class ArrayWrapper {
    /**
     * @param {number[]} nums
     */
    constructor(nums) {
        this.nums = nums;
    }

    /**
     * @return {number}
     */
    valueOf() {
        // Return the sum of all elements in the array
        return this.nums.reduce((acc, num) => acc + num, 0);
    }

    /**
     * @return {string}
     */
    toString() {
        // Return the array as a comma-separated string surrounded by brackets
        return `[${this.nums.join(',')}]`;
    }
}
