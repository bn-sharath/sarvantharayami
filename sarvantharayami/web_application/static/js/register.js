let form_input = document.querySelectorAll(".form-input");
let previous = document.getElementById("previous");
let next = document.getElementById("next");
let body = document.querySelector("body");
var index;
let start = true;


// showing the data
let r_profile = document.getElementById('r-profile');
let r_fname = document.getElementById('r-fname');
let r_sname = document.getElementById('r-sname');
let r_email = document.getElementById('r-email');
let r_phone = document.getElementById('r-phone');
let r_address = document.getElementById('r-address');
let r_addhar = document.getElementById('r-addhar');
// let govID = document.getElementById('r-govID');
let r_userid = document.getElementById('r-userid');

// input elments in forms
let firstname = document.getElementById('firstname');
let secondname = document.getElementById('secondname');
let email = document.getElementById('email');
let phone = document.getElementById('phone-no');
let address = document.getElementById('address');
let addhar_no = document.getElementById('addhar-no');
let user_id = document.getElementById('user-id');
let password = document.getElementById('password');
let confirm_passowd = document.getElementById('confirm-password');
let validation_error = document.getElementById('validation-error');

let verify_flag = false;



firstname.addEventListener("change", () => {

    r_fname.querySelector("span").innerText = " = " + firstname.value;

})
secondname.addEventListener("change", () => {

    r_sname.querySelector("span").innerText = " = " + secondname.value;

})
email.addEventListener("change", () => {
    r_email.querySelector("span").innerText = " = " + email.value;
})
phone.addEventListener("change", () => {
    r_phone.querySelector("span").innerText = " = " + phone.value;
})

// address.addEventListener("change", () => {
//     r_address.querySelector("span").innerText = " = " + address.value;
// })

addhar_no.addEventListener("change", () => {
    r_addhar.querySelector("span").innerText = " = " + addhar_no.value;
})
user_id.addEventListener("change", () => {
    r_userid.querySelector("span").innerText = " = " + user_id.value;
})
password.addEventListener("change", () => {
    // r_fname.querySelector("span").innerText = password.value;
})
confirm_passowd.addEventListener("change", () => {
    // r_fname.querySelector("span").innerText = confirm_passowd.value;
})

if (start) {
    // console.log("runing");
    form_input.forEach((item) => {
        item.style.display = "none";
    });
    index = 0;
    start = false;
    form_input[index].style.display = "block";
}


previous.addEventListener("click", () => {
    // console.log("working")
    validation_error.innerHTML = "";
    if (index <= 0) {
        previous.disabled = true
    } else {

        index = index - 1;
        if (index < form_input.length && index >= 0) {
            previous.disabled = false;
            form_input[index].style.display = "block";

            // form_input[index].style.display = "none";
            let temp = index;
            for (let index = 0; index < form_input.length; index++) {
                if (index != temp) {
                    form_input[index].style.display = "none";
                }
            }
            index = temp;
            next.textContent = "Next"
        } else {
            previous.disabled = true;
        }
    }
});
next.addEventListener("click", () => {
    console.log(index)
    let input_element = form_input[index].querySelectorAll('input')
    // input_element[0].placeholder
    if (validate_input(input_element)) {

        index++;

        if (index < form_input.length && index >= 0) {
            // console.log(form_input[index])
            form_input[index].style.display = "block";
            // console.log(index);
            let temp = index;
            for (let index = 0; index < form_input.length; index++) {
                if (index != temp) {
                    form_input[index].style.display = "none";
                }
            }
            index = temp;
            // console.log(index);
            previous.disabled = false;
            next.textContent = "Next"
        }
        if (index == form_input.length - 1) {

            next.textContent = "Submit";

        }
        if (index >= form_input.length) {
            // console.log("working")
            // console.dir(next.type)
            next.type = "submit";
            // console.dir(next.type)
        }
    }

});

function validate_input(input_element) {
    let count_input = -1
    let error_input = 0
    let error_message = {}
    for (let i = 0; i < input_element.length; i++) {
        let element = input_element[i];

        if (element.value == null || element.value.length <= 0 || element.value == "") {
            error_input++;
            count_input = i
            error_message[error_input] = "<li>Invalid!.. input is empty, Please " + element.placeholder.toString() + "</li>";

        }

    }

    if (input_element[0].id == "email") {
        console.log("entering to email part")
       if(! ValidateEmail(input_element[0])){
            error_input++;
            error_message[error_input]="<li>Invalid!.. Email format is incorrect, Please " + input_element[0].placeholder.toString() + "</li>"
       }
    }
    
    if (error_input > 0) {
        validation_error.innerHTML = ""
        for (const key in error_message) {
            // console.log(key)
            let element = error_message[key];
            validation_error.innerHTML += element;
        }
    }
    else {
        validation_error.innerHTML = ""
        return true
    }



}

function ValidateEmail(input) {

    // var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if (input.value.match(mailformat)) {


        // document.form1.text1.focus();

        return true;

    } else {

        // alert("Invalid email address!");

        // document.form1.text1.focus();

        return false;

    }

}
