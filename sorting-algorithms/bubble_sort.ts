/**
 *
 * @param array
 * @description Sort an array using bubble sort algorithm
 * @returns The sorted array
 */
function bubbleSort(array: Array<number>): Array<number> {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length - i - 1; j++) {
      // swap elements if current index is greater than next index

      if (array[j] > array[j + 1]) {
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }

  return array;
}
