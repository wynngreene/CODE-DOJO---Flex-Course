//Given an array with multiple values, write a function that replaces each value in the array with the product of the original value multiplied by itself.
//(e.g. [1,5,10,-2] will become [1,25,100,4])

function squareVal(arr) {
    let holdMe = 0;

    for(let i = 0; i < arr.length; i++){
        holdMe = arr[i]*arr[i];
        arr[i] = holdMe;
    }
    console.log(arr);

}

squareVal([1,3,5,7,9])