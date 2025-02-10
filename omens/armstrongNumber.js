// @ts-check

/**
 *
 * @param {number} num
 * @returns {boolean} Returns true if a number is an armstrong number and false if it is not.
 */
const armstrongNumber = (num) => {
  // Type cast to a string;

  const strNum = String(num);
  let result = 0;

  // Loop through the string number and get the cube

  for (let i = 0; i < strNum.length; i++) {
    result += Number(strNum[i]) ** 3;
  }

  return result === num;
};


console.log(armstrongNumber(371))
console.log(armstrongNumber(101))
