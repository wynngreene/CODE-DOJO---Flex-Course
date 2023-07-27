// Magic function so that I don't have to misspell console.log I can just type print
function print(a,num) {
    console.log("printing line", num, a)
}
print('I am connected', 5)

let colorSize = document.getElementById('h4Style')
// var colorSize is now equal to = hey html find id h4Style
// print(colorSize, 8)
function h4Style() {
    colorSize.style.color = 'pink'
    colorSize.style.fontSize = '3em'
}
let img = document.getElementById('addImg')
function addImg() {
    // let theImg = document.createElement('img')
    let theImg = new Image()
    theImg.src = './images/DSCN1100.JPG'
    theImg.alt = 'An Img'
    img.appendChild(theImg)
}

function stringAlert() {
    alert("I am a string")
}

// alert("I am a very very very very very large string")

let x = 0
let span = document.getElementById('like')
function likeMe() {
    x++
    print(x,32)
    span.innerText = x
}

let answer = document.getElementById('add')
function adding(a,b) {
    let sum = a + b
    console.log(sum)
    answer.innerText = sum
}
function adding02() {
    var n01 = document.form01.num01.value
    var n02 = document.form01.num02.value
    answer = document.getElementById('add')
    let sum = n02 + n01
    console.log('work',sum, n02, n01)
    answer.innerText = sum
}
