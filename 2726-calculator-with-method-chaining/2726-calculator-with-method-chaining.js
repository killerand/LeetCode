class Calculator {
    /**
     * @param {number} value - The initial value of the calculator
     */
    constructor(value) {
        this.result = value;
    }
    
    /**
     * Adds the given value to the result
     * @param {number} value
     * @return {Calculator}
     */
    add(value) {
        this.result += value;
        return this;
    }
    
    /**
     * Subtracts the given value from the result
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value) {
        this.result -= value;
        return this;
    }
    
    /**
     * Multiplies the result by the given value
     * @param {number} value
     * @return {Calculator}
     */
    multiply(value) {
        this.result *= value;
        return this;
    }
    
    /**
     * Divides the result by the given value
     * @param {number} value
     * @return {Calculator}
     * @throws {Error} Division by zero is not allowed
     */
    divide(value) {
        if (value === 0) {
            throw new Error("Division by zero is not allowed");
        }
        this.result /= value;
        return this;
    }
    
    /**
     * Raises the result to the power of the given value
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        this.result = Math.pow(this.result, value);
        return this;
    }
    
    /**
     * Returns the result
     * @return {number}
     */
    getResult() {
        return this.result;
    }
}