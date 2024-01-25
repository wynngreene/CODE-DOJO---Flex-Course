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

// Acronyms
// function change_Chars(){
//     let my_String = "Fear of Missing Out";
//     let new_String = my_String
//     .split(" ")
//     .map(my_String.charAt(0).toUpperCase())
//     .join("");
//     console.log(new_String);
// };
// change_Chars();

// Zip Arrays into Dictionary

// arr1 = ["abc", 3, "yo"]
// arr2 = [42, "wassup", true]
// return {"abc": 42, 3: "wassup", "yo": true}

function zip_Array(array_1, array_2){

}

//zip_Array(["abc", 3, "yo"], [42, "wassup", true]);

// Invert Hash

// Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}
// return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}