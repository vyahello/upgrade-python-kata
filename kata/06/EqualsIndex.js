/*
Given a sorted array of distinct integers, write a function index_equals_value that returns the lowest index for which
array[index] == index. Return -1 if there is no such index.

Your algorithm should be very performant.

[input] array of integers ( with 0-based nonnegative indexing )
[output] integer
*/

function indexEqualsValue(array) {
  return indexSearch(array, 0, array.length-1);
}

function indexSearch(array, low, high) {
  if(low > high) {
    return -1;
  }
  let median = Math.floor((high + low) / 2);
  if(array[median] === median) {
    let leftVal = indexSearch(array, low, median-1);
    return (leftVal !== -1 && leftVal < median) ? leftVal: median;
  }
  if(array[median] > median) {
    return indexSearch(array, low, median - 1);
  }
  return indexSearch(array, median + 1, high)
}
