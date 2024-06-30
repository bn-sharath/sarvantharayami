let password = document.querySelector('#password');
let password_visible = document.querySelector('#password_visible')
let submit = document.getElementById("submit");
let login_form = document.getElementById("login-form");
let user_id = document.getElementById("user-id");
let display_error_u = document.querySelector("#display-error-u")
let display_error_p = document.querySelector("#display-error-p")
// let password = document.getElementById("password");


display_error_u.style.display = "none"
display_error_p.style.display = "none"


password_visible.addEventListener("click", function () {
    if (password.type == "password") {
        password.type = "text";
        // console.log(password_visible.src)
        password_visible.src = "static/media/off.svg";
        // console.log(password_visible.src)

    }
    else {
        password.type = "password";
        // console.log(password_visible.src)
        password_visible.src = "static/media/on.svg";
        // console.log(password_visible.src)

    }
});
function validate_login() {

    console.log("working")

    let return_value = true
    if (user_id.value == null || user_id.value.length <= 0 || user_id.value == "") {
        display_error_u.style.display = "block"

        console.log("user-id not valid")
        display_error_u.innerHTML = "Invalid!.. User Id, Please enter valid User Id"
        return_value = false
    }
    else {
        display_error_u.style.display = "none"

    }
    if (password.value == null || password.value.length <= 0 || password.value == "") {
        display_error_p.style.display = "block"

        display_error_p.innerHTML = "Invalid!.. password, Please enter valid passwword"
        console.log("password not valid")
        return_value = false
    }
    else {
        display_error_p.style.display = "none"


    }
    if (!validateUserID(user_id)) {
        display_error_u.style.display = "block"

        console.log("user-id not valid")
        display_error_u.innerHTML = "Invalid!.. User Id, Please enter valid User Id"
        return_value = false

    }
    else {
        display_error_u.style.display = "none"
    }

    if (!CheckPassword(password)) {
        display_error_p.style.display = "block"

        display_error_p.innerHTML = "Invalid!.. password, Please enter valid passwword"
        console.log("password not valid")
        return_value = false

    }
    else {
        display_error_p.style.display = "none"
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

function validateUserID(inputtxt) {
    var userID = /^[A-Za-z]\w{7,14}$/;
    if (inputtxt.value.match(userID)) {
        // alert('Correct,')
        return true;
    }
    else {
        // alert('Wrong...!')
        return false;
    }
}

