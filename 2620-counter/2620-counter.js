var createCounter = function(n) {
    return function() {
        return n++;
    };
};

var counter = createCounter(10);

var calls = ["call","call","call"];
var result = [];
for (var i = 0; i < calls.length; i++) {
    if (calls[i] === "call") {
        result.push(counter());
    }
}

console.log(result); // Output: [10, 11, 12]
