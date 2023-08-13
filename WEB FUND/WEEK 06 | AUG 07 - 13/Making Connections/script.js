console.log("page loaded...");

// Edit button to change name

let edit_name = document.querySelector("#edit_user_name");

function btn_change_name(){
    
    console.log(edit_name);
    edit_name.innerText = "Bilbo Baggins";


}

document.getElementById("hidden_todd").style.visibility = "hidden";
document.getElementById("hidden_phil").style.visibility = "hidden";

var display_count_request = document.querySelector("#count_request");
var display_count_connect = document.querySelector("#count_connect");

let current_count_request = 2;
let current_count_connect = 418;

// JS for User Todd
function btn_accept_1(element) {
    var remove_User = document.getElementById("user_todd");
    remove_User.remove();

    current_count_request--;
    display_count_request.innerText = current_count_request;

    current_count_connect++;
    display_count_connect.innerText = current_count_connect;

    document.getElementById("hidden_todd").style.visibility = "visible";
}

function btn_close_1(element) {
        var remove_User = document.getElementById("user_todd");
    remove_User.remove();

    current_count_request--;
    display_count_request.innerText = current_count_request;

}

// JS for User Phil
function btn_accept_2(element) {
    var remove_User = document.getElementById("user_phil");
    remove_User.remove();

    current_count_request--;
    display_count_request.innerText = current_count_request;

    current_count_connect++;
    display_count_connect.innerText = current_count_connect;

    document.getElementById("hidden_phil").style.visibility = "visible";
}

function btn_close_2(element) {
        var remove_User = document.getElementById("user_phil");
    remove_User.remove();

    current_count_request--;
    display_count_request.innerText = current_count_request;

}




