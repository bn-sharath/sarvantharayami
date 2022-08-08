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

form_container.style.display = "none";
display_error_u.style.display = "none";
gov_form.style.display = "none";
private_form.style.display = "none";
public_form.style.display = "none";
general_form.style.display = "none";
// console.dir(form_container);

gov.addEventListener("click", () => {

    console.log("u clicked this")
    // Create an XMLHttpRequest object
const xhttp = new XMLHttpRequest();

// Define a callback function
xhttp.onload = function() {
  // Here you can use the Data
  
  display_error_u.style.display = "none";
  
  form_container.style.display = "block";
  gov_form.style.display = "block";
  private_form.style.display = "none";
  public_form.style.display = "none";
  general_form.style.display = "none";
}

// Send a request
xhttp.open("GET", "/sendmail/1");
xhttp.send();
});

public.addEventListener("click", () => {
    display_error_u.style.display = "none";

    form_container.style.display = "block";
    gov_form.style.display = "none";
    private_form.style.display = "none";
    public_form.style.display = "block";
    general_form.style.display = "none";
});
private.addEventListener("click", () => {
    display_error_u.style.display = "none";

    form_container.style.display = "block";
    gov_form.style.display = "none";
    private_form.style.display = "block";
    public_form.style.display = "none";
    general_form.style.display = "none";
});
general.addEventListener("click", () => {
    display_error_u.style.display = "none";

    form_container.style.display = "block";
    gov_form.style.display = "none";
    private_form.style.display = "none";
    public_form.style.display = "none";
    general_form.style.display = "block";
});

function validation(form_control) {
    //   display_error_u.innerHTML = "";
    // let otp_control = form_control.getElementsByName("otp")
    //   let elemets = form_control.querySelectorAll(".input-set input");
    //   elemets.forEach((element) => {
    //     if (
    //       element.value == null ||
    //       element.value.length <= 0 ||
    //       element.value == ""
    //     ) {
    //       display_error_u.style.display = "block";
    //       display_error_u.innerHTML +=
    //         "<li>input is empty please " + element.placeholder + "</li>";
    //     }
    //   });
    //   console.log(otpValidation(otp_control));
    return false;

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
