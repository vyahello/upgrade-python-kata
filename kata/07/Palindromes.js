/*
An array is given with palindromic and non-palindromic numbers.
A palindromic number is a number that is the same from a reversed order.
For example 122 is not a palindromic number, but 202 is one.

Your task is to write a function that returns an array with only 1s and 0s,
where all palindromic numbers are replaced with a 1 and all non-palindromic numbers are replaced with a 0.
*/

function isPalindromeString(string) {
    /**
     * Checks if string is a palindrome
     */
    return string === string.split("").reverse().join("");
}


function convertPalindromes(numbers) {
    /**
     * Converts numbers into palindrome sequence
     */
    let result = [];
    for(number of numbers) {
        if(isPalindromeString(number.toString())) {
            result.push(1);
        }
        else {
            result.push(0);
        }
    }
    return result;
}


function convertPalindromesEfficient(numbers) {
    /**
     * Converts numbers into palindrome sequence
     */
    return numbers.map(number => Number(number.toString() == number.toString().split('').reverse().join('')));
}
