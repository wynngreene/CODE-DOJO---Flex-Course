console.log("connected_outside");

// function myColorChangeInside(color_02){
//     console.log("connected_inside");
//     document.getElementById("change_color").innerHTML = "<div class='box' id='change_color'>BOX</div>";
// }

// function myFunction() {
//     const box_color = document.getElementById("change_color");
//     let new_html = "<div class='box' id='change_color'>BOX</div>";
//     box_color.insertAdjacentHTML("afterend", new_html);
// }

function myFunction() {
    // Get the String color
    let new_color = document.getElementById("find_color").innerHTML;
    let new_number = document.getElementById("find_number").innerHTML;
    console.log(new_color);
    console.log(new_number);
    // Get the boxes
    let all_boxes = document.getElementById("container").querySelectorAll(".box");
    console.log(all_boxes);
    for(var i = 0; i < new_number; i++){
        all_boxes[i].style.backgroundColor = new_color;
    }
}