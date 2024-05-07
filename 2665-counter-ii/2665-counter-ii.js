const createCounter = (init) => {
    let currentValue = init;
    
    return {
        increment: () => {
            return ++currentValue;
        },
        decrement: () => {
            return --currentValue;
        },
        reset: () => {
            currentValue = init;
            return currentValue;
        }
    };
};

// Example usage:
const counter = createCounter(5);
const calls = ["increment", "reset", "decrement"];
const result = [];

calls.forEach(call => {
    switch(call) {
        case "increment":
            result.push(counter.increment());
            break;
        case "decrement":
            result.push(counter.decrement());
            break;
        case "reset":
            result.push(counter.reset());
            break;
    }
});

console.log(result); // Output: [6, 5, 4]
