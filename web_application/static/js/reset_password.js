let display_error_u = document.querySelector("#display-error-u")
let password = document.querySelector('#password');
let confirm_passowd = document.querySelector('#confirm-password');



display_error_u.style.display = "none"

function validate_login() {

    let return_value = true
    if (password.value == null || password.value.length <= 0 || password.value == "") {
        display_error_u.style.display = "block"

        // console.log("user-id not valid")
        display_error_u.innerHTML = "Invalid!.. password is empty, Please enter valid password"
        return_value = false
    }
    else {
        display_error_u.style.display = "none"

    }
    if (password.value != confirm_passowd.value) {
        display_error_u.style.display = "block"

        // console.log("user-id not valid")
        display_error_u.innerHTML = "Invalid!.. confirm password is incorrect, password and confirm passowrd are not same Please"
        return_value = false

    } else {
        display_error_u.style.display = "none"

    }
    if (!CheckPassword(password)) {
        display_error_u.style.display = "block"

        // console.log("user-id not valid")
        display_error_u.innerHTML = "Invalid!.. password, Please enter valid password of " + "between 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character"
        return_value = false
    }
    else {
        display_error_u.style.display = "none"


    }
    return return_value
}



function CheckPassword(inputtxt) {
    var decimal = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    if (inputtxt.value.match(decimal)) {
        // alert('Correct, try another...')
        return true;
    }
    else {
        // alert('Wrong...!')
        return false;
    }
}