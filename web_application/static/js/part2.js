// let gov = document.getElementById("gov");
// let public = document.getElementById("public");
// let private = document.getElementById("private");
// let general = document.getElementById("general");
let gov_form = document.getElementById("gov-form");
let public_form = document.getElementById("public-form");
let private_form = document.getElementById("private-form");
let general_form = document.getElementById("general-form");
let display_error_u = document.getElementById("display-error-u");

let form_container = document.querySelector(".form-container .container");


function validation() {
      display_error_u.innerHTML = "";
      return_value = true
    // let otp_control = form_control.getElementsByName("otp")
      let elemets = document.querySelectorAll(".input-set input");
      elemets.forEach((element) => {
        if (
          element.value == null ||
          element.value.length <= 0 ||
          element.value == ""
        ) {
          display_error_u.style.display = "block";
          display_error_u.innerHTML +=
            "<li>input is empty please " + element.placeholder + "</li>";
            return_value=false

        }
        
      })
    //   console.log(otpValidation(otp_control));
    return return_value;

    // console.dir(elemets.name)
}

function otpValidation(inputtxt) {
    var otp = /^\d{6}$/;
    if (inputtxt.value.match(otp)) {
        return true;
    } else {
        // alert("message");
        return false;
    }
}
