//Create a function that filters out negative numbers
const numbers = [1, 0, 34, 7, -5, 24, -50, 8, -20, 0.65];
function negativeNumber(num) {
    return num < 0;
}
console.log(numbers.filter(negativeNumber));
