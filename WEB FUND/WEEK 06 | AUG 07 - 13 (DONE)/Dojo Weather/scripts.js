console.log("connected");

function btn_city(element) {
    window.alert("Loading weather report...");
}

function btn_cookie_hidden(element){
    var x = document.getElementById("alert_cookie");
    x.style.display = "none";

}

function btn_change_temp() {
    let selected_option = document.getElementById("change_temp").value;

    if (selected_option = "option_f"){
        document.getElementById("red_today").innerHTML = "75°";
        document.getElementById("blue_today").innerHTML = "65°";

        document.getElementById("red_tomorrow").innerHTML = "80°";
        document.getElementById("blue_tomorrow").innerHTML = "66°";

        document.getElementById("red_friday").innerHTML = "69°";
        document.getElementById("blue_friday").innerHTML = "61°";

        document.getElementById("red_saturday").innerHTML = "78°";
        document.getElementById("blue_saturday").innerHTML = "70°";

        console.log("temp in F");
    }

    else if (selected_option = "option_c"){
        document.getElementById("red_today").innerHTML = "24°";
        document.getElementById("blue_today").innerHTML = "18°";

        document.getElementById("red_tomorrow").innerHTML = "27°";
        document.getElementById("blue_tomorrow").innerHTML = "19°";

        document.getElementById("red_friday").innerHTML = "21°";
        document.getElementById("blue_friday").innerHTML = "16°";

        document.getElementById("red_saturday").innerHTML = "26°";
        document.getElementById("blue_saturday").innerHTML = "21°";

        console.log("Temp in C");
    }
    else {
        console.log("temp is NOPE");
    }
}