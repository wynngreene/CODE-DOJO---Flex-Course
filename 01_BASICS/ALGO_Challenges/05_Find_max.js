// //Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
// function findMax(arr) {
//     max = 0;
//         //your code here 
//     for (i=0: i == arr.length; i++){
//         arr[i] + max;
//     }
//     return max; 
// }

// function findMax(arr){
//     let max = 0;

//     for(let i = 0; i < arr.length; i++){
//         max = arr[i] + max;
//     }
//     arr.push(max);
//     console.log(arr.length);

// }

// findMax([1,2,3]);

// function findMax(arr) {
//     let max = 0;
//     let currentLength = 0;

//     currentLength = arr.length;
//     console.log(currentLength);

//     max = arr[currentLength - 1];

//     console.log(max);

// }
// findMax([1,2,3,4,5,6,212]);

function findMax(arr) {
    let max = 0;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
    console.log(max);
}
findMax([1,5,12,7,3,8,1])