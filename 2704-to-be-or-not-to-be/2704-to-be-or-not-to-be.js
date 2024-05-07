const expect = (val) => {
    return {
        toBe: (otherVal) => {
            if (val !== otherVal) {
                throw new Error("Not Equal");
            }
            return true;
        },
        notToBe: (otherVal) => {
            if (val === otherVal) {
                throw new Error("Equal");
            }
            return true;
        }
    };
};

// Example usage:
try {
    expect(5).toBe(5); // No error, returns true
    expect(5).notToBe(10); // No error, returns true
    expect(5).toBe(10); // Throws an error: "Not Equal"
    expect(5).notToBe(5); // Throws an error: "Equal"
} catch (error) {
    console.error(error.message);
}
