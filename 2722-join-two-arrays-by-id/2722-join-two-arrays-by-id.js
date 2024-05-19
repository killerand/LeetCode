/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const map = new Map();

    // Helper function to add objects to the map
    const addToMap = (arr) => {
        for (const obj of arr) {
            const id = obj.id;
            if (!map.has(id)) {
                map.set(id, {...obj});
            } else {
                map.set(id, {...map.get(id), ...obj});
            }
        }
    };

    // Add objects from arr1 and arr2 to the map
    addToMap(arr1);
    addToMap(arr2);

    // Convert map values to array and sort by id
    const resultArray = Array.from(map.values());
    resultArray.sort((a, b) => a.id - b.id);

    return resultArray;
};
