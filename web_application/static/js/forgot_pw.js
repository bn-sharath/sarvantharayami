let display_error_u = document.querySelector("#display-error-u")
let email = document.querySelector('#email');



display_error_u.style.display = "none"

function validate_login() {

    let return_value = true
    if (email.value == null || email.value.length <= 0 || email.value == "") {
        display_error_u.style.display = "block"

        // console.log("user-id not valid")
        display_error_u.innerHTML = "Invalid!.. email, Please enter valid email"
        return_value = false
    }
    else {
        display_error_u.style.display = "none"

    }
    if (!ValidateEmail(email)) {
        display_error_u.style.display = "block"

        // console.log("user-id not valid")
        display_error_u.innerHTML = "Invalid!.. email, Please enter valid email"
        return_value = false
    }
    else {
        display_error_u.style.display = "none"


    }
    return return_value
}

function ValidateEmail(input) {

    // var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if (input.value.match(mailformat)) {
        return true;
    } else {
        return false;

    }

}