console.log("Im connected!")

// Challenge 01 - Change the Text Color and Size
function ch_01_Text_Change() {
  document.getElementById("ch_01_display_Text").style.color = "orange";
  document.getElementById("ch_01_display_Text").style.fontSize = "larger";

}

function ch_01_Text_Back() {
  document.getElementById("ch_01_display_Text").style.color = "bisque";
  document.getElementById("ch_01_display_Text").style.fontSize = "medium";
}

// Challenge 02 - Add an Image to my Div using JS.
function ch_02_Add_Image() {
  var x = document.createElement("img");
  
  x.setAttribute("src", "https://www.pexels.com/photo/little-bird-among-apple-flowers-17645795/");
  x.setAttribute("width", "200");
  x.setAttribute("height", "200");
  x.setAttribute("alt", "The Pulpit Rock");
    console.log(x);
  document.body.appendChild(x);
}

function ch_02_Add_Off() {
  
}

// Challenge 03 - Using JS show the hidden images and display them in a flex row spaced evenly.
