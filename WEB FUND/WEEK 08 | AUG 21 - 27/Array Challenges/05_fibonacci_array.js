//DONE

function fibonacciArray(n) {

    var fibArr = [0, 1];

    for (let i = 0; i < n; i++){
        fibArr[i+2] = fibArr[i] + fibArr[i + 1];
    }
    console.log(fibArr);
    return fibArr;
}
// var result = fibonacciArray(10);
// console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
fibonacciArray(10);