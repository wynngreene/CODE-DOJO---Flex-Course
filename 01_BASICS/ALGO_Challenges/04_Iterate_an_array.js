// //Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8, [-5,2,5,12] returns 14)
// function iterArr(arr) {
//     //your code here 

//     let arr = [1,2,5]

//     for(i = 0; i == arr.length; i++){
//         arr  
//     }
//     return sum; 
// }
function iterArr(arr) {
    let sum = 0;

    for(let i = 0;i < arr.length; i++){
        sum = arr[i] + sum;
    }
    console.log(sum);
}

iterArr([1,2,3]);