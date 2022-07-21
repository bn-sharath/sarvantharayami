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
address.addEventListener("change", () => {
    r_address.querySelector("span").innerText = " = " + address.value;
})
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
});
next.addEventListener("click", () => {
    // console.log("working")
    let input_element = form_input[index].querySelectorAll('input')
    // console.log(input_element[0].placeholder)
    // console.log(input_element[0].id)
    if(!verify_flag){
        input_element.forEach(element => {
            if((element.value == null) || (element.value.length <= 0) || (element.value == "")) {
                // alert("Input is empty please Enter the valid input")
                validation_error.innerHTML += "<li>Invalid!..Input is Empty " + element.placeholder +"<br></li>";
                element.focus;
                
            }
          
            
        });
     
    }


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

});


