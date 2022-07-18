let form_input = document.querySelectorAll(".form-input");
let previous = document.getElementById("previous");
let next = document.getElementById("next");
let body = document.querySelector("body");
var index;
let start = true;

// if (index==0) {
//     form_input.forEach(item => {

//         item.style.display = "none";
//     });
//     form_input[index].style.display = "block"
// }
// console.dir(form_input)
// console.log(form_input.length)

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
    if (index < form_input.length && index > 0) {
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
