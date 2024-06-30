let form_add = document.querySelector(".box .form-element label input")
let display_validity = document.getElementById("invalid")

display_validity.display = "none"

function validate(){
    let return_value = true
    display_validity.display = "none"
    if (form_add.value == null || form_add.value.length <=0 || form_add.value == ""){
        return_value= false
        display_validity.display = "block"

        display_validity.innerHTML = "please enter valide CCTV camera ip address"
    }


    return return_value
}