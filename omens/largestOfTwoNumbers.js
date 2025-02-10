// @ts-check

/**
 *
 * @param {number} num1
 * @param {number} num2
 * @returns {number} The largest of two numbers
 */
const largestOfTwoNumbers = (num1, num2) => {
  if (num1 > num2) {
    return num1;
  }

  return num2;
};

console.log(largestOfTwoNumbers(5, 10)); // 10
console.log(largestOfTwoNumbers(-5, -2)); // -2
console.log(largestOfTwoNumbers(5, 5)); // 5
