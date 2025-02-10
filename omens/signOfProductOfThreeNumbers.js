// @ts-check

/**
 * @param {number} num1
 * @param {number} num2
 * @param {number} num3
 * @returns {string} Returns -1 if the product of num1, num2, and num3 is negative, 0 if the product is zero, and 1 if the product is positive.
 * */
const signOfProductOfThreeNumbers = (num1, num2, num3) => {
  const output = num1 * num2 * num3; // O(1)

  return output < 0 ? "The sign is -ve" : "The sign is +ve";
};

console.log(signOfProductOfThreeNumbers(-1, 1, 1)); // The sign is -ve
console.log(signOfProductOfThreeNumbers(-1, 1, -1)); // The sign is +ve
console.log(signOfProductOfThreeNumbers(-1, -1, -1)); // The sign is -ve
