//Given an array with multiple values,write a function that returns the average of the values in the array.
//(e.g. for [1,3,5,7,20] average is 7.2)
let max = 0;
let averageArr = 0;

function findMax(arr) {
    for (i=0; i == arr.length; i++){
    max = arr[i] + max;

    }
    averageArr = max
    //your code here 
    return max; 
}
