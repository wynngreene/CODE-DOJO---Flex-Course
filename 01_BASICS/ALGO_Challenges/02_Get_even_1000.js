//Write a function that would get the sum of all the even numbers from 1 to 1000. You may use a modulus operator for this exercise.
// function sum_even_numbers(){
//     var sum = 0;
//     //your code here
//     let myEvenArray[];
    
//     for (i = 0; sum >= 10; i++)
//         if (myArray.(i) % 2 = 0){
//             myArray.[] = i;
//         }
//     return sum; 
// }

function sum_even_number(){
    var sum = 0;
    let number_end = 1001;

    for(i = 1; i < number_end; i++){
        if(i % 2 == 0){
        sum = i + sum;
        }
    }
    console.log(sum);
}

sum_even_number();