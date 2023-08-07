// console.log("connected!!!")

let count_Likes_neil = 1;
let count_Likes_nichole = 2;
let count_Likes_jim = 3;

let count_Element_1 = document.querySelector("#count_Likes_neil");
let count_Element_2 = document.querySelector("#count_Likes_nichole");
let count_Element_3 = document.querySelector("#count_Likes_jim");

function btn_Add_neil() {
    count_Likes_neil++ ;
    count_Element_1.innerText = count_Likes_neil + " Like(s)";
    console.log("my count is " + count_Likes_neil);
    
}

function btn_Add_nichole() {
    count_Likes_nichole++ ;
    count_Element_2.innerText = count_Likes_nichole + " Like(s)";
    console.log("my count is " + count_Likes_nichole);
    
}

function btn_Add_jim() {
    count_Likes_jim++ ;
    count_Element_3.innerText = count_Likes_jim + " Like(s)";
    console.log("my count is " + count_Likes_jim);
    
}