/**
 * @param {Array<number>} arr
 */
function sorted_squared(arr) {
  const squared_arr = arr.map((value) => value ** 2);

  return squared_arr.sort((a, b) => a - b);
}

console.log(sorted_squared([-4, -2, 4]));

/**
 *
 * @param {Array<number>} array
 */
function updated_sorted_squared(array) {
  let leftPointer = 0; // points to first element in the array
  let rightPointer = array.length - 1; // points to last element in the array
  const newArray = new Array(array.length).fill(0);

  for (let i = array.length - 1; i >= 0; i--) { // O(n)
    const left_square = array[leftPointer] ** 2;
    const right_square = array[rightPointer] ** 2;

    if (right_square >= left_square) {
      newArray[i] = right_square;
      rightPointer--;
    } else {
      newArray[i] = left_square;
      leftPointer++;
    }
  }

  return newArray;
}

console.log(updated_sorted_squared([-4, -1, 0, 1, 2, 5]));
