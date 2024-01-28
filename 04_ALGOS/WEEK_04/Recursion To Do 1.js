// Recursive Sigma | DONE!
function recursive_Sigma(number) {
    if (number > 0) {
        return number + recursive_Sigma(number - 1);
    } else {
        return 0;
    }
}
console.log(recursive_Sigma(6));


// Recursive Factorial | DONE!
function recursive_Factorial(number) {
    if (number > 1) {
        return number * recursive_Factorial(number - 1);
    } else {
        return 1;
    }
}
console.log(recursive_Factorial(5));