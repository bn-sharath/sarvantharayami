let form_input = document.querySelectorAll(".form-input");
let previous = document.getElementById("previous");
let next = document.getElementById("next");
let body = document.querySelector("body");
var index;
let start = true;


// showing the data
let profile = document.getElementById('r-profile');
let name = document.getElementById('r-name');
let email = document.getElementById('r-email');
let phone = document.getElementById('r-phone');
let address = document.getElementById('r-address');
let addhar = document.getElementById('r-addhar');
let govID = document.getElementById('r-govID');
let userid = document.getElementById('r-userid');


if (start) {
    console.log("runing");
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
        next.textContent="Next"
    } else {
        previous.disabled = true;
    }
});
next.addEventListener("click", () => {
    // console.log("working")
    
    index = index + 1;
    if (index < form_input.length  && index >= 0) {
        // console.log(form_input[index])
        form_input[index].style.display = "block";
        console.log(index);
        let temp = index;
        for (let index = 0; index < form_input.length; index++) {
            if (index != temp) {
                form_input[index].style.display = "none";
            }
        }
        index = temp;
        console.log(index);
        previous.disabled = false;
        next.textContent="Next"
    }
    if (index==form_input.length-1) {

        next.textContent = "Submit";
        
    }
    if (index >= form_input.length ) {
        // console.log("working")
        // console.dir(next.type)
        next.type = "submit";
        // console.dir(next.type)
    } 
});

function data_show() {
    
}
