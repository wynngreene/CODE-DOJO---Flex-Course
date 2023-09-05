//Write a function that returns an array with all the numbers from 1 to 255. You may use the push() function for this exercise.
// function get_array(startNumb,finishNumb) {
//     var arr = [];
//     for (var i = startNumb ; i = finishNumb; i++)
//     {
//         arr += arr.push(i);
//     }
//     return arr;
// };
// console.log(get_array(2,10));

function get_array() {
    let arr = [];
    let numbEnd = 10;

    for(let i = 1; i < numbEnd; i++){
        i = arr.push(i);

    }
    console.log(arr);

}
get_array();