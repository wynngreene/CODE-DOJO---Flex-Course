// Remove Blanks | DONE!
function remove_Blanks(){
    let wordArray = "Pl ayTha tF u nkyM usi c ";
    let new_Word = wordArray.split(" ").join("");
    console.log(new_Word);
}
remove_Blanks();

// Get Digits | DONE!
function remove_Chars(){
    let my_String = "0s1a3y5w7h9a2t4?6!8?0";
    let new_String = my_String.replace(/[^0-9]/g,'');
    console.log(new_String);
}
remove_Chars();

// Acronyms | DONE!
function arconym_String(my_String){
    let string_ph_01 = my_String.split(" ");
    console.log(string_ph_01);
    let string_ph_02 = string_ph_01.map(string_First_Letter);
    console.log(string_ph_02);
    return string_ph_02.join("").toUpperCase();
};

function string_First_Letter(this_String){
    return this_String[0];
};

let string_Enter = "bilbo baggins my ring bearer."
console.log(arconym_String(string_Enter));

// Zip Arrays into Dictionary | DONE!
function zip_Array(array_01, array_02){
    let combined_Object = {};
    for (let i = 0; i < array_01.length; i++){
    combined_Object[array_01[i].toString()] = array_02[i];
    }
    return combined_Object;
}

let arr1 = ["01","02","03"];
let arr2 = ["0A","0B","0C"];

console.log(zip_Array(arr1,arr2));



// Invert Hash | DONE!
let my_Object = {
    "name": "Zaphod",
    "charm": "high",
    "morals": "dicey"
}

let swapped_Object = Object
    .fromEntries(Object.entries(my_Object)
    .map(a => a.reverse())); // Arrow function expressions!!!

console.log(swapped_Object);