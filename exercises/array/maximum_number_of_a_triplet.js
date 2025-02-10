// @ts-check

/**
 *
 * @param {Array<number>} array
 */
function maximumNumberOfATriplet(array) {
  // Find first three maximum numbers

  let first = array[0];
  let second = -100_000_000;
  let third = -100_000_000_000;

  for (let i = 0; i < array.length; i++) {
    const value = array[i]

    if (value > first) {
      third = second;
      second = first;
      first = value;
    } else if (value > second) {
      third = second;
      second = value;
    } else if (value > third) {
      third = value;
    }
  }

  return first * second * third;
}

console.log(maximumNumberOfATriplet([-10, -3, -5, -6, -20]));
console.log(maximumNumberOfATriplet([10, 3, 5, 6, 20]));
console.log(maximumNumberOfATriplet([1, -4, 3, -6, 7, 0]));
