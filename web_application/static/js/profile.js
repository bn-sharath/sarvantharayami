let userID = document.getElementById("userID")
let password = document.getElementById("password")
let fname = document.getElementById("fname")
let sname = document.getElementById("sname")
let email = document.getElementById("email")
let phone = document.getElementById("phone")
let person = document.getElementById("person")
let addhar = document.getElementById("addhar")
let save = document.getElementById("save")
let error = document.getElementById("error")
let profile_image = document.getElementById("profile_image")




error.style.display = "none"

person.addEventListener("change",(event)=>{
    profile_image.src = URL.createObjectURL(event.target.files[0]);
    console.log(profile_image.src)
});

function validation() {

    if (userID.value == "" || userID.value.length <= 0 || userID.value == null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter User ID </li>"
        return false
    }
    if (password.value == "" || password.value.length <= 0 || password.value == null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter password </li>"
        return false
    }

    if (fname.value == "" || fname.value.length <= 0 || fname.value == null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter first name </li>"
        return false
    }

    if (sname.value == "" || sname.value.length <= 0 || sname.value == null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter second name </li>"
        return false
    }


    if (email.value == "" || email.value.length <= 0 || email.value == null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter Email </li>"
        return false
    }

    if (phone.value == "" || phone.value.length <= 0 || phone.value == null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter phone number </li>"
        return false
    }

    if (addhar.value == "" || addhar.value.length <= 0 || addhar.value == null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter addhar number </li>"
        return false
    }

}
