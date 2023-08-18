// Get comfortable with loops: for and while.
// Get comfortable with conditionals: if/else.

// 1. Print odds 1-20
// Using a loop write code that will console.log all of the odd values from 1 up to 20.

function printOdds() {
    for (let i = 1; i < 21; i++){
        if (i % 2 != 0)
        console.log(i);
    }
}
// printOdds();


// 2. Decreasing Multiples of 3
// Using a loop write code that will console.log all of the values that are 
// evenly divisible by 3 from 100 down to 0.

function decreaseByThree() {

    for (let i = 100; i > 0; i-- ){
        if (i % 3 == 0){
            console.log(i);
        }
    }
}
decreaseByThree()

// 3. Print the sequence
// Using a loop write code that will console.log the values in this sequence 4, 2.5, 1, -0.5, -2, -3.5.

function printSeq() {
    const myArray = [4, 2.5, 1, -0.5, -2, -3.5];
    let = currentNum = 0;
    for (i = 0; i < myArray.length; i++){

        currentNum = myArray[i];
        
        console.log(currentNum);
    }
}
// printSeq();

// 4. Sigma
// Write code that will add all of the values from 1-100 onto some variable sum and
// at the end console.log the result 1 + 2 + 3 + ... + 98 + 99 + 100. We should get back 5050 at the end.
// function addSigma() {
//     totalSum = 0;

    for (i = 1; i < 101; i++){
        totalSum = totalSum + i;
        console.log(totalSum);
    }

// addSigma();

// 5. Factorial
// Write code that will multiply all of the values from 1-12 onto some variable product and
// at the end console.log the result 1 * 2 * 3 * ... * 10 * 11 * 12. We should get back 479001600 at the end.

function multiByFive() {

    currentValue = 1;
    for(i = 1; i < 13; i++){
        currentValue = currentValue * i;
        console.log(currentValue);
    }
}
// multiByFive();